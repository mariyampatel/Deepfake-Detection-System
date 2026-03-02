import streamlit as st
import random
from PIL import Image
import time

# ===================================
# 1. PAGE CONFIGURATION
# ===================================
st.set_page_config(
    page_title="Deepfake Scanner",
    page_icon="👁️",
    layout="centered", # Centered for a more focused, app-like feel
    initial_sidebar_state="expanded"
)

# ===================================
# 2. CYBER-THEMED CUSTOM CSS
# ===================================
st.markdown("""
    <style>
    /* Full Page Background Color / Gradient */
    .stApp {
        background: linear-gradient(135deg, #0b132b, #1c2541, #0b132b);
        color: #e0e1dd;
    }
    .sidebar-title {
            color: #000066;
            font-size: 26px;
            font-weight: bold;
        }
    /* Typography */
    h1, h2, h3 {
        color: #00FFEA !important;
        font-family: 'Courier New', Courier, monospace;
        text-align: center;
    }
    
    /* Custom Neon Button */
    div.stButton > button {
        background: transparent;
        color: #00FFEA;
        border: 2px solid #00FFEA;
        border-radius: 8px;
        padding: 10px 24px;
        font-size: 16px;
        font-weight: 700;
        letter-spacing: 1px;
        text-transform: uppercase;
        width: 100%;
        transition: 0.3s ease-in-out;
    }
    div.stButton > button:hover {
        background: #00FFEA;
        color: #0b132b;
        box-shadow: 0 0 15px #00FFEA;
    }
    
    /* Result Cards */
    .scan-result-fake {
        background: rgba(255, 0, 60, 0.1);
        border-left: 5px solid #ff003c;
        padding: 20px;
        border-radius: 5px;
        text-align: center;
    }
    .scan-result-real {
        background: rgba(0, 255, 234, 0.1);
        border-left: 5px solid #00FFEA;
        padding: 20px;
        border-radius: 5px;
        text-align: center;
    }
    .score-text {
        font-size: 2.5rem;
        font-weight: bold;
        margin: 0;
    }
    </style>
""", unsafe_allow_html=True)

# ===================================
# 3. CORE LOGIC (UNTOUCHED)
# ===================================
def predict_dummy():
    """Dummy prediction logic"""
    prediction = random.choice(["Real", "Fake"])
    confidence = round(random.uniform(0.75, 0.99), 4)
    return prediction, confidence

# ===================================
# 4. SIDEBAR WITH IMAGE
# ===================================
# Adding a cool AI aesthetic picture to the sidebar
st.sidebar.image("https://images.unsplash.com/photo-1620712943543-bcc4688e7485?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", caption="Neural Engine Online")

st.sidebar.markdown('<p class="sidebar-title">System Controls</p>', unsafe_allow_html=True)
option = st.sidebar.radio("Select Targeting Mode:", ["🖼️ Image Scan", "🎥 Video Scan"])

st.sidebar.markdown("---")
st.sidebar.markdown("<p style='color: #888; font-size: 0.8rem;'>System Status: Active<br>Server: Secure Connection</p>", unsafe_allow_html=True)

# ===================================
# 5. MAIN UI & HEADER IMAGE
# ===================================
# Adding a high-tech banner image at the top of the app
st.image("image_1.png", use_container_width=True) # CHANGED: Uses the provided image as the main banner

st.title("DEEPFAKE NEURAL SCANNER")
st.markdown("<p style='text-align: center; color: #a8b2d1; margin-bottom: 30px;'>Upload suspect media to our forensic neural network for authenticity verification.</p>", unsafe_allow_html=True)

# ===================================
# IMAGE SCANNER
# ===================================
if option == "🖼️ Image Scan":
    
    uploaded_file = st.file_uploader("INITIALIZE IMAGE UPLOAD", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        # Display the uploaded image inside a styled container
        with st.container(border=True):
            st.image(image, caption="Target Acquired", use_container_width=True)

        if st.button("INITIATE SCAN SEQUENCE"):
            
            # Using an empty placeholder to create a cool scanning text effect
            status_text = st.empty()
            status_text.markdown("<h4 style='text-align: center; color: #ffbc42;'>Running facial landmark analysis...</h4>", unsafe_allow_html=True)
            time.sleep(1) # Fake delay for effect
            status_text.markdown("<h4 style='text-align: center; color: #ffbc42;'>Detecting pixel manipulation...</h4>", unsafe_allow_html=True)
            time.sleep(1.5)
            status_text.empty() # Clear the status text

            prediction, confidence = predict_dummy()

            # Display the Cyber-themed results
            if prediction == "Fake":
                st.markdown(f"""
                    <div class="scan-result-fake">
                        <h2 style="color: #ff003c; margin: 0;">🚨 THREAT DETECTED: {prediction.upper()} 🚨</h2>
                        <p style="color: #ccc; margin-top: 10px;">Artificial manipulation identified in media structure.</p>
                        <p class="score-text" style="color: #ff003c;">{confidence * 100:.2f}%</p>
                        <p>Confidence Score</p>
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                    <div class="scan-result-real">
                        <h2 style="color: #00FFEA; margin: 0;">✅ MEDIA AUTHENTICATED: {prediction.upper()}</h2>
                        <p style="color: #ccc; margin-top: 10px;">No deepfake artifacts detected in neural scan.</p>
                        <p class="score-text" style="color: #00FFEA;">{confidence * 100:.2f}%</p>
                        <p>Confidence Score</p>
                    </div>
                """, unsafe_allow_html=True)

# ===================================
# VIDEO SCANNER
# ===================================
elif option == "🎥 Video Scan":
    
    uploaded_video = st.file_uploader("INITIALIZE VIDEO UPLOAD", type=["mp4", "mov", "avi"])

    if uploaded_video is not None:
        with st.container(border=True):
            st.video(uploaded_video)

        if st.button("INITIATE FRAME SCAN"):
            
            status_text = st.empty()
            status_text.markdown("<h4 style='text-align: center; color: #ffbc42;'>Extracting frames for temporal analysis...</h4>", unsafe_allow_html=True)
            time.sleep(2)
            status_text.empty()

            prediction, confidence = predict_dummy()

            if prediction == "Fake":
                st.markdown(f"""
                    <div class="scan-result-fake">
                        <h2 style="color: #ff003c; margin: 0;">🚨 THREAT DETECTED: {prediction.upper()} 🚨</h2>
                        <p style="color: #ccc; margin-top: 10px;">Temporal inconsistencies and artificial artifacts identified.</p>
                        <p class="score-text" style="color: #ff003c;">{confidence * 100:.2f}%</p>
                        <p>Confidence Score</p>
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                    <div class="scan-result-real">
                        <h2 style="color: #00FFEA; margin: 0;">✅ MEDIA AUTHENTICATED: {prediction.upper()}</h2>
                        <p style="color: #ccc; margin-top: 10px;">Video sequence cleared by neural engine.</p>
                        <p class="score-text" style="color: #00FFEA;">{confidence * 100:.2f}%</p>
                        <p>Confidence Score</p>
                    </div>
                """, unsafe_allow_html=True)

# ===================================
# FOOTER
# ===================================
st.markdown("<br><hr style='border-color: #1c2541;'>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #555;'>DEEPFAKE FORENSICS v2.0 | ENCRYPTED CONNECTION</p>", unsafe_allow_html=True)
