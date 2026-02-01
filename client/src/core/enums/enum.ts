type EnumLike = Record<string, string | number>;

export function enumWithLabelToOptions<
  TEnum extends EnumLike,
  TValue extends TEnum[keyof TEnum] & number
>(
  enumObj: TEnum,
  labels: Record<TValue, string>
) {
  return Object.values(enumObj)
    .filter((v): v is TValue => typeof v === "number")
    .map((value) => ({
      value,
      label: labels[value],
    }));
}