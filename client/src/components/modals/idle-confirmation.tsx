import Text from "@/components/commons/text";
import { Button } from "@/components/ui/button";
import { useModal } from "@saimin/react-modal-manager";

interface Props {
  onLogout: () => void;
}

function IdleConfirmation({ onLogout }: Props) {
  const { closeAll } = useModal();

  const handleLogout = () => {
    onLogout();
    closeAll();
  };

  return (
    <div className="w-[400px] rounded-lg overflow-hidden bg-background p-4">
      <Text size="lg">
        <b>Você ficou ocioso.</b>
      </Text>

      <br />

      <div className="flex gap-4 justify-end">
        <Button onClick={handleLogout} variant="secondary">
          Logout
        </Button>

        <Button onClick={closeAll}>Continuar</Button>
      </div>
    </div>
  );
}

export default IdleConfirmation;
