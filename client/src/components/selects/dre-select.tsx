import { useGetAllDres } from "@/core/apis/queries/sme";
import SelectInput from "@/components/inputs/select-input";

interface Props {
  label?: string;
  placeholder?: string;
  description?: string;
  withAsterisk?: boolean;
  name: string;
  form?: any;
  isLoading?: boolean;
  className?: string;
  hideSelectAll?: boolean;
}

export function DreSelect(props: Props) {
  const { data = [], isLoading } = useGetAllDres();

  const dres = props.hideSelectAll
    ? data
    : [
        {
          value: "todas",
          label: "Todas",
        },
        ...data,
      ];

  return (
    <SelectInput
      data={dres}
      label={props.label || "Diretoria Regional de Educação (DRE)"}
      placeholder={props.placeholder || "Selecione a DRE"}
      isLoading={isLoading}
      {...props}
    />
  );
}
