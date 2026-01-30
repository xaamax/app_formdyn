from enum import IntEnum


class FieldTypeEnum(IntEnum):
    FRASE = 1
    TEXTO = 2
    NUMERICO = 3
    DATA = 4
    RADIO = 5
    SELECT = 6
    CHECKBOX = 7
    UPLOAD = 8

    @property
    def label(self) -> str:
        labels = {
            FieldTypeEnum.FRASE: 'Frase',
            FieldTypeEnum.TEXTO: 'Texto',
            FieldTypeEnum.NUMERICO: 'Numérico',
            FieldTypeEnum.DATA: 'Data',
            FieldTypeEnum.RADIO: 'Radio',
            FieldTypeEnum.SELECT: 'Select',
            FieldTypeEnum.CHECKBOX: 'Checbox',
            FieldTypeEnum.UPLOAD: 'Upload',
        }
        return labels[self]
