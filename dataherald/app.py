import dataherald
import dataherald.config
from dataherald.server.fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

settings = dataherald.config.Settings()
server = FastAPI(settings)
app = server.app()

origins = [
    "http://localhost:3000",
    "http://localhost:3001",
    "https://airpipe.onrender.com",
    "https://api-airpipe.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)