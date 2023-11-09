'use client'
import Link from 'next/link'
import React, { useState } from 'react'
import Avatars from '@/assets/Avatars.png'
import Image from 'next/image'

const Trabajadores = [
    {
        nombre: "Juan",
        rol: "Gerente",
        image: Avatars
    },
    {
        nombre: "Maria",
        rol: "Contadora",
        image: Avatars
    },
    {
        nombre: "Pedro",
        rol: "Programador",
        image: Avatars
    }
]

const Page = () => {
    const [searchTerm, setSearchTerm] = useState("")

    const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        setSearchTerm(event.target.value)
    }

    const filteredTrabajadores = Trabajadores.filter((trabajador) => {
        const nombre = trabajador.nombre.toLowerCase()
        const rol = trabajador.rol.toLowerCase()
        const searchTermLowerCase = searchTerm.toLowerCase()
        return nombre.includes(searchTermLowerCase) || rol.includes(searchTermLowerCase)
    })

    return (
        <div>
            <nav className='w-full flex sm:px-16 justify-start bg-[#ffffff65] backdrop-blur-lg h-[68px] border-b border-white items-center'>
                <ul className="flex justify-between list-none p-0 gap-20">
                    <li><Link href="/trabajadores">Trabajadores</Link></li>
                    <li><Link href="/pago">Pago</Link></li>
                    <li><Link href="/precios">Precios</Link></li>
                </ul>
            </nav>
            <div className='flex justify-center mt-[100px]'>
                <input type="text" placeholder="Buscar" className="w-1/2 p-2.5" value={searchTerm} onChange={handleChange} />
            </div>
            <div className='flex justify-center mt-[50px]'>
                <div className="w-1/2">
                    <div className="w-full flex flex-col">
                        {filteredTrabajadores.map((trabajador, index) => (
                            <div key={index} className="w-full h-40 bg-white rounded shadow-md flex items-center mb-5 gap-3">
                                <Image
                                    src={Avatars}
                                    width={0}
                                    height={0}
                                    alt='avatar'
                                    priority
                                    className="w-12 h-12 rounded-full bg-gray-300 mb-5">

                                </Image>
                                <div className="flex flex-col items-baseline">
                                    <p className="font-bold text-xl mb-0">{trabajador.nombre}</p>
                                    <p className="text-lg mb-2.5">{trabajador.rol}</p>
                                </div>
                            </div>
                        ))}
                    </div>
                </div>
            </div>
        </div >
    )
}

export default Page
