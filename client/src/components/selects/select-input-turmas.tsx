import { useGetAllTurmasByUe } from "@/core/apis/queries/gestao";
import SelectInput from "../inputs/select-input";

type Props = {
  form?: any;
  withAsterisk?: boolean;
};

export function SelectInputTurmas({ form, withAsterisk }: Props) {
  const ue = form.watch("ue");

  const { data, isLoading } = useGetAllTurmasByUe(ue);

  if (!data?.length && isLoading) return null;

  return (
    <SelectInput
      isLoading={isLoading}
      label="Turma"
      placeholder="Selecione a Turma"
      name="turma"
      withAsterisk={withAsterisk}
      data={data || []}
      form={form}
    />
  );
}
