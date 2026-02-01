import { getOcorrenciaDetalhes, getOcorrencias, getOcorrenciasDashboard } from "@/core/apis/services/ocorrencia-service";
import { useQuery } from "@tanstack/react-query";
import { ocorrenciaKeys } from "./keys";


export function useGetOcorrenciasDashboard(filters: {
  ano_letivo: number
  codigo_dre?: string
  codigo_ue?: string
}) {
  return useQuery({
    queryKey: ocorrenciaKeys.dashboardWithFilters(filters),
    queryFn: () => getOcorrenciasDashboard(filters),
    enabled: !!filters.ano_letivo,
  })
}


export function useGetAllOcorrencias(filters = {}) {
  return useQuery({
    queryKey: ocorrenciaKeys.list(filters),
    queryFn: getOcorrencias,
  });
}

export function useGetOcorrenciaPorId(id: number) {
  return useQuery({
    queryKey: ocorrenciaKeys.detail(id),
    queryFn: () => getOcorrenciaDetalhes(id),
    enabled: !!id,
  });
}
