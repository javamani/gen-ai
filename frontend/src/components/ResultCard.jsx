export default function ResultCard({ result }) {
  if (!result) return null;

  return (
    <div style={{
      border: "1px solid #ccc",
      padding: "20px",
      borderRadius: "8px",
      marginTop: "20px"
    }}>
      <h3>KYC Result</h3>

      <p><b>Filename:</b> {result.filename}</p>
      <p><b>Document Type:</b> {result.entities.document_type}</p>

      {Object.entries(result.entities).map(([key, value]) => (
        value && key !== "document_type" && (
          <p key={key}><b>{key}:</b> {value}</p>
        )
      ))}
    </div>
  );
}
