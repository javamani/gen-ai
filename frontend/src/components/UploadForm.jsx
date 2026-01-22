import { useState } from "react";
import { uploadKyc } from "../api";

export default function UploadForm({ setResult }) {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    if (!file) return alert("Select a file");

    try {
      setLoading(true);
      const res = await uploadKyc(file);
      setResult(res.data);
    } catch (err) {
      alert("Upload failed");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ marginBottom: "20px" }}>
      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <br /><br />
      <button onClick={handleSubmit}>
        {loading ? "Processing..." : "Upload KYC"}
      </button>
    </div>
  );
}
