import React, { useState } from "react";
import client from "../../api/client";

const UploadDocument = ({ caseId }) => {
  const [file, setFile] = useState(null);
  const [docType, setDocType] = useState("PAN");

  const handleUpload = async (e) => {
    e.preventDefault();
    if (!file) {
      alert("Please select a file");
      return;
    }
    const formData = new FormData();
    formData.append("file", file);
    formData.append("doc_type", docType);

    try {
      const res = await client.post(`/onboarding/${caseId}/documents`, formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      alert("Document uploaded: " + res.data.file_path);
    } catch (err) {
      console.error(err);
      alert("Error uploading document");
    }
  };

  return (
    <form onSubmit={handleUpload}>
      <h2>Upload Document for Case: {caseId}</h2>
      <select value={docType} onChange={(e) => setDocType(e.target.value)}>
        <option value="PAN">PAN</option>
        <option value="Aadhaar">Aadhaar</option>
        <option value="Passport">Passport</option>
      </select>
      <input type="file" onChange={(e) => setFile(e.target.files[0])} required />
      <button type="submit">Upload</button>
    </form>
  );
};

export default UploadDocument;
