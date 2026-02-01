import { useGetAllMatriculasByTurma } from "@/core/apis/queries/gestao";
import SelectInput from "../inputs/select-input";

type Props = {
  form?: any;
};

export function SelectInputMatriculas({ form }: Props) {
  const turma = form.watch("turma");

  const { data, isLoading } = useGetAllMatriculasByTurma(turma);

  if (!data?.length && isLoading) return null;

  return (
    <SelectInput
      type="number"
      isLoading={isLoading}
      label="Aluno(a)"
      placeholder="Selecione o Aluno(a)"
      name="matricula"
      withAsterisk
      data={data || []}
      form={form}
    />
  );
}
