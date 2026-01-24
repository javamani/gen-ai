import React, { useState, useContext } from "react";
import client from "../../api/client";
import UploadDocument from "./UploadDocument";
import { AuthContext } from "../../context/AuthContext";

const CreateCase = () => {
  const { user } = useContext(AuthContext); // logged-in user
  const [name, setName] = useState("");
  const [dob, setDob] = useState("");
  const [address, setAddress] = useState("");
  const [caseId, setCaseId] = useState(null);

  if (!user) return <p>Loading user info...</p>;

  // Only MAKER can create a case
  if (user.role !== "MAKER") {
    return <p>You do not have permission to create a case.</p>;
  }

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const payload = { 
        name, 
        dob, 
        address 
        // makerId is taken from logged-in user on backend
      };

      const res = await client.post("/onboarding/create", payload);
      alert("Case created: " + res.data.case_id);
      setCaseId(res.data.case_id); // proceed to upload documents
    } catch (err) {
      console.error(err);
      alert("Error creating case");
    }
  };

  return (
    <div>
      {!caseId ? (
        <form onSubmit={handleSubmit}>
          <h2>Create Customer Case</h2>

          <input
            type="text"
            placeholder="Customer Name"
            value={name}
            onChange={(e) => setName(e.target.value)}
            required
          />

          <input
            type="date"
            placeholder="Date of Birth"
            value={dob}
            onChange={(e) => setDob(e.target.value)}
            required
          />

          <input
            type="text"
            placeholder="Address"
            value={address}
            onChange={(e) => setAddress(e.target.value)}
            required
          />

          <button type="submit">Create Case</button>
        </form>
      ) : (
        <div>
          <h3>Upload Documents for Case {caseId}</h3>
          <UploadDocument caseId={caseId} />

          <p>Once all documents are uploaded, submit the case:</p>
          <button
            onClick={async () => {
              try {
                await client.post("/workflow/submit", { 
  case_id: caseId, 
  username: user.username   // 👈 VERY IMPORTANT
});
                alert("Case submitted successfully!");
              } catch (err) {
                console.error(err);
                alert("Failed to submit case. Check your role or server.");
              }
            }}
          >
            Submit Case
          </button>
        </div>
      )}
    </div>
  );
};

export default CreateCase;
