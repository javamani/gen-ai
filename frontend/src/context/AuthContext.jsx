import React, { createContext, useState, useEffect } from "react";

export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);

  // Auto login for dev (remove later when real login added)
  useEffect(() => {
    const savedUser = {
      user_id: "checker001",
      username: "checker001",
      role: "CHECKER", // CHANGE TO "CHECKER" TO TEST CHECKER DASHBOARD
      token: "checker-token"   // 👈 required for backend auth
    };

    localStorage.setItem("token", savedUser.token);
    setUser(savedUser);
  }, []);

  const login = (userData) => {
    localStorage.setItem("token", userData.token);
    setUser(userData);
  };

  const logout = () => {
    localStorage.removeItem("token");
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};
