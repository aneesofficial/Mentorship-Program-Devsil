import cv2
import numpy as np
import os
import pickle
from config import MODEL_PATH
import face_recognition

class FaceRecognitionService:
    def __init__(self):
        self.known_face_encodings = []
        self.known_face_names = []
        self.is_model_loaded = False
        self.load_model()

    def load_model(self):
        """
        MODEL INPUT
            ↓
        Loads encodings from the specified MODEL_PATH.
        """
        if not os.path.exists(MODEL_PATH):
            print(f"Warning: Model file not found at {MODEL_PATH}")
            return

        try:
            with open(MODEL_PATH, 'rb') as f:
                data = pickle.load(f)
                # Assuming data is a dict: {"encodings": [...], "names": [...]}
                # Modify this based on your exact trained model format.
                if isinstance(data, dict):
                    self.known_face_encodings = data.get("encodings", [])
                    self.known_face_names = data.get("names", [])
                elif isinstance(data, list):
                    # Alternatively, maybe a list of tuples? Adjust as needed.
                    pass
            self.is_model_loaded = True
            print("Model loaded successfully.")
        except Exception as e:
            print(f"Error loading model: {e}")

    def get_registered_students(self):
        """Returns a list of unique student names registered in the model."""
        return list(set(self.known_face_names))

    def recognize_face(self, image_bytes: bytes) -> dict:
        """
        IMAGE PREPROCESSING
            ↓
        FACE DETECTION
            ↓
        FACE ENCODING
            ↓
        FACE MATCHING
            ↓
        STUDENT IDENTIFICATION
        """
        if not self.is_model_loaded:
            return {"status": "error", "message": "Face recognition model is not loaded."}

        try:
            # Convert image bytes to numpy array then to OpenCV format
            nparr = np.frombuffer(image_bytes, np.uint8)
            img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

            if img is None:
                return {"status": "error", "message": "Invalid image data."}

            # Convert BGR (OpenCV) to RGB (face_recognition)
            rgb_small_frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            # Detect faces
            face_locations = face_recognition.face_locations(rgb_small_frame)
            if not face_locations:
                return {"status": "error", "message": "No face detected in the image."}

            # Get encodings for detected faces
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
            
            # For simplicity, we assume we are recognizing the first face found.
            # You can loop through all if needed.
            face_encoding = face_encodings[0]

            # Compare faces
            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
            name = "Unknown"
            confidence = 0.0

            # Use the known face with the smallest distance
            face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
            if len(face_distances) > 0:
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = self.known_face_names[best_match_index]
                    confidence = round((1 - face_distances[best_match_index]) * 100, 2)

            if name != "Unknown":
                return {
                    "status": "success",
                    "student_name": name,
                    "confidence": confidence
                }
            else:
                return {
                    "status": "error",
                    "message": "Face not recognized."
                }

        except Exception as e:
            return {"status": "error", "message": f"Recognition failed: {str(e)}"}

# Singleton instance to be used across routes
face_service = FaceRecognitionService()
