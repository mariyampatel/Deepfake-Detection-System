import streamlit as st
import random
from PIL import Image
import time

# ===================================
# 1. PAGE CONFIGURATION
# ===================================
st.set_page_config(
    page_title="Deepfake Scanner",
    page_icon="🛡️",
    layout="centered",
    initial_sidebar_state="expanded"
)

# ===================================
# 2. LIGHT BLUE & NAVY CUSTOM CSS
# ===================================
st.markdown("""
    <style>
    /* Main Background - Light Blue */
    .stApp {
        background-color: #F0F8FF; 
        color: #333333;
    }
    
    /* Sidebar - Professional Dark Navy Blue (Not Super Dark) */
    [data-testid="stSidebar"] {
        background-color: #001f3f;
    }
    
    /* Force Sidebar text to be White for visibility */
    [data-testid="stSidebar"] * {
        color: white !important;
    }
    
    /* Typography - Navy Blue for Headers */
    h1, h2, h3 {
        color: #000080 !important;
        font-family: 'Segoe UI', sans-serif;
        text-align: center;
    }
    
    /* Custom Button */
    div.stButton > button {
        background: #000080;
        color: white;
        border-radius: 8px;
        padding: 10px 24px;
        font-weight: 700;
        width: 100%;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background: #0056b3;
        color: white;
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
        background: rgba(0, 128, 0, 0.1);
        border-left: 5px solid #008000;
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
# 3. CORE LOGIC
# ===================================
def predict_dummy():
    """Dummy prediction logic"""
    prediction = random.choice(["Real", "Fake"])
    confidence = round(random.uniform(0.75, 0.99), 4)
    return prediction, confidence

# ===================================
# 4. SIDEBAR WITH IMAGE
# ===================================
# Professional Digital Face ID Icon for Sidebar (Replaces Puppy Emoji)
st.sidebar.markdown(
    """
    <div style="text-align: center; padding-top: 20px;">
        <img src="https://img.icons8.com/color/144/facial-recognition.png" alt="Forensic Logo" width="80">
        <p style='color: white; margin-top: 10px; font-size: 0.9rem;'>Forensic ID Engine</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Force text colors in sidebar
st.sidebar.markdown("<h2 style='text-align: center;'>System Controls</h2>", unsafe_allow_html=True)
option = st.sidebar.radio("Navigation:", ["🖼️ Image Scan", "🎥 Video Scan"])

st.sidebar.markdown("---")
st.sidebar.write("System Status: Active")

# ===================================
# 5. MAIN UI & HEADER IMAGE
# ===================================
# Professional Face Scanning Image (Replaces Puppy Main Photo)
st.image("https://images.unsplash.com/photo-1593006526978-651c6c132890?q=80&w=1000&auto=format&fit=crop", use_container_width=True)

st.title("DEEPFAKE NEURAL SCANNER")
st.markdown("<p style='text-align: center; color: #555; margin-bottom: 30px; font-weight: 500;'>Upload suspect media to our forensic neural network for authenticity verification.</p>", unsafe_allow_html=True)

# ===================================
# IMAGE SCANNER
# ===================================
if option == "🖼️ Image Scan":
    
    uploaded_file = st.file_uploader("INITIALIZE IMAGE UPLOAD", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        with st.container(border=True):
            st.image(image, caption="Target Acquired", use_container_width=True)

        if st.button("RUN NEURAL SCAN"):
            
            status_text = st.empty()
            status_text.markdown("<h4 style='text-align: center; color: #ffbc42;'>Running facial landmark analysis...</h4>", unsafe_allow_html=True)
            time.sleep(1) # Delay for effect
            status_text.markdown("<h4 style='text-align: center; color: #ffbc42;'>Detecting pixel manipulation...</h4>", unsafe_allow_html=True)
            time.sleep(1.5)
            status_text.empty() # Clear the status text

            prediction, confidence = predict_dummy()

            # Display the results
            if prediction == "Fake":
                st.markdown(f"""
                    <div class="scan-result-fake">
                        <h2 style="color: #ff003c; margin: 0;">🚨 DETECTED: {prediction.upper()} 🚨</h2>
                        <p style="color: #ccc; margin-top: 10px;">Artificial manipulation identified in media structure.</p>
                        <p class="score-text" style="color: #ff003c;">{confidence * 100:.2f}%</p>
                        <p>Confidence Score</p>
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                    <div class="scan-result-real">
                        <h2 style="color: #008000; margin: 0;">✅ AUTHENTIC ✅</h2>
                        <p style="color: #ccc; margin-top: 10px;">No deepfake artifacts detected in neural scan.</p>
                        <p class="score-text" style="color: #008000;">{confidence * 100:.2f}%</p>
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

        # "Run Temporal" button name changed to professional alternative
        if st.button("ANALYZE TEMPORAL SEQUENCE"):
            
            # Use fixed fast speed for professional video analysis
            progress_bar = st.progress(0)
            for i in range(100):
                time.sleep(0.01)
                progress_bar.progress(i + 1)
            
            status_text = st.empty()
            status_text.markdown("<h4 style='text-align: center; color: #ffbc42;'>Finalizing frames...</h4>", unsafe_allow_html=True)
            time.sleep(1)
            status_text.empty()

            prediction, confidence = predict_dummy()

            if prediction == "Fake":
                st.markdown(f"""
                    <div class="scan-result-fake">
                        <h2 style="color: #ff003c; margin: 0;">🚨 DETECTED: {prediction.upper()} 🚨</h2>
                        <p style="color: #ccc; margin-top: 10px;">Temporal inconsistencies and artificial artifacts identified.</p>
                        <p class="score-text" style="color: #ff003c;">{confidence * 100:.2f}%</p>
                        <p>Confidence Score</p>
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                    <div class="scan-result-real">
                        <h2 style="color: #008000; margin: 0;">✅ AUTHENTIC ✅</h2>
                        <p style="color: #ccc; margin-top: 10px;">Video sequence cleared by neural engine.</p>
                        <p class="score-text" style="color: #008000;">{confidence * 100:.2f}%</p>
                        <p>Confidence Score</p>
                    </div>
                """, unsafe_allow_html=True)

# ===================================
# FOOTER
# ===================================
st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888;'>Forensic AI v2.0 | Encrypted Connection</p>", unsafe_allow_html=True)
