import { getFormsAll } from "@/core/apis/services/form-service";
import { useQuery } from "@tanstack/react-query";
import { formKeys } from "./keys";


export function useGetAllForms() {
  return useQuery({
    queryKey: formKeys.filters({}),
    queryFn: getFormsAll
  });
}
