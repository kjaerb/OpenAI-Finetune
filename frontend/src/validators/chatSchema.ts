import { z } from "zod";

export const chatSchema = z.object({
  message: z
    .string()
    .min(1, {
      message: "Beskeden er for kort",
    })
    .max(255, { message: "Beskeden er for lang. Maks 255 tegn" }),
});

export type ChatSchema = z.infer<typeof chatSchema>;
