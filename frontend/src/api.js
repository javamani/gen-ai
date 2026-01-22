import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000"
});

export const uploadKyc = (file) => {
  const formData = new FormData();
  formData.append("file", file);

  return API.post("/pipeline/kyc-process", formData, {
    headers: {
      "Content-Type": "multipart/form-data"
    }
  });
};
