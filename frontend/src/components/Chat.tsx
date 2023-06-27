"use client";

import { useChat } from "ai/react";
import { Input } from "@/components/ui/Input";
import { Button } from "@/components/ui/Button";
import { cn } from "@/lib/utils";
import { Textarea } from "./ui/Textarea";
import { ChatForm } from "./ChatForm";

interface ChatProps extends React.ComponentProps<"div"> {}

export function Chat({ className, ...props }: ChatProps) {
  const { input, messages, handleSubmit, setInput } = useChat();

  console.log(input);

  return (
    <div
      {...props}
      className={cn("flex flex-col justify-between h-full", className)}
    >
      <div className="border overflow-scroll">
        <p>Enter chat</p>
        {messages.map((message) => (
          <div key={message.id} className="whitespace-pre-wrap">
            {message.role} says: {message.content}
          </div>
        ))}
      </div>
      <ChatForm />
    </div>
  );
}
