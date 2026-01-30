from enum import IntEnum


class FormTypeEnum(IntEnum):
    FORMULARIO_ENSINO_FUNDAMENTAL = 1
    FORMULARIO_ENSINO_MEDIO = 2
    FORMULARIO_EJA = 3

    @property
    def label(self) -> str:
        labels = {
            FormTypeEnum.FORMULARIO_ENSINO_FUNDAMENTAL: "Formulário Ensino Fundamental",
            FormTypeEnum.FORMULARIO_ENSINO_MEDIO: "Formulário Ensino Médio",
            FormTypeEnum.FORMULARIO_EJA: "Formulário EJA",
        }
        return labels[self]
