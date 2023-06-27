import { Chat } from "@/components/Chat";
import { Configuration } from "@/components/Configuration";
import { Separator } from "@/components/ui/Separator";

export default function Home() {
  return (
    <main className="overflow-hidden h-screen w-full">
      <div className="p-4 flex items-center justify-between h-full">
        <Configuration className="flex-1" />
        <Separator orientation="vertical" className="mx-4 py-4" />
        <Chat className="flex-1" />
      </div>
    </main>
  );
}
