import React, { useContext, useState } from "react";
import { AuthContext } from "../../context/AuthContext";
import client from "../../api/client";

const CaseActions = ({ caseId, reloadCase }) => {
  const { user } = useContext(AuthContext);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  if (!user) return null;

  const handleAction = async (action) => {
    setLoading(true);
    setError("");
    try {
      await client.post(`/workflow/${action}`, { case_id: caseId });
      reloadCase();
    } catch (err) {
      console.error(err);
      setError("Action failed. Check your role or server.");
    } finally {
      setLoading(false);
    }
  };

  if (user.role !== "CHECKER") return null;

  return (
    <div>
      {error && <p style={{ color: "red" }}>{error}</p>}
      <button disabled={loading} onClick={() => handleAction("approve")}>Approve</button>
      <button disabled={loading} onClick={() => handleAction("reject")}>Reject</button>
    </div>
  );
};

export default CaseActions;
