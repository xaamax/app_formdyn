import { createBrowserRouter, Navigate } from "react-router-dom";
import { DashboardLayout } from "@/layouts/dashboard/dashboard-layout";
import RootLayout from "@/layouts/root/root-layout";
import {
  PainelControle,
  Error404,
} from "@/pages/index";

export const router = createBrowserRouter([
  {
    path: "/",
    element: <RootLayout />,
    children: [
      {
        path: "",
        element: <DashboardLayout />,
        children: [
          {
            index: true,
            element: <Navigate to="painel-controle" replace />,
          },
          {
            index: true,
            path: "painel-controle",
            element: <PainelControle />,
          },
        ],
      },
    ]
  },
  {
    path: "/*",
    element: <Error404 />,
  },
]);
