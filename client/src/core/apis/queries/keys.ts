export const ocorrenciaKeys = {
  all: ["ocorrencias"] as const,
  lists: () => [...ocorrenciaKeys.all, "list"] as const,
  list: (filters: object) =>
    [...ocorrenciaKeys.lists(), filters] as const,


  dashboard: () => [...ocorrenciaKeys.all, "dashboard"] as const,
  dashboardWithFilters: (filters: Record<string, any>) =>
    [...ocorrenciaKeys.dashboard(), filters] as const,

  details: () => [...ocorrenciaKeys.all, "detail"] as const,
  detail: (id: number) =>
    [...ocorrenciaKeys.details(), id] as const,
};

export const dreKeys = {
  all: ["dre"] as const,
  detail: (id: string) => [...dreKeys.all, id] as const,
  filters: ({ }) => [...dreKeys.all] as const,
};
