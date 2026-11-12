import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Base directories
BASE_DIR = Path(__file__).resolve().parent.parent
BACKEND_DIR = BASE_DIR / "backend"

# Configurable paths (can be overridden via .env)
MODEL_PATH = os.getenv("MODEL_PATH", str(BASE_DIR / "models" / "encodings.pkl"))
ATTENDANCE_FILE = os.getenv("ATTENDANCE_FILE", str(BASE_DIR / "data" / "attendance.csv"))
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:5173")

# Ensure directories exist
os.makedirs(os.path.dirname(ATTENDANCE_FILE), exist_ok=True)
os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
