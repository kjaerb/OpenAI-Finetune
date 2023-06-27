"use client";

import { useForm } from "react-hook-form";
import {
  Form as FormProvider,
  FormField,
  FormItem,
  FormLabel,
  FormControl,
  FormDescription,
  FormMessage,
} from "./ui/Form";
import { ChatSchema, chatSchema } from "@/validators/chatSchema";
import { Textarea } from "./ui/Textarea";
import { zodResolver } from "@hookform/resolvers/zod";
import { Button } from "./ui/Button";
import { useChat } from "ai/react";
import { cn } from "@/lib/utils";

interface ChatFormProps {}

export function ChatForm({}: ChatFormProps) {
  const { setInput } = useChat();

  const form = useForm<ChatSchema>({
    resolver: zodResolver(chatSchema),
  });

  const { setValue } = form;

  return (
    <FormProvider {...form}>
      <form
        onSubmit={form.handleSubmit(submitChatMessage)}
        className="flex flex-col"
      >
        <div className="flex">
          <FormField
            control={form.control}
            name="message"
            render={({ field }) => (
              <FormItem className="mr-2 w-full">
                <FormMessage />
                <FormControl>
                  <Textarea placeholder="Skriv besked" {...field} />
                </FormControl>
              </FormItem>
            )}
          />
          <Button
            className="h-full px-8 max-h-[56px] self-end"
            variant={"green"}
          >
            Send
          </Button>
        </div>
        <FormDescription className="mt-2">
          Beskeden må gerne være varens navn eller hvordan du vil have den
          beskrevet.
        </FormDescription>
      </form>
    </FormProvider>
  );

  async function submitChatMessage(data: ChatSchema) {
    console.log("submitChatMessage", data);
    setInput(() => {
      return data.message;
    });

    setValue("message", "");
    setInput(() => {
      return "";
    });
  }
}
