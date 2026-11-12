# Smart Attendance System

A professional, production-style Smart Attendance System utilizing an AI Face Recognition model. This project consists of a React (Vite) frontend and a FastAPI (Python) backend.

## Features
- AI Face Recognition based attendance marking
- Clean, responsive dashboard
- Student management
- Attendance history and analytics
- System status monitoring

## Technology Stack
- **Frontend**: React, Vite, Vanilla CSS
- **Backend**: Python, FastAPI, Uvicorn
- **AI/CV**: OpenCV, face_recognition, NumPy
- **Data**: CSV (pandas)

## Folder Structure
- `frontend/` - React frontend application.
- `backend/` - FastAPI backend application.
- `models/` - Directory for trained AI models (e.g., `encodings.pkl`).
- `data/` - CSV files containing attendance records.
- `docs/` - System architecture and debugging documentation.

## Installation & Environment Setup

1. **Clone the repository.**
2. **Environment Variables**: Copy `.env.example` to `.env` in both the root or specific folders as needed, and configure paths.

### Backend Setup
```bash
cd backend
python -m venv venv
# Windows: venv\Scripts\activate
# Mac/Linux: source venv/bin/activate
pip install -r requirements.txt
```

### Frontend Setup
```bash
cd frontend
npm install
```

## How to Run

**1. Start the Backend**
```bash
cd backend
uvicorn main:app --reload --port 8000
```
The backend API will be available at `http://localhost:8000`.

**2. Start the Frontend**
```bash
cd frontend
npm run dev
```
The frontend application will be available at `http://localhost:5173`.

## Connecting the Trained Model
Place your trained face-recognition model (e.g., `encodings.pkl`) in the `models/` directory.
Ensure that the `MODEL_PATH` inside the backend configuration points to this file. See `models/README.md` for more details.
