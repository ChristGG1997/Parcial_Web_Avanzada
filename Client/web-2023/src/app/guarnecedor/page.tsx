"use client"
import { SetStateAction, useState } from "react"

interface Product {
    product: string
    quantity: number
    tickets: Ticket[]
}


interface Ticket extends Product {
    date: Date
}



export default function GuarnecedorSection() {
    const [product, setProduct] = useState("")
    const [quantity, setQuantity] = useState<number>(0)
    const [productsList, setProductsList] = useState<Product[]>([])
    const [productError, setProductError] = useState(false)
    const [quantityError, setQuantityError] = useState(false)
    const [tickets, setTickets] = useState<Ticket[]>([])

    const handleProductChange = (event: { target: { value: SetStateAction<string> } }) => {
        setProduct(event.target.value)
        setProductError(false)
    }

    const handleQuantityChange = (event: { target: { value: SetStateAction<string> } }) => {
        setQuantity(Number(event.target.value))
        setQuantityError(false)
    }

    const handleSave = () => {
        if (product === "") {
            setProductError(true)
            return
        }
        if (quantity === 0) {
            setQuantityError(true)
            return
        }
        const existingProductIndex = productsList.findIndex(item => item.product.toLowerCase() === product.toLowerCase())
        if (existingProductIndex !== -1) {
            const updatedProductsList = [...productsList]
            updatedProductsList[existingProductIndex].quantity += quantity
            setProductsList(updatedProductsList)
        } else {
            setProductsList([...productsList, { product, quantity, tickets: [] }])
        }
        setProduct("")
        setQuantity(0)
    }

    const handleGenerateTicket = (index: number) => {
        const item = productsList[index]
        const ticket: Ticket = {
            date: new Date(),
            product: "",
            quantity: 0,
            tickets: []
        }
        const updatedProductsList = [...productsList]
        updatedProductsList[index].tickets.push(ticket)
        setProductsList(updatedProductsList)
        console.log("Generating ticket...")
    }

    const handleGeneratePackageTicket = (index: number) => {
        const item = productsList[index]
        const ticket: Ticket = {
            date: new Date(),
            product: "",
            quantity: 0,
            tickets: []
        }
        const updatedProductsList = [...productsList]
        updatedProductsList[index].tickets.push(ticket)
        setProductsList(updatedProductsList)
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
                    <label htmlFor="quantity">Quantity:</label>
                    <input type="number" id="quantity" value={quantity} onChange={handleQuantityChange} style={{ border: '1px solid black', padding: '5px' }} />
                    {quantityError && <p style={{ color: 'red' }}>Quantity is required</p>}
                </div>
                <button onClick={handleSave}>Save</button>

            </div>
            <div className='flex items-center'>
                <div className='flex flex-col' style={{ alignItems: 'flex-start' }}>
                    {productsList.map((item, index) => (
                        <div key={index}>
                            <div className="border border-black p-2.5 m-2.5 flex">
                                <p>{item.product}</p>
                                <p className="ml-2.5">{item.quantity}</p>
                            </div>
                            <div className="flex items-center m-2.5">
                                {item.quantity >= 12 ? (
                                    <button onClick={() => handleGeneratePackageTicket(index)}>Generar ticket para paquete</button>
                                ) : (
                                    <button onClick={() => handleGenerateTicket(index)}>Generar ticket</button>
                                )}
                            </div>
                            <div className="flex flex-col items-start">
                                {item.tickets.map((ticket, ticketIndex) => (
                                    <div key={ticketIndex} className="border border-black p-2.5 m-2.5">
                                        <p>Product: {item.product}</p>
                                        <p>Quantity: {item.quantity}</p>
                                        <p>Date: {ticket.date.toLocaleString()}</p>
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