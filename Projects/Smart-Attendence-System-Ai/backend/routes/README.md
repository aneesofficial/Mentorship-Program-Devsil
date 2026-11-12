# Backend Routes

This folder contains FastAPI route definitions. All business logic is deferred to `backend/services/`.

- `dashboard.py`: Aggregates stats.
- `students.py`: Lists students known to the model.
- `attendance.py`: Fetches CSV records.
- `recognition.py`: The main POST endpoint that accepts webcam images.
- `system.py`: Exposes system health and path configs.
