import { useState } from "react";
import Header from "../components/Header";
import AnimatedSearchBox from "../components/SearchBar";
// import ResultGrid from "../components/ResultGrid"; //this is for pagination
import Loader from "../components/Loader";
import { searchSimilarImages } from "../services/api";

const Home = () => {
  const [showResults, setShowResults] = useState(false);
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleSearch = async (file) => {
    setShowResults(true);
    setLoading(true);

    try {
      const data = await searchSimilarImages(file);
      setResults(data); // Store full JSON
    } catch (err) {
      console.error("Search failed:", err);
      alert("Something went wrong during search.");
    }

    setLoading(false);
  };

  const handleBack = () => {
    setResults([]);
    setShowResults(false);
    setLoading(false);
  };

  return (
    <div style={{ padding: "40px" }}>
        <Header />
      {!showResults ? (
        <AnimatedSearchBox onSearch={handleSearch} />
      ) : loading ? (
        <Loader />
      ) : (
        <>
          <button
            onClick={handleBack}
            style={{
              marginBottom: "20px",
              background: "#3498db",
              color: "#fff",
              border: "none",
              padding: "10px 18px",
              borderRadius: "6px",
              cursor: "pointer",
            }}
          >
            ⬅ Back to Search
          </button>
          <h2>Raw JSON Output</h2>
          <pre
            style={{
              background: "#f4f4f4",
              padding: "20px",
              borderRadius: "10px",
              overflowX: "auto",
            }}
          >
            {JSON.stringify(results, null, 2)}   
          </pre>                                 
        </>
      )}
    </div>
  );
};

export default Home;
