from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

from routes import dashboard, students, attendance, recognition, system
from config import FRONTEND_URL

app = FastAPI(title="Smart Attendance System API")

# Configure CORS
origins = [
    FRONTEND_URL,
    "http://localhost:5173", # Default Vite port
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(dashboard.router, prefix="/api/dashboard", tags=["Dashboard"])
app.include_router(students.router, prefix="/api/students", tags=["Students"])
app.include_router(attendance.router, prefix="/api/attendance", tags=["Attendance"])
app.include_router(recognition.router, prefix="/api/recognition", tags=["Recognition"])
app.include_router(system.router, prefix="/api/system", tags=["System"])

@app.get("/")
def read_root():
    return {"status": "ok", "message": "Smart Attendance API is running"}

@app.get("/api/health")
def health_check():
    return {"status": "healthy"}
