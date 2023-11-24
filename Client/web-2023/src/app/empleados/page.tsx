'use client'
import React, { useState } from "react"

const TicketsComponent = () => {
  const [tickets, setTickets] = useState([
    {
      id: "1",
      name: "Ticket 1",
      product: "Goma",
      quantity: 12,
      role: "Guarnecedor",
      date: new Date("2023-11-24"),
      price: 1200
    },
    {
      id: "2",
      name: "Ticket 2",
      product: "Cordon",
      quantity: 12,
      role: "Guarnecedor",
      date: new Date("2023-11-25"),
      price: 2400
    },
    {
      id: "3",
      name: "Ticket 3",
      product: "Suela",
      quantity: 12,
      role: "Guarnecedor",
      date: new Date("2023-11-26"),
      price: 3600
    },
    {
      id: "4",
      name: "Ticket 4",
      product: "Cordon",
      quantity: 5,
      role: "Guarnecedor",
      date: new Date("2023-11-26"),
      price: 1000
    }
  ]);

  const incompletePackagesTotalPrice = tickets
    .filter(ticket => ticket.quantity < 12)
    .reduce((total, ticket) => total + ticket.price, 0);

  const completePackagesTotalPrice = tickets
    .filter(ticket => ticket.quantity === 12)
    .reduce((total, ticket) => total + ticket.price, 0);

  const totalTicketsPrice = tickets.reduce((total, ticket) => total + ticket.price, 0);

  return (
    <div className="flex flex-col h-screen">
      <div className="flex flex-row justify-center items-center w-full">
        <h1 className="text-2xl font-bold mb-4">Tickets</h1>
      </div>
      <div className="flex flex-col flex-wrap mt-4">
        {tickets.map((ticket) => (
          <div className="flex flex-row justify-between items-center w-full mb-4 p-4 border-2 border-black rounded" key={ticket.id}>
            <div className="flex flex-row">
              <div className="flex flex-col mr-4">
                <p className="text-xl font-medium">Número de ticket:</p>
                <p className="text-md font-normal">{ticket.name}</p>
              </div>
              <div className="flex flex-col">
                <p className="text-xl font-medium">Producto:</p>
                <p className="text-md font-normal">{ticket.product}</p>
              </div>
            </div>
            <div className="flex flex-col">
              <p className="text-xl font-medium">Cantidad:</p>
              <p className="text-md font-normal">{ticket.quantity}</p>
            </div>
            <div className="flex flex-col">
              <p className="text-xl font-medium">Precio:</p>
              <p className="text-md font-normal">{ticket.price}</p>
            </div>
            <div className="flex flex-col">
              <p className="text-xl font-medium">Rol:</p>
              <p className="text-md font-normal">{ticket.role}</p>
            </div>
            <div className="flex flex-col">
              <p className="text-xl font-medium">Fecha:</p>
              <p className="text-md font-normal">{ticket.date.toLocaleString()}</p>
            </div>
          </div>
        ))}
        <div className="flex flex-row justify-between items-center w-full mt-4">
          <h2 className="text-xl font-bold">Cantidad total en paquetes incompletos: {incompletePackagesTotalPrice}</h2>
          <h2 className="text-xl font-bold">Total paquetes completos: {completePackagesTotalPrice}</h2>
          <h2 className="text-xl font-bold">Total: {totalTicketsPrice}</h2>
        </div>
      </div>
    </div>
  );
};

export default TicketsComponent;
