import { NextRequest, NextResponse } from "next/server";

let array: any[] = [];

export async function POST(req: NextRequest) {
  if (req.method === "POST") {
    array.push(await req.json());
    return new NextResponse(
      JSON.stringify({
        message: `Hello from Next.js! ${array.length}`,
        data: array,
      }),
      { status: 200 }
    );
  } else {
    return new NextResponse(
      JSON.stringify({ message: `Method ${req.method} Not Allowed` }),
      { status: 405 }
    );
  }
}
