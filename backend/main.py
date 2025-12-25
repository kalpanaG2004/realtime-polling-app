from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import register_routes

app = FastAPI(title="Real-Time Polling App")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

register_routes(app)