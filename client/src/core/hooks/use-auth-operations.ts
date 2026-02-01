import { AuthResponseDTO } from "@/core/apis/services/auth-service";
import Cookie from "js-cookie";

const AUTH_KEY = "@app:auth";

export const getAuth = (): AuthResponseDTO | null => {
  const data = Cookie.get(AUTH_KEY);
  return data ? JSON.parse(data) : null;
};

export const setAuth = (auth: AuthResponseDTO) => {
  Cookie.set(AUTH_KEY, JSON.stringify(auth));
  window.location.href = "/"
};

export const closeAuth = () => {
  Cookie.remove(AUTH_KEY);
};

