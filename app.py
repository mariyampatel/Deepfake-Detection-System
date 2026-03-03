import streamlit as st
import random
from PIL import Image
import time
import base64

# ===================================
# 1. PAGE CONFIGURATION
# ===================================
st.set_page_config(
    page_title="Deepfake Neural Scanner",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ================= ==================
# 2. NEON CYBER-DARK THEME (EYE-FRIENDLY)
# ===================================
st.markdown("""
    <style>
    /* Main Background - Deep Charcoal for no eye strain */
    .stApp {
        background-color: #0B0E14;
        color: #E0E0E0;
    }
    
    /* Sidebar - Professional Dark Grey */
    [data-testid="stSidebar"] {
        background-color: #12161D;
        border-right: 1px solid #1E2530;
    }

    /* Titles - Matching the Neon Green from your image */
    h1, h2, h3 {
        color: #00FF7F !important; /* Spring Green */
        font-family: 'Courier New', Courier, monospace;
        text-transform: uppercase;
        letter-spacing: 2px;
        text-shadow: 0px 0px 10px rgba(0, 255, 127, 0.3);
    }

    /* Professional Glassmorphism Cards */
    .stFileUploader, .stMarkdown, div[data-testid="stVerticalBlock"] > div {
        border-radius: 10px;
    }

    /* Custom Scan Button - Matrix Style */
    div.stButton > button {
        background: transparent;
        color: #00FF7F;
        border: 2px solid #00FF7F;
        border-radius: 4px;
        padding: 12px 20px;
        font-weight: 700;
        transition: 0.3s;
        width: 100%;
        box-shadow: 0px 0px 15px rgba(0, 255, 127, 0.1);
    }
    div.stButton > button:hover {
        background: #00FF7F;
        color: #000000;
        box-shadow: 0px 0px 25px rgba(0, 255, 127, 0.4);
    }

    /* Status Alerts */
    .scan-result-fake {
        background: rgba(255, 46, 99, 0.1);
        border: 1px solid #FF2E63;
        padding: 20px;
        border-radius: 8px;
        color: #FF2E63;
        text-align: center;
    }
    .scan-result-real {
        background: rgba(0, 255, 127, 0.1);
        border: 1px solid #00FF7F;
        padding: 20px;
        border-radius: 8px;
        color: #00FF7F;
        text-align: center;
    }

    /* Smooth Progress Bar */
    .stProgress > div > div > div > div {
        background-color: #00FF7F;
    }
    </style>
""", unsafe_allow_html=True)

# ===================================
# 3. CORE LOGIC (Content Unchanged)
# ===================================
def predict_dummy():
    prediction = random.choice(["Real", "Fake"])
    confidence = round(random.uniform(0.75, 0.99), 4)
    return prediction, confidence

# ===================================
# 4. SIDEBAR (Professional Layout)
# ===================================
with st.sidebar:
    st.markdown("<h2 style='text-align: left; font-size: 22px;'>SYSTEM TERMINAL</h2>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&w=800&q=80", caption="Neural Core Active")
    
    st.markdown("---")
    option = st.radio("TARGETING MODE:", ["🖼️ Image Scan", "🎥 Video Scan"])
    
    st.markdown("---")
    st.info("Artifact Density: 0.02\n\nMotion Check: Normal")

# ===================================
# 5. HOME PAGE & HEADER (Using Your Image Style)
# ===================================

# Hero Header Section
col1, col2, col3 = st.columns([1, 6, 1])
with col2:
    # Aapki provided image ko yahan display kar rahe hain header ki tarah
    # Note: Make sure image file is in same folder or use URL
    st.image("image.jpg.jpeg", use_container_width=True) 
    
    st.title("DEEPFAKE NEURAL SCANNER")
    st.markdown("<p style='text-align: center; color: #888; margin-top: -20px;'>FORENSIC ANALYSIS ENGINE V2.0</p>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ===================================
# 6. ANALYSIS SECTION
# ===================================
container = st.container()

with container:
    if option == "🖼️ Image Scan":
        uploaded_file = st.file_uploader("UPLOAD TARGET IMAGE FOR ARTIFACT ANALYSIS", type=["jpg", "jpeg", "png"])
        
        if uploaded_file:
            c1, c2 = st.columns([1, 1])
            with c1:
                st.image(uploaded_file, caption="Target Acquired", use_container_width=True)
            with c2:
                st.markdown("<h3 style='text-align: left;'>Analysis Terminal</h3>", unsafe_allow_html=True)
                st.write("Initializing facial mesh...")
                if st.button("INITIATE SCAN"):
                    with st.spinner("Decoding pixels..."):
                        time.sleep(1.5)
                    prediction, confidence = predict_dummy()
                    
                    if prediction == "Fake":
                        st.markdown(f'<div class="scan-result-fake"><h2>🚨 {prediction.upper()} DETECTED</h2><p>Confidence: {confidence*100:.2f}%</p></div>', unsafe_allow_html=True)
                    else:
                        st.markdown(f'<div class="scan-result-real"><h2>✅ AUTHENTIC</h2><p>Confidence: {confidence*100:.2f}%</p></div>', unsafe_allow_html=True)

    elif option == "🎥 Video Scan":
        uploaded_video = st.file_uploader("UPLOAD VIDEO SEQUENCE", type=["mp4", "mov"])
        if uploaded_video:
            st.video(uploaded_video)
            if st.button("ANALYZE TEMPORAL SEQUENCE"):
                progress = st.progress(0)
                for i in range(100):
                    time.sleep(0.02)
                    progress.progress(i + 1)
                prediction, confidence = predict_dummy()
                
                if prediction == "Fake":
                    st.error(f"ALERT: Temporal anomalies detected! Result: {prediction} ({confidence*100:.2f}%)")
                else:
                    st.success(f"SUCCESS: Pattern consistency verified. Result: {prediction} ({confidence*100:.2f}%)")

# Footer
st.markdown("<br><br><p style='text-align: center; color: #444; font-size: 12px;'>SECURITY LEVEL: ALPHA-ST-7 | ENCRYPTION: ACTIVE</p>", unsafe_allow_html=True)
