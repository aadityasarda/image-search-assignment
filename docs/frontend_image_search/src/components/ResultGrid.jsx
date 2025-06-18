import { useState } from "react";
import "./ResultGrid.css";

const ITEMS_PER_PAGE = 10;

const ResultGrid = ({ results }) => {
  const [currentPage, setCurrentPage] = useState(1);

  const startIdx = (currentPage - 1) * ITEMS_PER_PAGE;
  const paginatedResults = results.slice(startIdx, startIdx + ITEMS_PER_PAGE);

  const totalPages = Math.ceil(results.length / ITEMS_PER_PAGE);

  return (
    <div className="results-wrapper">
      <h2>Top Matches</h2>

      <div className="result-grid">
        {paginatedResults.map((item, idx) => (
          <div className="result-card" key={idx}>
            <img src={`http://localhost:8000/${item.url}`} alt={`img-${idx}`} />
            <div className="label">{item.label}</div>
            <div className="score">Score: {item.score}</div>
          </div>
        ))}
      </div>

      <div className="pagination">
        {[...Array(totalPages)].map((_, i) => (
          <button
            key={i}
            className={currentPage === i + 1 ? "active" : ""}
            onClick={() => setCurrentPage(i + 1)}
          >
            {i + 1}
          </button>
        ))}
      </div>
    </div>
  );
};

export default ResultGrid;
