import { useState } from "react";

function App() {
  const [item, setItem] = useState("Wooden Chair");
  const [qty, setQty] = useState(50);
  const [result, setResult] = useState(null);

  const fetchBestVendor = async () => {
    const res = await fetch(
      `https://render-test-48g0.onrender.com/best-vendor?item=${item}&required_qty=${qty}`
    );
    const data = await res.json();
    setResult(data);
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>Procurement Tool</h2>

      <input
        value={item}
        onChange={(e) => setItem(e.target.value)}
        placeholder="Item"
      />

      <input
        type="number"
        value={qty}
        onChange={(e) => setQty(e.target.value)}
        placeholder="Quantity"
      />

      <button onClick={fetchBestVendor}>
        Get Best Vendor
      </button>

      {result && (
        <div>
          <h3>Best Vendor: {result.best_vendor}</h3>
          <pre>{JSON.stringify(result.avg_prices, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default App;