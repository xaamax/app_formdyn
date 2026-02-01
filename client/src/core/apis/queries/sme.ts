import { useQuery } from "@tanstack/react-query";
import { dreKeys } from "./keys";
import { DreDTO, getDres, getUesPorDre, UeDTO } from "../services/sme-service";

export function useGetAllDres() {
  return useQuery({
    queryKey: dreKeys.filters({}),
    queryFn: getDres,
    select: (data) =>
      data.data?.map((dre: DreDTO) => ({
        value: dre.codigo_dre,
        label: dre.nome,
      })),
  });
}

export function useGetAllUesByDre(codigo_dre: string) {
  return useQuery({
    queryKey: ["ues", codigo_dre],
    queryFn: () => getUesPorDre(codigo_dre),
    enabled: !!codigo_dre,
    select: (data) =>
      data.data?.map((ue: UeDTO) => ({
        value: ue.codigo_ue,
        label: ue.nome,
      })),
  });
}