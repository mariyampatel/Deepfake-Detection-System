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
    layout="centered", 
    initial_sidebar_state="expanded"
)

# ===================================
# 2. CYBER-THEMED CUSTOM CSS
# ===================================
st.markdown("""
    <style>
    /* Full Page Navy Blue Background Gradient */
    .stApp {
        background: radial-gradient(circle at center, #0a1931 0%, #00001a 100%);
        color: #e0e1dd;
    }
    
    /* Custom Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #040d21 !important;
        border-right: 2px solid #00FFCC;
        box-shadow: 2px 0 15px rgba(0, 255, 204, 0.2);
    }
    
    .sidebar-title {
        color: #00FFCC;
        font-size: 24px;
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 2px;
        text-shadow: 0 0 10px rgba(0, 255, 204, 0.5);
    }

    /* Typography */
    h1 {
        color: #00FFCC !important;
        font-family: 'Courier New', Courier, monospace;
        text-align: center;
        text-shadow: 0 0 15px rgba(0, 255, 204, 0.6);
        letter-spacing: 3px;
        margin-bottom: 5px;
    }
    
    /* Custom Neon Button */
    div.stButton > button {
        background: rgba(0, 255, 204, 0.05);
        color: #00FFCC;
        border: 1px solid #00FFCC;
        border-radius: 4px;
        padding: 10px 24px;
        font-size: 16px;
        font-weight: bold;
        letter-spacing: 2px;
        text-transform: uppercase;
        width: 100%;
        transition: all 0.3s ease-in-out;
        box-shadow: 0 0 5px rgba(0, 255, 204, 0.2) inset;
    }
    div.stButton > button:hover {
        background: #00FFCC;
        color: #00001a;
        box-shadow: 0 0 20px #00FFCC;
        border-color: #00FFCC;
    }
    
    /* Result Cards */
    .scan-result-fake {
        background: rgba(255, 0, 60, 0.15);
        border: 1px solid #ff003c;
        border-left: 8px solid #ff003c;
        padding: 25px;
        border-radius: 8px;
        text-align: center;
        box-shadow: 0 0 20px rgba(255, 0, 60, 0.3);
    }
    .scan-result-real {
        background: rgba(0, 255, 204, 0.15);
        border: 1px solid #00FFCC;
        border-left: 8px solid #00FFCC;
        padding: 25px;
        border-radius: 8px;
        text-align: center;
        box-shadow: 0 0 20px rgba(0, 255, 204, 0.2);
    }
    .score-text {
        font-size: 3rem;
        font-weight: bold;
        margin: 10px 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }
    
    /* Image container styling */
    [data-testid="stImage"] {
        border-radius: 10px;
        border: 1px solid #00FFCC;
        box-shadow: 0 0 25px rgba(0, 255, 204, 0.15);
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
# 4. SIDEBAR
# ===================================
# A smaller tech image for the sidebar to keep it interesting
st.sidebar.image("https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?auto=format&fit=crop&w=800&q=80", caption="Node: Active")

st.sidebar.markdown('<p class="sidebar-title">Controls</p>', unsafe_allow_html=True)
option = st.sidebar.radio("Targeting Mode:", ["🖼️ Image Scan", "🎥 Video Scan"])

st.sidebar.markdown("---")
st.sidebar.markdown("<p style='color: #00FFCC; font-size: 0.85rem; text-align: center;'>[ System Status: ONLINE ]<br>Uplink: Secure</p>", unsafe_allow_html=True)

# ===================================
# 5. MAIN UI & CENTERED IMAGE
# ===================================
st.title("DEEPFAKE SCANNER")
st.markdown("<p style='text-align: center; color: #8da9c4; font-family: monospace; font-size: 14px; margin-bottom: 20px;'>FORENSIC NEURAL NETWORK INITIALIZED</p>", unsafe_allow_html=True)

# Adding your uploaded image right in the center!
st.image("1000125282.jpg", use_container_width=True, caption="Biometric Mesh Active")

st.markdown("---")

# ===================================
# IMAGE SCANNER
# ===================================
if option == "🖼️ Image Scan":
    
    uploaded_file = st.file_uploader("UPLOAD SUSPECT IMAGE", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        with st.container(border=True):
            st.image(image, caption="Target Acquired", use_container_width=True)

        if st.button("INITIATE SCAN SEQUENCE"):
            
            status_text = st.empty()
            status_text.markdown("<h4 style='text-align: center; color: #ffbc42; font-family: monospace;'>[►] Running facial landmark analysis...</h4>", unsafe_allow_html=True)
            time.sleep(1) 
            status_text.markdown("<h4 style='text-align: center; color: #ffbc42; font-family: monospace;'>[►] Detecting pixel manipulation...</h4>", unsafe_allow_html=True)
            time.sleep(1.5)
            status_text.empty() 

            prediction, confidence = predict_dummy()

            if prediction == "Fake":
                st.markdown(f"""
                    <div class="scan-result-fake">
                        <h2 style="color: #ff003c; margin: 0; font-family: monospace;">🚨 THREAT DETECTED: {prediction.upper()} 🚨</h2>
                        <p style="color: #e0e1dd; margin-top: 10px;">Artificial manipulation identified in media structure.</p>
                        <p class="score-text" style="color: #ff003c;">{confidence * 100:.2f}%</p>
                        <p style="color: #ff003c; font-weight: bold;">CONFIDENCE SCORE</p>
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                    <div class="scan-result-real">
                        <h2 style="color: #00FFCC; margin: 0; font-family: monospace;">✅ MEDIA AUTHENTICATED: {prediction.upper()}</h2>
                        <p style="color: #e0e1dd; margin-top: 10px;">No deepfake artifacts detected in neural scan.</p>
                        <p class="score-text" style="color: #00FFCC;">{confidence * 100:.2f}%</p>
                        <p style="color: #00FFCC; font-weight: bold;">CONFIDENCE SCORE</p>
                    </div>
                """, unsafe_allow_html=True)

# ===================================
# VIDEO SCANNER
# ===================================
elif option == "🎥 Video Scan":
    
    uploaded_video = st.file_uploader("UPLOAD SUSPECT VIDEO", type=["mp4", "mov", "avi"])

    if uploaded_video is not None:
        with st.container(border=True):
            st.video(uploaded_video)

        if st.button("INITIATE FRAME SCAN"):
            
            status_text = st.empty()
            status_text.markdown("<h4 style='text-align: center; color: #ffbc42; font-family: monospace;'>[►] Extracting frames for temporal analysis...</h4>", unsafe_allow_html=True)
            time.sleep(2)
            status_text.empty()

            prediction, confidence = predict_dummy()

            if prediction == "Fake":
                st.markdown(f"""
                    <div class="scan-result-fake">
                        <h2 style="color: #ff003c; margin: 0; font-family: monospace;">🚨 THREAT DETECTED: {prediction.upper()} 🚨</h2>
                        <p style="color: #e0e1dd; margin-top: 10px;">Temporal inconsistencies and artificial artifacts identified.</p>
                        <p class="score-text" style="color: #ff003c;">{confidence * 100:.2f}%</p>
                        <p style="color: #ff003c; font-weight: bold;">CONFIDENCE SCORE</p>
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                    <div class="scan-result-real">
                        <h2 style="color: #00FFCC; margin: 0; font-family: monospace;">✅ MEDIA AUTHENTICATED: {prediction.upper()}</h2>
                        <p style="color: #e0e1dd; margin-top: 10px;">Video sequence cleared by neural engine.</p>
                        <p class="score-text" style="color: #00FFCC;">{confidence * 100:.2f}%</p>
                        <p style="color: #00FFCC; font-weight: bold;">CONFIDENCE SCORE</p>
                    </div>
                """, unsafe_allow_html=True)

# ===================================
# FOOTER
# ===================================
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #4a6fa5; font-size: 12px; font-family: monospace;'>DEEPFAKE FORENSICS v3.0 | SECURE CONNECTION</p>", unsafe_allow_html=True)
