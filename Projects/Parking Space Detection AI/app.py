import streamlit as st
from ultralytics import YOLO
from PIL import Image
import tempfile
import os

# ===========================
# Page Configuration
# ===========================

st.set_page_config(
    page_title="Parking Space Detection AI",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ===========================
# Header
# ===========================

st.title("🚗 Parking Space Detection AI")

st.write("Welcome to the AI-powered Parking Space Detection System.")

st.success("Project Loaded Successfully ✅")

# ===========================
# Sidebar
# ===========================

st.sidebar.title("🚗 Parking AI")

st.sidebar.markdown("---")

st.sidebar.success("🟢 AI Model Loaded")

st.sidebar.markdown("## 📌 Project Information")

st.sidebar.info("""
**Model :** YOLOv8

**Framework :** Streamlit

**Language :** Python

**Detection :** Parking Spaces
""")

st.sidebar.markdown("---")

st.sidebar.write("👨‍💻 Developed by")

st.sidebar.write("**Anees Ur Rehman**")

# ===========================
# Main Heading
# ===========================

st.markdown("""
# 🚗 Parking Space Detection AI

### AI Powered Parking Space Detection System

Detect parking spaces using a trained YOLOv8 Deep Learning model.
""")

# ===========================
# Info Cards
# ===========================

col1, col2, col3 = st.columns(3)

with col1:
    st.info("🧠 Model\n\nYOLOv8")

with col2:
    st.success("⚡ Speed\n\nReal-Time Detection")

with col3:
    st.warning("🎯 Accuracy\n\nHigh Precision")

st.divider()

# ===========================
# Instructions
# ===========================

st.subheader("📋 Instructions")

st.markdown("""
1. Upload a parking lot image.

2. Click **Detect Parking Spaces**.

3. View AI prediction.

4. Download the result image.
""")

st.divider()

# ===========================
# Upload Image
# ===========================

uploaded_file = st.file_uploader(
    "📤 Upload Parking Image",
    type=["jpg", "jpeg", "png"]
)

st.divider()

st.caption("© 2026 Parking Space Detection AI | Developed by Anees Ur Rehman")

# ===========================
# Load YOLO Model
# ===========================

@st.cache_resource
def load_model():
    return YOLO("best.pt")

model = load_model()

# ===========================
# Detection Function
# ===========================

# ===========================
# Detection Function
# ===========================

def detect_parking_spaces(image):

    # Temporary image save
    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".jpg"
    ) as temp_file:

        image.save(temp_file.name)
        temp_path = temp_file.name

    # YOLO Prediction
    results = model.predict(
        source=temp_path,
        conf=0.25,
        save=False,
        verbose=False
    )

    # Windows me file lock hoti hai,
    # isliye os.remove() nahi use karenge.

    return results

# ===========================
# Detection Logic
# ===========================

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("📷 Original Image")

        st.image(image, use_container_width=True)

    if st.button("🚀 Detect Parking Spaces", use_container_width=True):

        with st.spinner("🔍 Detecting Parking Spaces..."):

            results = detect_parking_spaces(image)

        result_image = results[0].plot()

        detections = len(results[0].boxes)

        with col2:

            st.subheader("🤖 Detection Result")

            st.image(
                result_image,
                channels="BGR",
                use_container_width=True
            )

        st.success("✅ Detection Completed Successfully")

        st.info(f"🚗 Total Parking Spaces Detected: {detections}")

# ===========================
# Detection Statistics
# ===========================

if uploaded_file is not None:

    if st.button("📊 Show Detection Statistics", use_container_width=True):

        results = detect_parking_spaces(image)

        boxes = results[0].boxes

        detections = len(boxes)

        confidences = []

        for box in boxes:
            confidences.append(float(box.conf[0]))

        if len(confidences) > 0:

            avg_conf = sum(confidences) / len(confidences)
            max_conf = max(confidences)
            min_conf = min(confidences)

        else:

            avg_conf = 0
            max_conf = 0
            min_conf = 0

        st.divider()

        st.subheader("📊 Detection Statistics")

        c1, c2, c3, c4 = st.columns(4)

        with c1:
            st.metric(
                "🚗 Parking Spaces",
                detections
            )

        with c2:
            st.metric(
                "📈 Avg Confidence",
                f"{avg_conf*100:.1f}%"
            )

        with c3:
            st.metric(
                "🔥 Highest",
                f"{max_conf*100:.1f}%"
            )

        with c4:
            st.metric(
                "📉 Lowest",
                f"{min_conf*100:.1f}%"
            )

