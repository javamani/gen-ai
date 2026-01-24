import React from "react";
import { Routes, Route, Navigate, useParams } from "react-router-dom";
import CreateCase from "../pages/onboarding/CreateCase";
import CaseDetails from "../pages/onboarding/CaseDetails";
import CheckerDashboard from "../pages/CheckerDashboard";

const CaseDetailsWrapper = () => {
  const { caseId } = useParams();
  return <CaseDetails caseId={caseId} />;
};

const AppRoutes = () => (
  <Routes>
    {/* Redirect / to onboarding create page */}
    <Route path="/" element={<Navigate to="/onboarding/create" />} />

    {/* Onboarding routes */}
    <Route path="/onboarding/create" element={<CreateCase />} />
    <Route path="/onboarding/:caseId" element={<CaseDetailsWrapper />} />
      <Route path="/checker" element={<CheckerDashboard />} /> {/* ✅ ADD HERE */}
  </Routes>
);

export default AppRoutes;
