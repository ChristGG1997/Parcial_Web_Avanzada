"use client";
import React, { createContext, useState, useContext } from "react";

interface UserProp {
  id: string | null;
  name: string | null;
  email: string | null;
  role: string | null;
}

interface UserContextProp {
  user: UserProp;
  updateUser: ({ id, name, role }: UserProp) => void;
}

const UserContext = createContext<UserContextProp>({
  user: { id: null, name: null, role: null, email: null },
  updateUser: () => {},
});

export const UserProvider = ({ children }: { children: React.ReactNode }) => {
  const [user, setUser] = useState<UserProp>({
    id: null,
    name: null,
    role: null,
    email: null,
  });

  const updateUser = ({ id, name, role, email }: UserProp) => {
    setUser({ id, name, role, email });
  };

  return (
    <UserContext.Provider value={{ user, updateUser }}>
      {children}
    </UserContext.Provider>
  );
};

export const useUser = () => useContext(UserContext);
