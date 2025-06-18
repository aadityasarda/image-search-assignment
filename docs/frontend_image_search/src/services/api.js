import axios from "axios";

const API_BASE_URL = "http://localhost:8000/api";

export const searchSimilarImages = async (file) => {
  const formData = new FormData();
  formData.append("file", file);

  const response = await axios.post(`${API_BASE_URL}/search`, formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });

  return response.data;
};
