from fastapi import APIRouter, UploadFile, File, HTTPException
from services.face_recognition_service import face_service
from services.attendance_service import mark_attendance

router = APIRouter()

@router.post("/")
async def recognize_and_mark(image: UploadFile = File(...)):
    """
    Receives an image from the webcam, processes it to find a face,
    and marks attendance if the student is recognized.
    """
    if not image:
        raise HTTPException(status_code=400, detail="No image provided")

    try:
        contents = await image.read()
        
        # 1. Recognize face
        recognition_result = face_service.recognize_face(contents)
        
        if recognition_result.get("status") != "success":
            return recognition_result # Returns error or unknown face message
            
        student_name = recognition_result.get("student_name")
        
        # 2. Mark attendance
        attendance_result = mark_attendance(student_name)
        
        # 3. Combine results
        return {
            "status": "success",
            "student_name": student_name,
            "confidence": recognition_result.get("confidence"),
            "message": attendance_result.get("message"),
            "attendance_status": attendance_result.get("status") # 'success' or 'duplicate'
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
