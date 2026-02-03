import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { ChevronRight } from "lucide-react";
import { Link } from "react-router-dom";

type Props = {
  title: string;
  icon?: React.ElementType;
  path?: string;
};

export default function Box({ title, icon: Icon, path }: Props) {
  return (
    <Card>
      <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
        {Icon && <Icon className="text-primary" />}
        <Link to={path || ""}>
          <ChevronRight className="text-primary" />
        </Link>
      </CardHeader>
      <CardContent>
        <CardTitle className="text-1xl font-medium">{title}</CardTitle>
      </CardContent>
    </Card>
  );
}
