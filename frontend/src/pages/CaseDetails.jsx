// src/pages/onboarding/CaseDetails.jsx
import React, { useEffect, useState, useContext } from "react";
import client from "../../api/client";
import { AuthContext } from "../../context/AuthContext";

const CaseDetails = ({ caseId }) => {
  const { user } = useContext(AuthContext); // logged-in user
  const [caseData, setCaseData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  // Fetch case details
  const fetchCase = async () => {
    try {
      const res = await client.get(`/onboarding/${caseId}`);
      setCaseData(res.data);
      setLoading(false);
    } catch (err) {
      console.error(err);
      setError("Failed to fetch case details.");
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchCase();
  }, [caseId]);

  // Handle MAKER submit
  const handleSubmit = async () => {
    if (user.role !== "MAKER") {
      alert("Only MAKER can submit this case.");
      return;
    }
    try {
      await client.post("/workflow/submit", { case_id: caseId, username: user.user_id });
      alert("Case submitted successfully!");
      fetchCase(); // refresh case data
    } catch (err) {
      console.error(err);
      alert("Failed to submit case.");
    }
  };

  // Handle CHECKER approve/reject
  const handleApproveReject = async (action) => {
    if (user.role !== "CHECKER") {
      alert("Only CHECKER can approve or reject.");
      return;
    }
    try {
      const endpoint = action === "approve" ? "/workflow/approve" : "/workflow/reject";
      await client.post(endpoint, { case_id: caseId, username: user.user_id });
      alert(`Case ${action}d successfully!`);
      fetchCase(); // refresh case data
    } catch (err) {
      console.error(err);
      alert(`Failed to ${action} case.`);
    }
  };

  if (loading) return <p>Loading case details...</p>;
  if (error) return <p>{error}</p>;
  if (!caseData) return <p>No case found.</p>;

  return (
    <div>
      <h2>Case Details: {caseId}</h2>
      <p><strong>Name:</strong> {caseData.name}</p>
      <p><strong>DOB:</strong> {caseData.dob}</p>
      <p><strong>Address:</strong> {caseData.address}</p>
      <p><strong>Status:</strong> {caseData.status}</p>
      <p><strong>Maker:</strong> {caseData.maker}</p>
      <p><strong>Checker:</strong> {caseData.checker || "Not assigned"}</p>

      <h3>Documents</h3>
      {caseData.documents && caseData.documents.length > 0 ? (
        <ul>
          {caseData.documents.map((doc, idx) => (
            <li key={idx}>
              <a href={doc.url} target="_blank" rel="noopener noreferrer">
                {doc.doc_type}: {doc.filename}
              </a>
            </li>
          ))}
        </ul>
      ) : (
        <p>No documents uploaded yet.</p>
      )}

      {/* Actions based on RBAC */}
      {user.role === "MAKER" && caseData.status === "DRAFT" && (
        <button onClick={handleSubmit}>Submit Case</button>
      )}

      {user.role === "CHECKER" && caseData.status === "SUBMITTED" && (
        <div>
          <button onClick={() => handleApproveReject("approve")}>Approve Case</button>
          <button onClick={() => handleApproveReject("reject")}>Reject Case</button>
        </div>
      )}
    </div>
  );
};

export default CaseDetails;


