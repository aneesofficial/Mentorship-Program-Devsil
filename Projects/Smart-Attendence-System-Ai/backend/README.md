# Backend Service

This FastAPI backend serves as the bridge between the React frontend, the AI Face Recognition Model, and the CSV Attendance Data.

## Running the Server

```bash
uvicorn main:app --reload --port 8000
```

## Structure
- `main.py`: Entry point and CORS configuration.
- `config.py`: Environment variables and path resolution.
- `routes/`: API endpoint definitions.
- `services/`: Business logic.
    - `attendance_service.py`: CSV reading/writing.
    - `face_recognition_service.py`: Model loading and cv2 inference.
