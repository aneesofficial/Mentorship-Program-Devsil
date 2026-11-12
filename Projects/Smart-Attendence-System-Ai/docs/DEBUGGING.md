# Debugging Guide

When issues occur in the Smart Attendance System, use this guide to trace the problem.

## General Flow
The system flows from Frontend -> API Services -> Backend Routes -> Backend Services -> Data/Models. Always follow the chain.

## 1. Dashboard is Blank or Not Loading
- **Check Frontend**: `frontend/src/pages/Dashboard.jsx` - Is the component mounting? Is state updating?
- **Check API Call**: `frontend/src/services/api.js` - Is `getDashboardStats()` returning a 200 OK?
- **Check Backend Route**: `backend/routes/dashboard.py` - Is the `/api/dashboard` endpoint hit? Check terminal logs.
- **Check Service Layer**: `backend/services/attendance_service.py` - Is it successfully reading the CSV file?
- **Check Data**: `data/attendance.csv` - Ensure the file exists and is readable.

## 2. Face Recognition Fails
- **Check Frontend**: `frontend/src/pages/Recognition.jsx` - Is the webcam active? Is the image being captured properly as a Blob?
- **Check API Call**: Network Tab in Browser. Is `/api/recognition` sending a POST request with valid multipart data?
- **Check Backend Route**: `backend/routes/recognition.py` - Is the file being received?
- **Check Model Service**: `backend/services/face_recognition_service.py` - Is the trained model (`models/encodings.pkl`) loading correctly? If `FileNotFoundError` occurs, the path is wrong.
- **Check Data/Model**: Ensure your `encodings.pkl` exists inside the `models/` folder.

## 3. Attendance is Not Saving
- **Check Service Logic**: `backend/services/attendance_service.py` - Look at `mark_attendance`. Is the file locked by Excel or another program?
- **Check Duplicates**: Is the system correctly saying "already marked present" but you expected it to write? Ensure the date logic correctly compares today's date.
- **Check CSV File**: `data/attendance.csv` - Check for file permissions.

## Common Errors
- `CORS Error`: Ensure Vite frontend port is allowed in `backend/main.py` CORS middleware.
- `500 Internal Server Error`: Check the backend terminal (uvicorn logs) to see the exact Python traceback. Raw errors are caught by standard FastAPI exception handlers.
