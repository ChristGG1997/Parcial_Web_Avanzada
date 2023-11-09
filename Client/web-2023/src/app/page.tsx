import Link from 'next/link'
import React from 'react'

const Login = () => {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100">
      <div className="max-w-md w-full px-6 py-12 bg-white shadow-md rounded-md">
        <h2 className="text-2xl font-bold text-gray-800 mb-6">Iniciar sesión</h2>
        <form className="space-y-6">
          <div>
            <label htmlFor="username" className="block text-gray-800 font-medium mb-2">Nombre de usuario</label>
            <input type="text" id="username" name="username" className="w-full border-gray-300 rounded-md shadow-sm focus:border-indigo-500 focus:ring focus:ring-indigo-200 focus:ring-opacity-50" />
          </div>
          <div>
            <label htmlFor="password" className="block text-gray-800 font-medium mb-2">Contraseña</label>
            <input type="password" id="password" name="password" className="w-full border-gray-300 rounded-md shadow-sm focus:border-indigo-500 focus:ring focus:ring-indigo-200 focus:ring-opacity-50" />
          </div>
          <div>
            <Link href="/guarnecedor">
            <button type="submit" className="w-full bg-indigo-500 text-white py-2 px-4 rounded-md hover:bg-indigo-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">Iniciar sesión</button>
            </Link>
          </div>
        </form>
        <div className="mt-6">
          <a href="#" className="text-indigo-500 hover:text-indigo-600 font-medium">¿Olvidaste tu contraseña?</a>
        </div>
        <div className="mt-1">
          <a href="#" className="text-indigo-500 hover:text-indigo-600 font-medium">¿No tienes una cuenta? Regístrate</a>
        </div>
      </div>
    </div>
  )
}

export default Login
