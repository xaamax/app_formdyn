export const formKeys = {
  all: ["forms"] as const,
  detail: (id: string) => [...formKeys.all, id] as const,
  filters: ({ }) => [...formKeys.all] as const,
};
