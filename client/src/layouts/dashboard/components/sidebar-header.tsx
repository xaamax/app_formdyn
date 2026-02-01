import Logo from "@/assets/logo.png"
import Text from "@/components/commons/text";
import useUserPreference from "@/core/stores/user-preference";
import clsx from "clsx";

function SidebarHeader() {
  const { sidebarCollapsed } = useUserPreference();

  return (
    <div
      className={clsx(
        "flex items-center gap-2 my-3",
        sidebarCollapsed && "justify-center"
      )}
    >
      <div
        className={clsx(
          "h-8 w-8 ml-[5px] border flex items-center justify-center rounded-full bg-secondary font-semibold text-primary-foreground"
        )}
      >
        <img src={Logo} className="h-5 w-5 text-primary-foreground transition-all group-hover:scale-110" />
      </div>

      {!sidebarCollapsed && (
        <div className="flex flex-col h-[30px] flex-1 overflow-hidden">
          <Text size="lg">FormDyn</Text>                         
        </div>
      )}
    </div>
  );
}

export default SidebarHeader;
