// frontend/src/pages/CheckerDashboard.jsx
import React, { useEffect, useState, useContext } from "react";
import client from "../api/client";
import { AuthContext } from "../context/AuthContext";

const CheckerDashboard = () => {
  const { user } = useContext(AuthContext);
  const [cases, setCases] = useState([]);
  const [loading, setLoading] = useState(true);

  // Fetch submitted cases
  const fetchCases = async () => {
    try {
      const res = await client.get("/workflow/cases", {
        headers: {
          Authorization: "Bearer checker-token", // dummy token for CHECKER
        },
      });

      // Backend might return { cases: [...] }
      const casesArray = Array.isArray(res.data)
        ? res.data
        : res.data.cases || [];

      setCases(casesArray);
    } catch (err) {
      console.error("Error fetching cases", err);
      setCases([]);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    if (!user) return;
    fetchCases();
  }, [user]);

  if (!user) return <p>Loading user info...</p>;

  if (user.role !== "CHECKER") {
    return <p>You do not have permission to view this page.</p>;
  }

  const handleApprove = async (caseId) => {
    try {
      await client.post(
        "/workflow/approve",
        { case_id: caseId },
        { headers: { Authorization: "Bearer checker-token" } }
      );
      alert("Case approved!");
      fetchCases(); // refresh list
    } catch (err) {
      console.error(err);
      alert("Failed to approve case. Check backend or role.");
    }
  };

  const handleReject = async (caseId) => {
    try {
      await client.post(
        "/workflow/reject",
        { case_id: caseId },
        { headers: { Authorization: "Bearer checker-token" } }
      );
      alert("Case rejected!");
      fetchCases(); // refresh list
    } catch (err) {
      console.error(err);
      alert("Failed to reject case. Check backend or role.");
    }
  };

  if (loading) return <p>Loading submitted cases...</p>;

  if (cases.length === 0) return <p>No submitted cases to review.</p>;

  return (
    <div>
      <h2>Checker Dashboard</h2>
      {cases.map((c) => (
        <div
          key={c.case_id}
          style={{ border: "1px solid gray", margin: 10, padding: 10 }}
        >
          <p><b>Case ID:</b> {c.case_id}</p>
          <p><b>Status:</b> {c.status}</p>
          <p><b>Maker:</b> {c.maker}</p>
          <p><b>Audit:</b> {c.audit?.map((a, idx) => (
            <span key={idx}>
              {a.action} by {a.by} at {new Date(a.time).toLocaleString()}<br />
            </span>
          ))}</p>

          {c.status === "SUBMITTED" && (
            <>
              <button onClick={() => handleApprove(c.case_id)}>Approve</button>
              <button onClick={() => handleReject(c.case_id)}>Reject</button>
            </>
          )}
        </div>
      ))}
    </div>
  );
};

export default CheckerDashboard;
