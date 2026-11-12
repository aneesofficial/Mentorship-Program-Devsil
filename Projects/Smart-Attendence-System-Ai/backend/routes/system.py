from fastapi import APIRouter
import os
from config import MODEL_PATH, ATTENDANCE_FILE
from services.face_recognition_service import face_service

router = APIRouter()

@router.get("/status")
def system_status():
    """Returns the status of backend, models, and data files."""
    
    model_exists = os.path.exists(MODEL_PATH)
    attendance_exists = os.path.exists(ATTENDANCE_FILE)
    
    return {
        "status": "success",
        "data": {
            "backend": "Online",
            "model_file_found": model_exists,
            "model_path": MODEL_PATH,
            "model_loaded_in_memory": face_service.is_model_loaded,
            "attendance_file_found": attendance_exists,
            "attendance_path": ATTENDANCE_FILE
        }
    }
