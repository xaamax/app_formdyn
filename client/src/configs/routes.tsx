import { createBrowserRouter, Navigate } from "react-router-dom";
import { DashboardLayout } from "@/layouts/dashboard/dashboard-layout";
import RootLayout from "@/layouts/root/root-layout";
import {
  Formularios,
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
            element: <Navigate to="formularios/consultar" replace />,
          },
          {
            index: true,
            path: "formularios/consultar",
            element: <Formularios />,
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
