/* eslint-disable @typescript-eslint/no-explicit-any */
import React, { Ref, useRef, useState } from "react";
import {
  ColumnDef,
  ColumnFiltersState,
  SortingState,
  VisibilityState,
  flexRender,
  getCoreRowModel,
  getFacetedRowModel,
  getFacetedUniqueValues,
  getFilteredRowModel,
  getPaginationRowModel,
  getSortedRowModel,
  useReactTable,
} from "@tanstack/react-table";
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import { DataTablePagination } from "@/components/data-table/data-table-pagination";
import { DataTableToolbar } from "@/components/data-table/data-table-toolbar";

interface DataTableProps<TData> {
  columns: (
    toggleExpandedRow?: (index: number) => void,
    toggleRefreshTable?: () => void,
    expandedRow?: Ref<number | null>,
  ) => ColumnDef<TData>[];

  data: TData[];
  facetedFilters?: { field: string; label: string }[];
  onRefresh?: () => void;
}

export function DataTable<TData>({
  columns,
  data,
  facetedFilters,
  onRefresh,
}: DataTableProps<TData>) {
  const [rowSelection, setRowSelection] = useState({});
  const [columnVisibility, setColumnVisibility] = useState<VisibilityState>({});
  const [columnFilters, setColumnFilters] = useState<ColumnFiltersState>([]);
  const [sorting, setSorting] = useState<SortingState>([]);
  const [globalFilter, setGlobalFilter] = React.useState("");
  const expandedRow = useRef<number | null>(null);

  const globalFilterFn = React.useCallback(
    (row: any, _columnId: string, filterValue: string) => {
      const searchValue = filterValue.toLowerCase();

      const getValue = (obj: any): any => {
        if (Array.isArray(obj)) {
          return obj.flatMap((item) => getValue(item));
        }
        if (typeof obj === "object" && obj !== null) {
          return Object.values(obj).flatMap((value) => getValue(value));
        }
        return [String(obj).toLowerCase()];
      };

      const flattenedValues = getValue(row.original);
      return flattenedValues.some((value: any) => value.includes(searchValue));
    },
    [],
  );

  const toggleExpandedRow = (index: number) => {
    expandedRow.current = expandedRow.current === index ? null : index;
  };

  const toggleRefreshTable = () => {
    onRefresh?.();
  };

  const tableColumns = columns(
    toggleExpandedRow,
    toggleRefreshTable,
    expandedRow,
  );

  const table = useReactTable({
    data,
    columns: tableColumns,
    state: {
      sorting,
      columnVisibility,
      rowSelection,
      columnFilters,
      globalFilter,
    },
    enableRowSelection: true,
    onRowSelectionChange: setRowSelection,
    onSortingChange: setSorting,
    onColumnFiltersChange: setColumnFilters,
    onColumnVisibilityChange: setColumnVisibility,
    getCoreRowModel: getCoreRowModel(),
    getFilteredRowModel: getFilteredRowModel(),
    getPaginationRowModel: getPaginationRowModel(),
    getSortedRowModel: getSortedRowModel(),
    getFacetedRowModel: getFacetedRowModel(),
    getFacetedUniqueValues: getFacetedUniqueValues(),
    onGlobalFilterChange: setGlobalFilter,
    globalFilterFn,
  });

  return (
    <div className="space-y-4">
      <DataTableToolbar table={table} facetedFilters={facetedFilters} />
      <div className="rounded-md border">
        <Table>
          <TableHeader>
            {table.getHeaderGroups().map((headerGroup) => (
              <TableRow key={headerGroup.id} className="group/row">
                {headerGroup.headers.map((header) => {
                  return (
                    <TableHead
                      key={header.id}
                      colSpan={header.colSpan}
                      className={header.column.columnDef.meta?.className ?? ""}
                    >
                      {header.isPlaceholder
                        ? null
                        : flexRender(
                            header.column.columnDef.header,
                            header.getContext(),
                          )}
                    </TableHead>
                  );
                })}
              </TableRow>
            ))}
          </TableHeader>
          <TableBody>
            {table.getRowModel().rows?.length ? (
              table.getRowModel().rows.map((row) => (
                <TableRow
                  key={row.id}
                  data-state={row.getIsSelected() && "selected"}
                  className="group/row"
                >
                  {row.getVisibleCells().map((cell) => (
                    <TableCell
                      key={cell.id}
                      className={cell.column.columnDef.meta?.className ?? ""}
                    >
                      {flexRender(
                        cell.column.columnDef.cell,
                        cell.getContext(),
                      )}
                    </TableCell>
                  ))}
                </TableRow>
              ))
            ) : (
              <TableRow>
                <TableCell
                  colSpan={columns.length}
                  className="h-24 text-center"
                >
                  Nenhum registro encontrado.
                </TableCell>
              </TableRow>
            )}
          </TableBody>
        </Table>
      </div>
      <DataTablePagination table={table} />
    </div>
  );
}
