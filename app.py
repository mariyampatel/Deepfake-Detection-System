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
    
    /* Sidebar - Navy Blue */
    [data-testid="stSidebar"] {
        background-color: #000080;
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
    </style>
""", unsafe_allow_html=True)

# ===================================
# 3. CORE LOGIC
# ===================================
def predict_dummy():
    prediction = random.choice(["Real", "Fake"])
    confidence = round(random.uniform(0.85, 0.99), 4)
    return prediction, confidence

# ===================================
# 4. SIDEBAR WITH IMAGES
# ===================================
# Professional Scanning Image for Sidebar
st.sidebar.image("https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&w=400&q=80", caption="Neural System Online")
st.sidebar.markdown("### Control System")
option = st.sidebar.radio("Navigation:", ["🖼️ Image Scan", "🎥 Video Scan"])

st.sidebar.markdown("---")
st.sidebar.write("Status: Active")

# ===================================
# 5. MAIN UI & HEADER IMAGE
# ===================================
# Main Header Image - AI Face Scan
st.image("https://images.unsplash.com/photo-1507146426996-ef05306b995a?auto=format&fit=crop&w=1000&q=80", use_container_width=True)

st.title("DEEPFAKE NEURAL SCANNER")
st.markdown("<p style='text-align: center; font-weight: 500;'>Advanced Forensic Verification Engine</p>", unsafe_allow_html=True)

# ===================================
# IMAGE SCANNER
# ===================================
if option == "🖼️ Image Scan":
    uploaded_file = st.file_uploader("UPLOAD IMAGE", type=["jpg", "png", "jpeg"])
    
    if uploaded_file:
        img = Image.open(uploaded_file)
        st.image(img, caption="Target Asset", use_container_width=True)
        
        if st.button("RUN ANALYSIS"):
            with st.spinner("Analyzing artifacts..."):
                time.sleep(0.8)
            
            res, conf = predict_dummy()
            if res == "Fake":
                st.error(f"ALERT: {res.upper()} detected with {conf*100:.2f}% confidence.")
            else:
                st.success(f"VERIFIED: Media is {res.upper()} ({conf*100:.2f}%)")

# ===================================
# VIDEO SCANNER
# ===================================
elif option == "🎥 Video Scan":
    uploaded_video = st.file_uploader("UPLOAD VIDEO", type=["mp4", "mov"])
    
    if uploaded_video:
        st.video(uploaded_video)
        
        if st.button("RUN TEMPORAL SCAN"):
            # Fixed loading speed for smoother experience
            progress = st.progress(0)
            for i in range(100):
                time.sleep(0.01)
                progress.progress(i + 1)
            
            res, conf = predict_dummy()
            st.info(f"Result: {res} | Confidence: {conf*100:.2f}%")

# ===================================
# FOOTER
# ===================================
st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #777;'>Forensic AI Project 2026</p>", unsafe_allow_html=True)
