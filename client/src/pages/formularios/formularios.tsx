import { Content } from "@/layouts/content";
import PageTitle from "@/components/commons/page-title";
import { Button } from "@/components/ui/button";
import { EllipsisVertical, PlusCircle } from "lucide-react";
import { useGetAllForms } from "@/core/apis/queries/form-query";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";

export function Formularios() {
  const { data } = useGetAllForms();

  return (
    <Content>
      <PageTitle
        hideToBack
        title="Formulários"
        desc="Gerencie os formulários existentes."
        actions={
          <Button>
            <PlusCircle className="h-5 w-5 mr-1" />
            Incluir Formulário
          </Button>
        }
      />
      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
        {data?.data?.items.map((form) => (
          <Card>
            <CardHeader>
              <div className="flex flex-grid justify-between text-primary">
                <CardTitle className="font-bold">#{form.id}</CardTitle>
                <EllipsisVertical />
              </div>
            </CardHeader>
            <CardContent className="space-y-1">
              <span className="font-medium">{form.name}</span>
              <CardDescription>{form.type}</CardDescription>
            </CardContent>
          </Card>
        ))}
      </div>
    </Content>
  );
}
