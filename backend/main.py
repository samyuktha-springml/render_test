from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend (Vercel) to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later restrict to your Vercel URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Sample procurement logic
purchase_history = [
    {"item": "Wooden Chair", "vendor": "ABC", "qty": 10, "price": 1200},
    {"item": "Wooden Chair", "vendor": "XYZ", "qty": 50, "price": 1000},
    {"item": "Wooden Chair", "vendor": "ABC", "qty": 100, "price": 900},
]

@app.get("/")
def home():
    return {"message": "Backend running"}

@app.get("/best-vendor")
def best_vendor(item: str, required_qty: int):
    vendors = {}

    for record in purchase_history:
        if record["item"] != item:
            continue

        # consider similar qty range (±30%)
        if abs(record["qty"] - required_qty) <= required_qty * 0.3:
            vendor = record["vendor"]
            vendors.setdefault(vendor, []).append(record["price"])

    if not vendors:
        return {"message": "No data available"}

    avg_prices = {
        v: sum(p)/len(p) for v, p in vendors.items()
    }

    best = min(avg_prices, key=avg_prices.get)

    return {
        "best_vendor": best,
        "avg_prices": avg_prices
    }