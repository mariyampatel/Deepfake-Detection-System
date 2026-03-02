import streamlit as st
import random
from PIL import Image

# ===================================
# PAGE CONFIG
# ===================================

st.set_page_config(
    page_title="Deepfake Detection System",
    page_icon="🧠",
    layout="wide"
)

# ===================================
# CUSTOM CSS (Professional UI)
# ===================================

st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #1f1c2c, #928dab);
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        border-radius: 8px;
        padding: 10px 24px;
    }
    </style>
""", unsafe_allow_html=True)

# ===================================
# TITLE
# ===================================

st.title("🧠 Deepfake Detection System")
st.markdown("Upload an **Image** or **Video** to detect whether it is **Real or Fake**.")

st.sidebar.title("Navigation")
option = st.sidebar.radio("Choose Input Type", ["Image", "Video"])

# ===================================
# DUMMY PREDICTION FUNCTION
# ===================================

def predict_dummy():
    prediction = random.choice(["Real", "Fake"])
    confidence = round(random.uniform(0.75, 0.99), 4)
    return prediction, confidence

# ===================================
# IMAGE SECTION
# ===================================

if option == "Image":

    st.header("🖼 Image Deepfake Detection")

    uploaded_file = st.file_uploader(
        "Upload Image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)

        if st.button("Predict Image"):

            with st.spinner("Analyzing Image..."):

                prediction, confidence = predict_dummy()

                if prediction == "Real":
                    st.success(f"Prediction: {prediction}")
                else:
                    st.error(f"Prediction: {prediction}")

                st.info(f"Confidence: {confidence * 100:.2f}%")

# ===================================
# VIDEO SECTION
# ===================================

elif option == "Video":

    st.header("🎥 Video Deepfake Detection")

    uploaded_video = st.file_uploader(
        "Upload Video",
        type=["mp4", "mov", "avi"]
    )

    if uploaded_video is not None:

        st.video(uploaded_video)

        if st.button("Predict Video"):

            with st.spinner("Analyzing Video..."):

                prediction, confidence = predict_dummy()

                if prediction == "Real":
                    st.success(f"Prediction: {prediction}")
                else:
                    st.error(f"Prediction: {prediction}")

                st.info(f"Confidence: {confidence * 100:.2f}%")

# ===================================
# FOOTER
# ===================================

st.markdown("---")
st.markdown("© 2026 Deepfake Detection System | Final Year Project")
