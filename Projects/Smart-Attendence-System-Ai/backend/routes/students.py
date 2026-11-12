from fastapi import APIRouter
from services.face_recognition_service import face_service
from services.attendance_service import get_student_attendance

router = APIRouter()

@router.get("/")
def get_students():
    """Returns a list of all registered students from the model."""
    students = face_service.get_registered_students()
    
    # Enrich with attendance percentage if desired, but keeping it simple:
    data = []
    for s in students:
        records = get_student_attendance(s)
        present_days = len(records)
        data.append({
            "name": s,
            "id": f"STD-{abs(hash(s)) % 10000}", # Dummy ID based on name
            "present_days": present_days
        })

    return {"status": "success", "data": data}

@router.get("/{student_id}")
def get_student_details(student_id: str):
    """Return specific student details (Placeholder)."""
    return {"status": "success", "data": {"id": student_id, "details": "To be implemented"}}
