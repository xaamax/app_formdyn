import { Cross2Icon } from "@radix-ui/react-icons";
import { Table } from "@tanstack/react-table";
import { Input } from "@/components/ui/input";
import { DataTableViewOptions } from "@/components/data-table/data-table-view-options";
import { Button } from "@/components/ui/button";
import { DataTableFacetedFilter } from "@/components/data-table/data-table-faceted-filter";
import { useNavigate } from "react-router-dom";
import { PlusCircle } from "lucide-react";

interface DataTableToolbarProps<TData> {
  table: Table<TData>;
  facetedFilters?: { field: string; label: string }[];
}

export function DataTableToolbar<TData>({
  table,
  facetedFilters,
}: DataTableToolbarProps<TData>) {
  const isFiltered = table.getState().columnFilters.length > 0;

  const navigate = useNavigate();

  return (
    <div className="flex items-center justify-between gap-2">
      <div className="flex flex-1 flex-col-reverse items-start gap-y-2 sm:flex-row sm:items-center sm:space-x-2">
        <Input
          placeholder="Pesquisar..."
          value={(table.getState().globalFilter as string) ?? ""}
          onChange={(event) => table.setGlobalFilter(event.target.value)}
          className="h-8 w-[200px] lg:w-[250px]"
        />
        <div className="flex gap-x-2">
          {facetedFilters?.length && (
            <>
              {facetedFilters.map(({ field, label }, index) => (
                <DataTableFacetedFilter
                  key={index}
                  column={table.getColumn(field)}
                  title={label}
                  options={Array.from(
                    table
                      .getColumn(field)
                      ?.getFacetedUniqueValues()
                      ?.entries() ?? []
                  ).map(([value]) => ({
                    label: String(value),
                    value: String(value),
                  }))}
                />
              ))}
            </>
          )}
        </div>
        {isFiltered && (
          <Button
            variant="ghost"
            onClick={() => table.resetColumnFilters()}
            className="h-8 px-2 lg:px-3"
          >
            Limpar
            <Cross2Icon className="ml-2 h-4 w-4" />
          </Button>
        )}
      </div>
      <Button
        size="sm"
        className="ml-auto hidden h-8 lg:flex"
        onClick={() => navigate("/ocorrencias/incluir")}
      >
        <PlusCircle className="mr-2 h-4 w-4" />
        Incluir
      </Button>
      <DataTableViewOptions table={table} />
    </div>
  );
}
