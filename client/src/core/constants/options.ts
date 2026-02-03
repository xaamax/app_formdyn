import { enumWithLabelToOptions } from "../enums/enum";
import { FormTypeEnum } from "../enums/form-type-enum";

export const FormTypeEnumLabel: Record<FormTypeEnum, string> = {
  [FormTypeEnum.FORMULARIO_EJA]: "EJA",
  [FormTypeEnum.FORMULARIO_ENSINO_FUNDAMENTAL]: "EF",
  [FormTypeEnum.FORMULARIO_ENSINO_MEDIO]: "EM",
};

export const FORM_TYPE_OPTIONS = enumWithLabelToOptions(
  FormTypeEnum,
  FormTypeEnumLabel
);