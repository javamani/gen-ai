import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import CreateCase from "../pages/onboarding/CreateCase";

const AppRoutes = () => {
  return (
    <Router>
      <Routes>
        <Route path="/onboarding" element={<CreateCase />} />
        <Route path="*" element={<CreateCase />} /> {/* default route */}
      </Routes>
    </Router>
  );
};

export default AppRoutes;
