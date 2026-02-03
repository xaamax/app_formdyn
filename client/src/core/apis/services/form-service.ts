import { URL_FORMS } from "@/core/constants/urls";
import { ApiResult, get } from "./api";
import { FormDTO } from "@/core/dto/form-dto";
import { PaginationResponseDTO } from "@/core/dto/pagination-dto";

export const getFormsAll = (): Promise<
  ApiResult<PaginationResponseDTO<FormDTO>>
> => get(URL_FORMS);
