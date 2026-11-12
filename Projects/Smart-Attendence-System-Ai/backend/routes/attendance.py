from fastapi import APIRouter
from services.attendance_service import get_all_attendance, get_today_attendance, get_student_attendance

router = APIRouter()

@router.get("/")
def get_attendance():
    """Returns all attendance records."""
    records = get_all_attendance()
    return {"status": "success", "data": records}

@router.get("/today")
def get_today():
    """Returns today's attendance records."""
    records = get_today_attendance()
    return {"status": "success", "data": records}

@router.get("/student/{student_name}")
def get_student(student_name: str):
    """Returns attendance records for a specific student."""
    records = get_student_attendance(student_name)
    return {"status": "success", "data": records}
