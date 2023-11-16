"use client"
import { SetStateAction, useState } from "react"

interface Product {
    product: string
    cantidad: number
    tickets: Ticket[]
}


interface Ticket extends Product {
    date: Date
}



export default function GuarnecedorSection() {
    const [product, setProduct] = useState("")
    const [cantidad, setCantidad] = useState<number>(0)
    const [productsList, setProductsList] = useState<Product[]>([])
    const [productError, setProductError] = useState(false)
    const [cantidadError, setCantidadError] = useState(false)
    const [tickets, setTickets] = useState<Ticket[]>([])

    const handleProductChange = (event: { target: { value: SetStateAction<string> } }) => {
        setProduct(event.target.value)
        setProductError(false)
    }

    const handleCantidadChange = (event: { target: { value: SetStateAction<string> } }) => {
        setCantidad(Number(event.target.value))
        setCantidadError(false)
    }

    const handleSave = () => {
        if (product === "") {
            setProductError(true);
            return;
        }
    
        if (cantidad === 0) {
            setCantidadError(true);
            return;
        }
    
        let existingProductIndex = productsList.findIndex(item => item.product.toLowerCase() === product.toLowerCase());
    
        if (existingProductIndex !== -1) {
            const updatedProductsList = [...productsList];
            const existingProduct = updatedProductsList[existingProductIndex];
    
            let totalQuantity = existingProduct.cantidad + cantidad;
    
            while (totalQuantity >= 12) {
                updatedProductsList.push({
                    product: existingProduct.product,
                    cantidad: 12,
                    tickets: [],
                });
                totalQuantity -= 12;
            }
    
            existingProduct.cantidad = totalQuantity;
    
            updatedProductsList[existingProductIndex] = existingProduct;
            setProductsList(updatedProductsList);
        } else {
            let totalQuantity = cantidad;
    
            while (totalQuantity >= 12) {
                productsList.push({
                    product,
                    cantidad: 12,
                    tickets: [],
                });
                totalQuantity -= 12;
            }
    
            if (totalQuantity > 0) {
                productsList.push({
                    product,
                    cantidad: totalQuantity,
                    tickets: [],
                });
            }
    
            setProductsList([...productsList]);
        }
    
        setProduct("");
        setCantidad(0);
    };
    
    const handleGenerateTickets = () => {
        const updatedProductsList = [...productsList];
    
        for (let i = 0; i < updatedProductsList.length; i++) {
            let totalQuantity = updatedProductsList[i].cantidad;
            let fullTicketsCount = Math.floor(totalQuantity / 12);
            let remainder = totalQuantity % 12;
    
            for (let j = 0; j < fullTicketsCount; j++) {
                updatedProductsList[i].tickets.push({
                    date: new Date(),
                    product: updatedProductsList[i].product,
                    cantidad: 12,
                    tickets: [],
                });
            }
    
            updatedProductsList[i].cantidad = remainder;
        }
    
        setProductsList(updatedProductsList);
    };
      
      
      

    const handleGenerateTicket = (index: number) => {
        const item = productsList[index]
        const ticket: Ticket = {
            date: new Date(),
            product: "",
            cantidad: 0,
            tickets: []
        }
        const upfechadProductsList = [...productsList]
        upfechadProductsList[index].tickets.push(ticket)
        setProductsList(upfechadProductsList)
        console.log("Generating ticket...")
    }

    const handleGeneratePackageTicket = (index: number) => {
        const item = productsList[index]
        const ticket: Ticket = {
            date: new Date(),
            product: "",
            cantidad: 0,
            tickets: []
        }
        const upfechadProductsList = [...productsList]
        upfechadProductsList[index].tickets.push(ticket)
        setProductsList(upfechadProductsList)
        console.log("Generating package ticket...")
    }


    return (
        <>
            <div className="flex justify-center items-center flex-col mt-40">
                <div className='p-[10px]'>
                    <label htmlFor="product">Product:</label>
                    <input type="text" id="product" value={product} onChange={handleProductChange} style={{ border: '1px solid black', padding: '5px' }} />
                    {productError && <p style={{ color: 'red' }}>Product is required</p>}
                </div>
                <div className='p-[10px]'>
                    <label htmlFor="cantidad">Cantidad:</label>
                    <input type="number" id="cantidad" value={cantidad} onChange={handleCantidadChange} style={{ border: '1px solid black', padding: '5px' }} />
                    {cantidadError && <p style={{ color: 'red' }}>Cantidad is required</p>}
                </div>
                <button onClick={handleSave}>Save</button>

            </div>
            <div className='flex items-center'>
                <div className='flex flex-col' style={{ alignItems: 'flex-start' }}>
                    {productsList.map((item, index) => (
                        <div key={index}>
                            <div className="border border-black p-2.5 m-2.5 flex">
                                <p>{item.product}</p>
                                <p className="ml-2.5">{item.cantidad}</p>
                            </div>
                            <div className="flex items-center m-2.5">
                                {item.cantidad >= 12 ? (
                                    <button onClick={() => handleGeneratePackageTicket(index)}>Generar ticket para paquete</button>
                                ) : (
                                    <button onClick={() => handleGenerateTicket(index)}>Generar ticket</button>
                                )}
                            </div>
                            <div className="flex flex-col items-start">
                                {item.tickets.map((ticket, ticketIndex) => (
                                    <div key={ticketIndex} className="border border-black p-2.5 m-2.5">
                                        <p>Product: {item.product}</p>
                                        <p>Cantidad: {item.cantidad}</p>
                                        <p>Fecha: {ticket.date.toLocaleString()}</p>
                                    </div>
                                ))}
                            </div>
                        </div>
                    ))}
                </div>
            </div>
        </>
    )
}