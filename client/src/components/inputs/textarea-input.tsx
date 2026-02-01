import {
  FormControl,
  FormDescription,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form";
import { Textarea } from "@/components/ui/textarea";

interface Props {
  label?: string;
  placeholder?: string;
  description?: string;
  withAsterisk?: boolean;
  name: string;
  rows?: number;
  form?: any;
}

function TextareaInput({
  label,
  placeholder,
  description,
  withAsterisk = false,
  name,
  rows,
  form,
}: Props) {
  return (
    <FormField
      control={form.control}
      name={name}
      render={({ field }) => {
        return (
          <FormItem>
            {(label || withAsterisk) && (
              <FormLabel className="flex items-center gap-1">
                {withAsterisk && (
                  <span className="mt-1 text-destructive">*</span>
                )}
                {label}{" "}
              </FormLabel>
            )}
            <FormControl>
              <Textarea
                placeholder={placeholder}
                className="resize-none"
                rows={rows}
                {...field}
              />
            </FormControl>
            {description && <FormDescription>{description}</FormDescription>}
            <FormMessage />
          </FormItem>
        );
      }}
    />
  );
}

export default TextareaInput;
