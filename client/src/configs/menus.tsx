import {
  Plus,
  Search,
  LayoutDashboard,
} from "lucide-react";

const menus = [
  {
    name: "Formulários",
    icon: <LayoutDashboard className="h-[18px] w-[18px]" />,
    route: "ocorrencias",
    childs: [
      {
        name: "Incluir",
        icon: <Plus className="h-[18px] w-[18px]" />,
        route: "formularios/incluir",
      },
      {
        name: "Consultar",
        icon: <Search className="h-[18px] w-[18px]" />,
        route: "formularios/consultar",
      },
    ],
  },
];

export default menus;