# ===========================
# Detection Table
# ===========================

import pandas as pd

if uploaded_file is not None:

    if st.button("📋 Show Detection Table", use_container_width=True):

        results = detect_parking_spaces(image)

        boxes = results[0].boxes

        data = []

        for i, box in enumerate(boxes):

            confidence = float(box.conf[0])

            data.append({
                "ID": i + 1,
                "Class": "Parking Space",
                "Confidence (%)": round(confidence * 100, 2)
            })

        if len(data) > 0:

            st.divider()

            st.subheader("📋 Detection Table")

            df = pd.DataFrame(data)

            st.table(df)

        else:

            st.warning("No Parking Space Detected.")

# ===========================
# Download Detection Result
# ===========================

import cv2

if uploaded_file is not None:

    if st.button("💾 Download Detection Result", use_container_width=True):

        results = detect_parking_spaces(image)

        result_image = results[0].plot()

        output_file = "Parking_Detection_Result.jpg"

        cv2.imwrite(output_file, result_image)

        with open(output_file, "rb") as file:

            st.download_button(
                label="📥 Click Here To Download",
                data=file,
                file_name="Parking_Detection_Result.jpg",
                mime="image/jpeg",
                use_container_width=True
            )

        st.success("✅ Detection Image Ready For Download")

# ===========================
# Professional Footer
# ===========================

st.divider()

st.markdown("## ℹ️ About This Project")

st.info("""
This AI system detects parking spaces using a YOLOv8 Deep Learning model.

### Features

✅ Parking Space Detection

✅ Detection Statistics

✅ Detection Table

✅ Download Detection Result

### Technologies Used

• Python

• Streamlit

• YOLOv8

• OpenCV

• Pillow

• Ultralytics
""")

st.divider()

st.markdown(
    """
    <center>
        <h4>🚗 Parking Space Detection AI</h4>
        <p>Developed by <b>Anees Ur Rehman</b></p>
        <p>© 2026 All Rights Reserved</p>
    </center>
    """,
    unsafe_allow_html=True
)

# ===========================
# Model Information
# ===========================

st.divider()

with st.expander("🧠 Model Information"):

    st.markdown("""
### YOLOv8 Model

**Model Name:** YOLOv8

**Task:** Object Detection

**Framework:** Ultralytics YOLO

**Programming Language:** Python

**Frontend:** Streamlit

**Dataset:** Parking Space Dataset

**Classes:** Parking Space

**Input Type:** Parking Lot Image

**Output:** Detected Parking Spaces with Bounding Boxes
""")

st.divider()

with st.expander("📂 Project Folder Structure"):

    st.code("""
Parking Space Detection AI
│
├── app.py
├── best.pt
├── requirements.txt
├── uploads/
├── outputs/
└── assets/
""")

st.divider()

with st.expander("🚀 Future Improvements"):

    st.markdown("""
✅ Live Camera Detection

✅ Video Detection

✅ Parking Occupancy Counter

✅ Free Parking Counter

✅ Occupied Parking Counter

✅ Deploy on Streamlit Cloud

✅ Deploy on Hugging Face

✅ Mobile Responsive UI
""")

# ===========================
# AI Dashboard
# ===========================

st.divider()

st.subheader("📊 AI Dashboard")

d1, d2, d3, d4 = st.columns(4)

with d1:
    st.metric(
        "🧠 Model",
        "YOLOv8"
    )

with d2:
    st.metric(
        "📂 Dataset",
        "Parking"
    )

with d3:
    st.metric(
        "🎯 Classes",
        "1"
    )

with d4:
    st.metric(
        "🟢 Status",
        "Ready"
    )

st.divider()

st.success("🎉 Parking Space Detection AI is Ready for Deployment!")

st.balloons()

