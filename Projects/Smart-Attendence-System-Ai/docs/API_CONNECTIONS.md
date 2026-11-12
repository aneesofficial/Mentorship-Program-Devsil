# API Connections

This document details every major API route in the Smart Attendance System, connecting the frontend to the backend logic.

## 1. System Status
**METHOD**: GET
**URL**: `/api/system/status`
**PURPOSE**: Check if backend, model, and dataset files are online.
- **Frontend**: `frontend/src/pages/Settings.jsx`, `frontend/src/services/api.js`
- **Backend Route**: `backend/routes/system.py`
- **Service File**: Checks variables from `backend/config.py`

## 2. Dashboard Statistics
**METHOD**: GET
**URL**: `/api/dashboard`
**PURPOSE**: Fetch high-level numbers (Total students, present today, etc).
- **Frontend**: `frontend/src/pages/Dashboard.jsx`
- **Backend Route**: `backend/routes/dashboard.py`
- **Service**: `backend/services/attendance_service.py`

## 3. List Students
**METHOD**: GET
**URL**: `/api/students`
**PURPOSE**: Return registered students.
- **Frontend**: `frontend/src/pages/Students.jsx`
- **Backend Route**: `backend/routes/students.py`
- **Service**: `backend/services/face_recognition_service.py` -> `get_registered_students()`

## 4. List Attendance
**METHOD**: GET
**URL**: `/api/attendance`
**PURPOSE**: Get all attendance records.
- **Frontend**: `frontend/src/pages/Attendance.jsx`
- **Backend Route**: `backend/routes/attendance.py`
- **Service**: `backend/services/attendance_service.py` -> `get_all_attendance()`

## 5. Recognize & Mark Attendance
**METHOD**: POST
**URL**: `/api/recognition`
**PURPOSE**: Receive webcam image, identify face, and mark attendance.
- **REQUEST**: `multipart/form-data` containing `image` (Blob).
- **RESPONSE**: JSON `{ "status": "success", "student_name": "Ali", "message": "Attendance marked." }`
- **Frontend**: `frontend/src/pages/Recognition.jsx`
- **Backend Route**: `backend/routes/recognition.py`
- **Service**: 
  - `backend/services/face_recognition_service.py` -> `recognize_face(image)` -> loads `models/encodings.pkl`
  - `backend/services/attendance_service.py` -> `mark_attendance(student_name)` -> writes to `data/attendance.csv`
