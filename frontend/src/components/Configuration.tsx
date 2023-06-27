import { cn } from "@/lib/utils";

interface ConfigurationProps extends React.ComponentProps<"div"> {}

export function Configuration({ className, ...props }: ConfigurationProps) {
  return (
    <div {...props} className={cn("h-full", className)}>
      Configuration
    </div>
  );
}
