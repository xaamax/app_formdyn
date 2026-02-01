import { Button } from "@/components/ui/button";
import { Calendar } from "@/components/ui/calendar";
import { format } from "date-fns";
import {
  FormControl,
  FormDescription,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form";
import { PopoverContent } from "@/components/ui/popover";
import { cn } from "@/core/lib/utils";
import { Popover, PopoverTrigger } from "@radix-ui/react-popover";
import { CalendarIcon } from "lucide-react";
import { ptBR } from "date-fns/locale";
import { useState } from "react";

interface Props {
  label?: string;
  placeholder?: string;
  description?: string;
  name: string;
  withAsterisk?: boolean;
  form?: any;
}

function DateInput({
  label,
  placeholder,
  description,
  withAsterisk = false,
  name,
  form,
}: Props) {
  const [open, setOpen] = useState(false);

  return (
    <FormField
      control={form.control}
      name={name}
      render={({ field }) => {
        const selectedDate = field.value
          ? new Date(field.value)
          : undefined;

        return (
          <FormItem className="flex flex-col">
            {(label || withAsterisk) && (
              <FormLabel className="flex items-center gap-1">
                {withAsterisk && (
                  <span className="mt-1 text-destructive">*</span>
                )}
                {label}
              </FormLabel>
            )}

            <Popover open={open} onOpenChange={setOpen}>
              <PopoverTrigger asChild>
                <FormControl>
                  <Button
                    variant="outline"
                    className={cn(
                      "pl-3 text-left font-normal hover:bg-background",
                      !field.value && "text-muted-foreground"
                    )}
                  >
                    {field.value ? (
                      format(selectedDate!, "PPP", { locale: ptBR })
                    ) : (
                      <span>{placeholder}</span>
                    )}
                    <CalendarIcon className="ml-auto h-4 w-4 opacity-50" />
                  </Button>
                </FormControl>
              </PopoverTrigger>

              <PopoverContent className="w-auto p-0" align="start">
                <Calendar
                  locale={ptBR}
                  mode="single"
                  selected={selectedDate}
                  onSelect={(date) => {
                    if (!date) return;

                    field.onChange(date.toISOString());
                    setOpen(false);
                  }}
                  disabled={(date) =>
                    date > new Date() || date < new Date("1900-01-01")
                  }
                  initialFocus
                />
              </PopoverContent>
            </Popover>

            {description && (
              <FormDescription>{description}</FormDescription>
            )}

            <FormMessage />
          </FormItem>
        );
      }}
    />
  );
}


export default DateInput;
