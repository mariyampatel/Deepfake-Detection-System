import streamlit as st
import random
import time

# ================= ==================
# 1. PAGE CONFIGURATION
# ===================================
st.set_page_config(
    page_title="Deepfake Neural Scanner Pro",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ================= ==================
# 2. PREMIUM LIGHT UI (CLEAN & MODERN)
# ================= ==================
st.markdown("""
    <style>
    /* Global Application Background - Soft Light Gradient (No pure white) */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #F4F7FB 0%, #EAF2FF 100%);
        color: #1E293B;
    }
    
    /* SIDEBAR - Soft Blue with Right Border */
    [data-testid="stSidebar"] {
        background-color: #EDF4FF !important;
        border-right: 2px solid #DCE6F9;
    }
    /* Sidebar Text Styling */
    [data-testid="stSidebar"] *, 
    [data-testid="stSidebar"] label, 
    [data-testid="stSidebar"] p { 
        color: #1E3A8A !important; 
        font-weight: 600;
    }
    [data-testid="stSidebar"] h2 {
        color: #2563EB !important;
        text-shadow: none;
        font-weight: 800;
        letter-spacing: 1px;
    }

    /* HEADER TYPOGRAPHY - Clean Blue Gradient */
    .hero-title {
        background: linear-gradient(to right, #1E3A8A, #2563EB, #00BFA6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 80px; 
        font-weight: 900;
        text-align: center;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-top: 15px;
        margin-bottom: 0px;
        text-shadow: 2px 2px 10px rgba(37, 99, 235, 0.15); /* Soft glow */
    }
    .hero-subtitle {
        color: #64748B;
        text-align: center;
        font-size: 18px;
        letter-spacing: 6px;
        margin-top: -5px;
        margin-bottom: 40px;
        font-weight: 600;
    }

    /* MAIN INTERFACE - RESIZED IMAGE (Made even smaller) */
    .header-img-container {
        display: flex;
        justify-content: center;
        margin-top: 10px;
    }
    .header-img-container img {
        max-width: 8% !important; /* Reduced from 15% to 8% */
        min-width: 80px !important; /* Ensures it doesn't get too small on phones */
        border-radius: 12px;
        border: 2px solid #2563EB;
        box-shadow: 0 4px 15px rgba(37, 99, 235, 0.1);
    }

    /* GLASSMORPHISM CARD FOR RESULTS */
    .result-box {
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        background: rgba(237, 244, 255, 0.7); 
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(37, 99, 235, 0.2);
        box-shadow: 0 8px 32px rgba(31, 38, 135, 0.08);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .result-box:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px rgba(31, 38, 135, 0.12);
    }
    .result-text {
        font-size: 32px;
        font-weight: 800;
        text-transform: uppercase;
        margin-bottom: 5px;
    }
    .confidence-text {
        font-size: 18px;
        color: #334155;
        font-weight: 600;
    }

    /* INPUT ACCENTS (Uploader & Status Bar) */
    .stFileUploader label { color: #1E3A8A !important; font-weight: 700; }
    .stProgress > div > div > div > div { background-color: #00BFA6; } 
    
    /* PREMIUM BUTTON STYLING */
    div.stButton > button {
        background: linear-gradient(135deg, #2563EB 0%, #1E3A8A 100%);
        color: #F4F7FB !important; 
        border: none;
        border-radius: 8px;
        padding: 12px 20px;
        font-weight: 700;
        transition: all 0.3s ease;
        width: 100%;
        box-shadow: 0 4px 10px rgba(37, 99, 235, 0.3);
    }
    div.stButton > button:hover {
        background: linear-gradient(135deg, #1E3A8A 0%, #2563EB 100%);
        color: #EDF4FF !important;
        transform: translateY(-2px);
        box-shadow: 0 6px 15px rgba(37, 99, 235, 0.4);
    }
    </style>
""", unsafe_allow_html=True)

# ================= ==================
# 3. CORE LOGIC (Content Unchanged)
# ===================================
def predict_dummy():
    prediction = random.choice(["Real", "Fake"])
    confidence = round(random.uniform(0.75, 0.99), 4)
    return prediction, confidence

# ================= ==================
# 4. SIDEBAR TERMINAL
# ================= ==================
with st.sidebar:
    st.markdown("<h2>TERMINAL</h2>", unsafe_allow_html=True)
    st.image("56387.jpg", use_container_width=True) 
    
    st.markdown("<br>", unsafe_allow_html=True)
    option = st.radio("SELECT MODE:", ["🖼️ Image Scan", "🎥 Video Scan"])
    
    st.markdown("---")
    st.write("🛰️ **LINK:** SECURE")
    st.write("🧠 **NEURAL:** v4.0-PRO")

# ================= ==================
# 5. HOME PAGE UI
# ================= ==================
# Top Image Banner (Image First, chota)
st.markdown('<div class="header-img-container">', unsafe_allow_html=True)
st.image("image.jpg.jpeg") 
st.markdown('</div>', unsafe_allow_html=True)

# Main Title (Niche, bada)
st.markdown('<p class="hero-title">Neural Scanner Pro</p>', unsafe_allow_html=True)
st.markdown('<p class="hero-subtitle">ADVANCED DEEPFAKE DETECTION</p>', unsafe_allow_html=True)

# ================= ==================
# 6. ANALYSIS SECTION
# ================= ==================
# Reusable Result Function (Updated colors to requested theme)
def show_final_result(res, conf):
    # Updated to requested Theme colors: Danger (#EF4444) and Success (#10B981)
    color = "#EF4444" if
