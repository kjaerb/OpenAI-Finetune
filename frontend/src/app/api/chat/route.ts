import { NextResponse } from "next/server";
import { Configuration, OpenAIApi } from "openai-edge";
import { OpenAIStream, StreamingTextResponse } from "ai";

const config = new Configuration({
  apiKey: process.env.OPEN_AI_KEY as string,
});

const promptMessages: OpenAIMessage[] = [
  {
    role: "system",
    content:
      "Du skriver varebeskrivelser for et dansk B2B virksomed. Skriv en produkt beskrivelse, som maks er 150 ord. Skriv først en beskrivelse og derefter en liste med specifikationer",
  },
];

const openai = new OpenAIApi(config);

export async function POST(req: Request) {
  const { messages } = await req.json();

  const contextMessage = [...promptMessages, ...messages];
  console.log(contextMessage);

  const response = await openai.createChatCompletion({
    model: "gpt-3.5-turbo",
    stream: true,
    messages: contextMessage,
  });

  if (!response.ok) {
    return NextResponse.json("Something went wrong. Try again later");
  }

  console.log(response);

  const stream = OpenAIStream(response);

  return new StreamingTextResponse(stream);
}
