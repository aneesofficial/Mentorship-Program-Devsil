# Trained Models Directory

**IMPORTANT:** Place your existing trained face-recognition model files inside this directory.

For example, if you have an `encodings.pkl` file, place it here.

## Connecting to Backend
The model is loaded inside `backend/services/face_recognition_service.py`.
It reads the location from the `MODEL_PATH` variable configured in `backend/config.py`.

By default, the expected path is:
`models/encodings.pkl`

**DO NOT** replace the model logic with fake data. Ensure your model format is compatible with the loading logic inside the `face_recognition_service.py` file, or adjust the service slightly if your model uses a different format (like `.pt`, `.h5`, or custom class structures).
