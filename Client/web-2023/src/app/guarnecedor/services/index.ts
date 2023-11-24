import { Ticket } from "@/services/app.services";

export const createPackage = async (data: Ticket) => {
  const response = await fetch("/api/createPackage", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });
  return {};
};
