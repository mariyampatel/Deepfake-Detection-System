import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.set_page_config(page_title="Deepfake Detection System")

st.title("Deepfake Detection System")
st.write("Upload an image to check if it is Real or Fake (Demo Version)")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Convert image to numpy array
    img_array = np.array(image)

    # Convert to grayscale (demo processing)
    gray = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)

    # Simple demo logic (Random Prediction)
    prediction = np.random.choice(["Real", "Fake"])

    st.subheader("Prediction Result:")
    if prediction == "Real":
        st.success("This image is predicted as REAL")
    else:
        st.error("This image is predicted as FAKE")

    st.info("Note: This is a demo version without ML model.")
