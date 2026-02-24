import streamlit as st
import requests
from PIL import Image

# ==============================
# BACKEND URL (Render)
# ==============================
API_URL = "https://deepfake-detection-system-backend.onrender.com"

st.set_page_config(
    page_title="Deepfake Detection System",
    page_icon="🧠",
    layout="wide"
)

# ==============================
# TITLE
# ==============================

st.title("🧠 Deepfake Detection System")
st.markdown("Upload an **Image** or **Video** to detect whether it is Real or Fake.")

st.sidebar.title("Navigation")
option = st.sidebar.selectbox("Choose Input Type", ["Image", "Video"])

# ==============================
# IMAGE SECTION
# ==============================

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

                try:
                    response = requests.post(
                        f"{API_URL}/predict-image/",
                        files={
                            "file": (
                                uploaded_file.name,
                                uploaded_file.getvalue(),
                                uploaded_file.type
                            )
                        }
                    )

                    st.write("Status Code:", response.status_code)

                    if response.status_code == 200:
                        result = response.json()

                        prediction = result.get("prediction")
                        confidence = result.get("confidence")

                        st.success(f"Prediction: {prediction}")
                        st.info(f"Confidence: {round(confidence * 100, 2)}%")
                    else:
                        st.error(response.text)

                except Exception as e:
                    st.error(f"Connection Error: {e}")

# ==============================
# VIDEO SECTION
# ==============================

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

                try:
                    response = requests.post(
                        f"{API_URL}/predict-video/",
                        files={
                            "file": (
                                uploaded_video.name,
                                uploaded_video.getvalue(),
                                uploaded_video.type
                            )
                        }
                    )

                    st.write("Status Code:", response.status_code)

                    if response.status_code == 200:
                        result = response.json()

                        prediction = result.get("prediction")
                        confidence = result.get("confidence")

                        st.success(f"Prediction: {prediction}")
                        st.info(f"Confidence: {round(confidence * 100, 2)}%")
                    else:
                        st.error(response.text)

                except Exception as e:
                    st.error(f"Connection Error: {e}")

# ==============================
# FOOTER
# ==============================

st.markdown("---")
