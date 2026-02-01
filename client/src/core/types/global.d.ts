declare global {
  type Lang = "en" | "mm";

  type Theme = "dark" | "light";

  type DataType = { value: string | number | undefined; label: string };
}

export {};
