import { useQuery } from "@tanstack/react-query";
import { getMatriculasPorTurma, getTurmasPorUe, TurmaDTO } from "../services/gestao-service";
import { AlunoDTO } from "@/core/dto/matricula-dto";

export function useGetAllTurmasByUe(codigo_ue: string) {
  return useQuery({
    queryKey: ["turmas", codigo_ue],
    queryFn: () => getTurmasPorUe(codigo_ue),
    enabled: !!codigo_ue,
    select: (data) =>
      data.data?.map((turma: TurmaDTO) => ({
        value: String(turma.id),
        label: turma.nome,
      })),
  });
}

export function useGetAllMatriculasByTurma(turma_id: number) {
  return useQuery({
    queryKey: ["matriculas", turma_id],
    queryFn: () => getMatriculasPorTurma(turma_id),
    enabled: !!turma_id,
    select: (data) =>
      data.data?.map((aluno: AlunoDTO) => ({
        value: String(aluno.id),
        label: aluno.nome,
      })),
  });
}