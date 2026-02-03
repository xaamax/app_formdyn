import { FormTypeEnum } from "../enums/form-type-enum"

export interface FormDTO {
    id: number
    name: string
    type: FormTypeEnum
}