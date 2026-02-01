import axios, {
  AxiosError,
  type AxiosRequestConfig,
  type AxiosResponse,
  // HttpStatusCode,
  // type InternalAxiosRequestConfig,
} from "axios";
import type { ResponseBaseDTO } from "@/core/dto/response-base-dto";
// import { dayjs } from "@/core/date/dayjs";
import { toast } from "sonner";
// import authService, { URL_REFRESH_TOKEN } from "./auth-service";
// import { getAuth, setAuth } from "@/core/hooks/use-auth-operations";

const api = axios.create({
  baseURL: import.meta.env.VITE_SME_FORMDYN_API,
});

// const SEGUNDOS_ANTES_EXPIRAR = 0;
// let refreshTokenPromise: Promise<any> | null = null;

// const getRefreshToken = (access: string) =>
//   authService.refreshToken(access).then((resp) => resp.data);

// const revalidateAuth = async (oldToken: string) => {
//   if (!refreshTokenPromise) {
//     refreshTokenPromise = getRefreshToken(oldToken)
//       .then((data) => {
//         refreshTokenPromise = null;
//         if (data?.access) {
//           setAuth(data);
//         }
//         return data;
//       })
//       .catch(() => {
//         refreshTokenPromise = null;
//         authService.logout();
//       });
//   }

//   return refreshTokenPromise;
// };

// api.interceptors.request.use(
//   async (requestConfig: InternalAxiosRequestConfig) => {
//     const auth = getAuth();

//     if (!auth) return requestConfig;

//     const { access, expiresIn } = auth;

//     const diff = dayjs().diff(dayjs(expiresIn), "seconds");

//     if (requestConfig.headers) {
//       requestConfig.headers.Authorization = `Bearer ${access}`;
//     }

//     if (
//       requestConfig.url !== URL_REFRESH_TOKEN &&
//       diff >= SEGUNDOS_ANTES_EXPIRAR
//     ) {
//       const refreshed = await revalidateAuth(access);

//       if (refreshed?.access && requestConfig.headers) {
//         requestConfig.headers.Authorization = `Bearer ${refreshed.access}`;
//       }
//     }

//     return requestConfig;
//   },
//   (error) => Promise.reject(error)
// );

// api.interceptors.response.use(
//   (response: AxiosResponse) => response,
//   (error: AxiosError) => {
//     if (error.response?.status === HttpStatusCode.Unauthorized) {
//       authService.logout();
//     }

//     return Promise.reject(error);
//   }
// );

export type ApiResult<T> = {
  success: boolean;
  data: T | null;
  messages: string[];
  status?: number;
};

const tratarThen = <T>(response: AxiosResponse<T>): ApiResult<T> => ({
  success: true,
  data: response.data,
  messages: [],
});


const tratarCatch = (
  error: AxiosError<ResponseBaseDTO>
): ApiResult<any> => {
  const response = error.response?.data;

  const message =
    response?.error ?? "Erro ao processar a requisição. Tente novamente.";

  toast.error(message);

  return {
    success: false,
    data: null,
    messages: [message],
    status: response?.status ?? error.response?.status,
  };
};

export const get = async <T>(
  url: string,
  config?: AxiosRequestConfig
): Promise<ApiResult<T>> =>
  api.get(url, config).then(tratarThen).catch(tratarCatch);

export const post = async <T>(
  url: string,
  params?: any,
  config?: AxiosRequestConfig
): Promise<ApiResult<T>> =>
  api.post(url, params, config).then(tratarThen).catch(tratarCatch);

export const put = async <T>(
  url: string,
  params?: any,
  config?: AxiosRequestConfig
): Promise<ApiResult<T>> =>
  api.put(url, params, config).then(tratarThen).catch(tratarCatch);

export const patch = async <T>(
  url: string,
  params?: any
): Promise<ApiResult<T>> =>
  api.patch(url, params).then(tratarThen).catch(tratarCatch);

export const remove = async <T>(
  url: string,
  config?: AxiosRequestConfig
): Promise<ApiResult<T>> =>
  api.delete(url, config).then(tratarThen).catch(tratarCatch);

export default api;
