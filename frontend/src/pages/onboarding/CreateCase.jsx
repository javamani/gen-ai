import React, { useState } from "react";
import client from "../../api/client";
import UploadDocument from "./UploadDocument";

const CreateCase = () => {
  const [name, setName] = useState("");
  const [dob, setDob] = useState("");
  const [address, setAddress] = useState("");
  const [makerId, setMakerId] = useState("");
  const [caseId, setCaseId] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const payload = { name, dob, address, maker_id: makerId };
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
            placeholder="Maker ID"
            value={makerId}
            onChange={(e) => setMakerId(e.target.value)}
            required
          />
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
        <UploadDocument caseId={caseId} />
      )}
    </div>
  );
};

export default CreateCase;
