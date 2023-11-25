"use client";
import { useState, useEffect } from "react";
import { useGetUser } from "../services/app.services";
import Link from "next/link";
import { useUser } from "@/data/context/userContext";

const Login = () => {
  const { users } = useGetUser();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [user, setUser] = useState<{ role: string } | null>(null);
  const [errorMessage, setErrorMessage] = useState("");

  const { updateUser } = useUser();

  useEffect(() => {
    if (users) {
      const foundUser = users.find(
        (u: { email: string }) => u.email === username
      );
      setUser(foundUser);
      updateUser({
        id: foundUser?.id,
        name: foundUser?.name,
        role: foundUser?.role,
        email: foundUser?.email,
      });
    }
  }, [users, username]);

  const handleSubmit = async (e: { preventDefault: () => void }) => {
    e.preventDefault();

    if (!username || !password) {
      setErrorMessage("Ambos campos son obligatorios");
      return;
    }
  };

  let linkDestination = "/guarnecedor";
  if (user && user.role === "admin") {
    linkDestination = "/admin";
  }

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100">
      <div className="max-w-md w-full px-6 py-12 bg-white shadow-md rounded-md">
        <h2 className="text-2xl font-bold text-gray-800 mb-6">
          Iniciar sesión
        </h2>
        <form className="space-y-6" onSubmit={handleSubmit}>
          {errorMessage && (
            <div className="text-red-500 text-center">{errorMessage}</div>
          )}
          <div>
            <label
              htmlFor="username"
              className="block text-gray-800 font-medium mb-2"
            >
              Nombre de usuario
            </label>
            <input
              type="text"
              id="username"
              name="username"
              className="w-full border-gray-300 rounded-md shadow-sm focus:border-indigo-500 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
              onChange={(e) => setUsername(e.target.value)}
            />
          </div>
          <div>
            <label
              htmlFor="password"
              className="block text-gray-800 font-medium mb-2"
            >
              Contraseña
            </label>
            <input
              type="password"
              id="password"
              name="password"
              className="w-full border-gray-300 rounded-md shadow-sm focus:border-indigo-500 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
              onChange={(e) => setPassword(e.target.value)}
            />
          </div>
          <div className="flex justify-center">
            <Link
              href={linkDestination}
              className={`w-full bg-indigo-500 text-white py-2 px-4 rounded-md hover:bg-indigo-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 text-center ${
                errorMessage ? "disabled" : ""
              }`}
            >
              Iniciar sesión
            </Link>
          </div>
        </form>
      </div>
    </div>
  );
};

export default Login;
