import streamlit as st
import tensorflow as tf
import numpy as np
import pandas as pd
import plotly.express as px

from PIL import Image

# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="Currency Note Recognition AI",
    page_icon="💵",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# Custom CSS
# ==========================================

st.markdown("""
<style>

.main{
    padding-top:20px;
}

.block-container{
    padding-top:2rem;
}

.stButton>button{
    width:100%;
    border-radius:10px;
    height:50px;
    font-size:18px;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# Class Names
# ==========================================

CLASS_NAMES = [

    "Afghani_10",
    "Afghani_100",
    "Afghani_1000",
    "Afghani_20",
    "Afghani_50",
    "Afghani_500",

    "PKR_10",
    "PKR_100",
    "PKR_1000",
    "PKR_20",
    "PKR_50",
    "PKR_500",
    "PKR_5000"

]

# ==========================================
# Currency Information
# ==========================================

CURRENCY_INFO = {

"PKR_10":"Pakistani Rupees 10",

"PKR_20":"Pakistani Rupees 20",

"PKR_50":"Pakistani Rupees 50",

"PKR_100":"Pakistani Rupees 100",

"PKR_500":"Pakistani Rupees 500",

"PKR_1000":"Pakistani Rupees 1000",

"PKR_5000":"Pakistani Rupees 5000",

"Afghani_10":"Afghani 10",

"Afghani_20":"Afghani 20",

"Afghani_50":"Afghani 50",

"Afghani_100":"Afghani 100",

"Afghani_500":"Afghani 500",

"Afghani_1000":"Afghani 1000"

}

# ==========================================
# Load Model
# ==========================================

@st.cache_resource
def load_model():

    model = tf.keras.models.load_model(
        "Best_Currency_Model.keras"
    )

    return model

model = load_model()

# ==========================================
# Image Preprocessing
# ==========================================

def preprocess_image(image):

    image = image.resize((224,224))

    image = np.array(image)

    if image.shape[-1] == 4:
        image = image[:,:,:3]

    image = image.astype("float32") / 255.0

    image = np.expand_dims(image,axis=0)

    return image

# ==========================================
# Prediction Function
# ==========================================

def predict(image):

    img = preprocess_image(image)

    prediction = model.predict(
        img,
        verbose=0
    )

    index = np.argmax(prediction)

    confidence = float(
        np.max(prediction)*100
    )

    return prediction,index,confidence

# ==========================================
# Sidebar
# ==========================================

st.sidebar.title("💵 Currency AI")

st.sidebar.markdown("---")

st.sidebar.success("AI Model Loaded")

st.sidebar.write("Classes :",len(CLASS_NAMES))

st.sidebar.markdown("---")

st.sidebar.info("""

Professional Currency Recognition

CNN Deep Learning

Developer

Anees Ur Rehman

""")

# ==========================================
# Main Header
# ==========================================

st.title("💵 Currency Note Recognition Assistant")

st.markdown("""
### Professional AI Powered Currency Detection System

Detect **Pakistani 🇵🇰** and **Afghani 🇦🇫** currency notes using a trained Deep Learning CNN model.
""")

st.markdown("---")

# ==========================================
# Dashboard Cards
# ==========================================

card1, card2, card3, card4 = st.columns(4)

with card1:
    st.metric(
        "Model",
        "CNN"
    )

with card2:
    st.metric(
        "Classes",
        len(CLASS_NAMES)
    )

with card3:
    st.metric(
        "Framework",
        "TensorFlow"
    )

with card4:
    st.metric(
        "Status",
        "Ready ✅"
    )

st.markdown("---")

# ==========================================
# Upload Section
# ==========================================

st.header("📤 Upload Currency Note")

uploaded_file = st.file_uploader(

    "Choose Currency Image",

    type=[
        "jpg",
        "jpeg",
        "png"
    ]

)

# ==========================================
# Image Preview
# ==========================================

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    left,right = st.columns([1,1])

    with left:

        st.subheader("Uploaded Image")

        st.image(
            image,
            use_container_width=True
        )

    with right:

        st.subheader("Image Details")

        st.success("Image Uploaded Successfully")

        st.write("Filename :", uploaded_file.name)

        st.write("Size :", image.size)

        st.write("Mode :", image.mode)

        st.write("Format :", image.format)

        st.info(
            "Click the Predict button below."
        )

    st.markdown("---")

    predict_button = st.button(
        "🚀 Predict Currency"
    )

    # ==========================================
# Prediction Section
# ==========================================

    if predict_button:

        with st.spinner("🔍 AI is analyzing the currency note..."):

            prediction, predicted_index, confidence = predict(image)

            predicted_class = CLASS_NAMES[predicted_index]

        st.markdown("---")

        st.subheader("🤖 AI Prediction Result")

        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric(
                "Predicted Currency",
                predicted_class
            )

        with c2:
            st.metric(
                "Confidence",
                f"{confidence:.2f}%"
            )

        with c3:

            if confidence >= 90:
                st.success("Excellent ✅")

            elif confidence >= 75:
                st.warning("Good ⚡")

            else:
                st.error("Low ❌")

        st.markdown("---")

        st.subheader("💰 Currency Information")

        st.info(
            CURRENCY_INFO[predicted_class]
        )

# ==========================================
# Top 3 Predictions
# ==========================================

        st.markdown("---")

        st.subheader("🏆 Top 3 Predictions")

        probabilities = prediction[0]

        top3 = np.argsort(probabilities)[::-1][:3]

        top3_df = pd.DataFrame({

            "Currency":[CLASS_NAMES[i] for i in top3],

            "Confidence (%)":[
                round(float(probabilities[i]*100),2)
                for i in top3
            ]

        })

        st.dataframe(
            top3_df,
            use_container_width=True,
            hide_index=True
        )

# ==========================================
# Interactive Chart
# ==========================================

        st.markdown("---")

        st.subheader("📊 Confidence Analysis")

        chart_df = pd.DataFrame({

            "Currency":CLASS_NAMES,

            "Probability":probabilities*100

        })

        chart_df = chart_df.sort_values(
            "Probability",
            ascending=False
        )

        fig = px.bar(

            chart_df,

            x="Currency",

            y="Probability",

            text="Probability",

            title="Prediction Probability"

        )

        fig.update_traces(
            texttemplate="%{text:.2f}%",
            textposition="outside"
        )

        fig.update_layout(
            height=500
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

# ==========================================
# Download Report
# ==========================================

        report = f"""
Currency Prediction Report

Predicted Currency : {predicted_class}

Confidence : {confidence:.2f} %

Model : CNN Deep Learning

Developer : Anees Ur Rehman
"""

        st.download_button(

            "📥 Download Report",

            report,

            file_name="prediction_report.txt"

        )

        # ==========================================
# Prediction History
# ==========================================

        st.markdown("---")

        st.subheader("📜 Prediction History")

        history_df = pd.DataFrame({

            "Currency":[predicted_class],

            "Confidence":[f"{confidence:.2f}%"]

        })

        st.dataframe(
            history_df,
            use_container_width=True,
            hide_index=True
        )

# ==========================================
# About Project
# ==========================================

st.markdown("---")

with st.expander("ℹ️ About This Project"):

    st.markdown("""

### 💵 Currency Note Recognition AI

This application is developed using:

- TensorFlow
- CNN Deep Learning
- Streamlit
- Plotly
- NumPy
- Pandas

### Supported Currency

🇵🇰 Pakistani Currency Notes

🇦🇫 Afghani Currency Notes

### Model Performance

✅ Test Accuracy : 84%

✅ Validation Accuracy : 90.9%

### Developer

Anees Ur Rehman

""")

# ==========================================
# Footer
# ==========================================

st.markdown("---")

st.markdown(
"""
<div style='text-align:center;padding:20px;'>

<h3>💵 Currency Note Recognition AI</h3>

<p>
Deep Learning Based Currency Detection System
</p>

<p>
Developed by <b>Anees Ur Rehman</b>
</p>

<p>
TensorFlow | Streamlit | Plotly
</p>

</div>
""",
unsafe_allow_html=True
)

# ==========================================
# Sidebar Extra Information
# ==========================================

st.sidebar.markdown("---")

st.sidebar.subheader("📊 Project Info")

st.sidebar.write("Version : 2.0")

st.sidebar.write("Model : CNN")

st.sidebar.write("Classes : 13")

st.sidebar.write("Accuracy : 84%")

st.sidebar.write("Status : Production Ready ✅")

st.sidebar.markdown("---")

st.sidebar.success("Tips")

st.sidebar.write("✔ Upload Clear Image")

st.sidebar.write("✔ JPG / PNG Only")

st.sidebar.write("✔ Front Side Preferred")

st.sidebar.write("✔ High Quality Image")