import streamlit as st
import numpy as np
import cv2
import tempfile
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image

st.set_page_config(page_title="Deepfake Detection System", layout="wide")

# --------- FUTURISTIC DARK THEME --------- #

st.markdown("""
<style>
body {
    background: radial-gradient(circle at top left, #1a002d, #000814 70%);
    color: white;
}

.block-container {
    padding-top: 2rem;
}

.hero {
    text-align: center;
    padding: 40px 20px;
}

.hero h1 {
    font-size: 55px;
    font-weight: 800;
    background: linear-gradient(90deg, #9d4edd, #00f5ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero p {
    font-size: 18px;
    opacity: 0.8;
}

.card {
    background: rgba(255, 255, 255, 0.05);
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0 0 30px rgba(157, 78, 221, 0.3);
    margin-top: 20px;
}

.result-real {
    color: #00ffcc;
    font-size: 26px;
    font-weight: bold;
}

.result-fake {
    color: #ff006e;
    font-size: 26px;
    font-weight: bold;
}

.stTabs [data-baseweb="tab"] {
    font-size: 18px;
}

</style>
""", unsafe_allow_html=True)

# --------- HERO --------- #

st.markdown("""
<div class="hero">
<h1>Deepfake Detection System</h1>
<p>AI-Powered Image & Video Forgery Detection Using Convolutional Neural Networks</p>
</div>
""", unsafe_allow_html=True)

model = load_model("image_deepfake_model.h5")

st.markdown("<div class='card'>", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["🖼 Image Analysis", "🎥 Video Analysis"])

# --------- IMAGE --------- #

with tab1:
    image_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

    if image_file:
        img = Image.open(image_file)
        st.image(img, use_container_width=True)

        img = img.resize((224, 224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0) / 255.0

        prediction = model.predict(img_array, verbose=0)[0][0]

        if prediction > 0.5:
            confidence = prediction * 100
            st.markdown(f"<div class='result-fake'>FAKE ({confidence:.2f}%)</div>", unsafe_allow_html=True)
        else:
            confidence = (1 - prediction) * 100
            st.markdown(f"<div class='result-real'>REAL ({confidence:.2f}%)</div>", unsafe_allow_html=True)

        st.progress(int(confidence))

# --------- VIDEO --------- #

with tab2:
    video_file = st.file_uploader("Upload Video", type=["mp4", "avi", "mov"])

    if video_file:
        st.video(video_file)

        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(video_file.read())

        cap = cv2.VideoCapture(tfile.name)

        process_every = 25
        fake_frames = 0
        real_frames = 0
        current_frame = 0

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            if current_frame % process_every == 0:
                frame = cv2.resize(frame, (224, 224))
                frame = np.expand_dims(frame / 255.0, axis=0)

                prediction = model.predict(frame, verbose=0)[0][0]

                if prediction > 0.5:
                    fake_frames += 1
                else:
                    real_frames += 1

            current_frame += 1

        cap.release()

        total = fake_frames + real_frames

        if total > 0:
            if fake_frames > real_frames:
                confidence = (fake_frames / total) * 100
                st.markdown(f"<div class='result-fake'>FAKE VIDEO ({confidence:.2f}%)</div>", unsafe_allow_html=True)
            else:
                confidence = (real_frames / total) * 100
                st.markdown(f"<div class='result-real'>REAL VIDEO ({confidence:.2f}%)</div>", unsafe_allow_html=True)

            st.progress(int(confidence))
            st.caption(f"Frames analyzed: {total}")

st.markdown("</div>", unsafe_allow_html=True)
