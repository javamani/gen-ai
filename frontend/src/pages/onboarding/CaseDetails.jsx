import React, { useEffect, useState, useContext } from "react";
import client from "../../api/client";
import CaseActions from "./CaseActions";
import UploadDocument from "./UploadDocument";
import { AuthContext } from "../../context/AuthContext";

const STATUS_STEPS = ["DRAFT", "SUBMITTED", "APPROVED", "REJECTED"];

const CaseDetails = ({ caseId }) => {
  const { user } = useContext(AuthContext);
  const [caseData, setCaseData] = useState(null);
  const [loading, setLoading] = useState(true);

  const loadCase = async () => {
    setLoading(true);
    try {
      const res = await client.get(`/onboarding/${caseId}`);
      setCaseData(res.data);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadCase();
  }, [caseId]);

  if (loading) return <p>Loading case...</p>;
  if (!caseData) return <p>Case not found</p>;

  const auditMap = {};
  caseData.audit?.forEach((entry) => {
    auditMap[entry.action] = { by: entry.by, time: entry.time };
  });

  const renderWorkflow = () => (
    <div style={{ display: "flex", alignItems: "center", gap: "10px", marginBottom: "20px" }}>
      {STATUS_STEPS.map((step, idx) => {
        const entry = auditMap[step];
        const isActive = step === caseData.status;
        const isCompleted = entry && step !== "REJECTED";

        const style = {
          padding: "10px 20px",
          borderRadius: "5px",
          backgroundColor: isActive
            ? "#4CAF50"
            : isCompleted
            ? "#A5D6A7"
            : "#E0E0E0",
          color: "#fff",
          fontWeight: isActive ? "bold" : "normal",
          position: "relative",
          cursor: entry ? "pointer" : "default"
        };

        return (
          <React.Fragment key={step}>
            <div
              style={style}
              title={entry ? `By: ${entry.by}\nAt: ${new Date(entry.time).toLocaleString()}` : ""}
            >
              {step}
            </div>
            {idx < STATUS_STEPS.length - 1 && (
              <div
                style={{
                  width: "30px",
                  height: "4px",
                  backgroundColor: isCompleted ? "#A5D6A7" : "#ccc",
                  margin: "0 5px"
                }}
              />
            )}
          </React.Fragment>
        );
      })}
    </div>
  );

  return (
    <div>
      <h2>Case ID: {caseData.case_id}</h2>
      <p>Customer Name: {caseData.name}</p>
      <p>Status: {caseData.status}</p>

      {renderWorkflow()}

      {/* MAKER actions */}
      {user?.role === "MAKER" && caseData.status === "DRAFT" && (
        <div>
          <h3>Upload Documents</h3>
          <UploadDocument caseId={caseId} />
          <button
            onClick={async () => {
              try {
                await client.post("/workflow/submit", { case_id: caseId });
                alert("Case submitted!");
                loadCase();
              } catch (err) {
                console.error(err);
                alert("Failed to submit");
              }
            }}
          >
            Submit Case
          </button>
        </div>
      )}

      {/* CHECKER actions */}
      <CaseActions caseId={caseId} reloadCase={loadCase} />
    </div>
  );
};

export default CaseDetails;

