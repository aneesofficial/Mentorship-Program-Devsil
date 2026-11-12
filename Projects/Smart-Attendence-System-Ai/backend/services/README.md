# Backend Services

This folder contains the core business logic of the application, keeping routes clean.

## `attendance_service.py`
Handles all I/O operations with `data/attendance.csv`. Includes duplicate checks, fetching today's records, and marking attendance.

## `face_recognition_service.py`
Loads the trained model (`models/encodings.pkl`) upon startup. Exposes methods to pass image bytes through the model for inference. Adjust the `load_model` method if your `encodings.pkl` has a different dictionary structure.
