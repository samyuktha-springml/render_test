from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import recommendation

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://your-frontend.vercel.app"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(recommendation.router)