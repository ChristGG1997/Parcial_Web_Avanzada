import { NextRequest, NextResponse } from "next/server";

export async function GET(req: NextRequest) {
  if (req.method === "GET") {
  } else {
    return new NextResponse(
      JSON.stringify({ message: `Method ${req.method} Not Allowed` }),
      { status: 405 }
    );
  }
}
