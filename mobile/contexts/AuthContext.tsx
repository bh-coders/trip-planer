// authContext.tsx
import React, { createContext, useState, useContext, useEffect, ReactNode } from 'react';
import { getToken } from '../components/utils/tokenUtils';

interface AuthContextType {
  userToken: string | null | undefined;
  setUserToken: (token: string | null) => void;
}
interface AuthProviderProps {
  children: ReactNode;
}
///Context
export const AuthContext = createContext<AuthContextType>({
  userToken: null,
  setUserToken: (token) => {},
});

interface AuthProviderProps {
  children: ReactNode;
}

///Provider
export const AuthProvider: React.FC<AuthProviderProps> = ({ children }) => {
  const [userToken, setUserToken] = useState<string | null | undefined>(null);

  useEffect(() => {
    const fetchToken = async () => {
      const token = await getToken();
      setUserToken(token);
    };

    fetchToken();
  }, []);

  return (
    <AuthContext.Provider value={{ userToken, setUserToken }}>{children}</AuthContext.Provider>
  );
};
