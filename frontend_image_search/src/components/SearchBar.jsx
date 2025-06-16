import { useState } from "react";
import "./SearchBar.css";

const AnimatedSearchBox = ({ onSearch }) => {
  const [file, setFile] = useState(null);
  

  const handleFileChange = (e) => {
    const selected = e.target.files[0];
    if (selected) {
      setFile(selected);
    }
  };

  const handleSearchClick = () => {
    if (file) {
      onSearch(file);
    } else {
      alert("Please upload an image first.");
    }
  };

  return (
    <div className="search-container">
      <div className="search-box">
        <label htmlFor="file-upload" className="upload-icon">📁</label>
        <input
          id="file-upload"
          type="file"
          accept="image/*"
          onChange={handleFileChange}
          hidden
        />

        {!file ? (
            <span className="animated-placeholder">Upload an image & Search Similar Images</span>
        ) : (
            <span className="file-name">{file.name}</span>
        )}


        

        <button className="search-btn" onClick={handleSearchClick}>🔍</button>
      </div>
    </div>
  );
};

export default AnimatedSearchBox;
