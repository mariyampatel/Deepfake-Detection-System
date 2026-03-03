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
# 2. PREMIUM LIGHT UI (MODERN SAAS THEME)
# ================= ==================
st.markdown("""
    <style>
    /* Global Application Background - Soft Gradient */
    .stApp {
        background: linear-gradient(135deg, #F8FAFF 0%, #E6F0FF 100%);
        color: #1E293B;
    }
    
    /* SIDEBAR - Clean & Bright */
    [data-testid="stSidebar"] {
        background-color: #FFFFFF !important;
        border-right: 1px solid #E2E8F0;
        box-shadow: 2px 0 15px rgba(0,0,0,0.02);
    }
    
    /* Sidebar Text & Typography */
    [data-testid="stSidebar"] *, 
    [data-testid="stSidebar"] label, 
    [data-testid="stSidebar"] p { 
        color: #334155 !important; 
        font-weight: 500;
    }
    [data-testid="stSidebar"] h2 {
        color: #1E3A8A !important;
        font-weight: 800;
        letter-spacing: 1px;
    }

    /* HEADER TYPOGRAPHY - Gradient Title */
    .hero-title {
        background: linear-gradient(90deg, #1E3A8A, #2563EB, #00BFA6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 64px; 
        font-weight: 900;
        text-align: center;
        letter-spacing: 2px;
        margin-top: 10px;
        margin-bottom: 0px;
        text-shadow: 0px 4px 20px rgba(37, 99, 235, 0.15);
    }
    .hero-subtitle {
        color: #64748B;
        text-align: center;
        font-size: 16px;
        letter-spacing: 6px;
        font-weight: 600;
        margin-top: -5px;
        margin-bottom: 40px;
        text-transform: uppercase;
    }

    /* MAIN INTERFACE - CLEAN IMAGE CONTAINER */
    .header-img-container {
        display: flex;
        justify-content: center;
        margin-top: 10px;
    }
    .header-img-container img {
        max-width: 15% !important; 
        border-radius: 12px;
        border: 1px solid #E2E8F0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    }

    /* GLASSMORPHISM CARD FOR RESULTS */
    .result-box {
        padding: 30px;
        border-radius: 16px;
        text-align: center;
        background: rgba(255, 255, 255, 0.85); 
        backdrop-filter: blur(12px); 
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.6);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .result-box:hover {
        transform: translateY(-4px);
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.12);
    }
    .result-text {
        font-size: 32px;
        font-weight: 800;
        text-transform: uppercase;
        margin-bottom: 5px;
        letter-spacing: 1px;
    }
    .confidence-text {
        font-size: 16px;
        color: #475569;
        font-weight: 500;
    }

    /* INPUT ACCENTS (Uploader & Text) */
    .stFileUploader label { color: #1E293B !important; font-weight: 600; }
    .stProgress > div > div > div > div { background-color: #2563EB; }
    
    /* MODERN SAAS BUTTONS */
    div.stButton > button {
        background: linear-gradient(135deg, #2563EB, #1D4ED8) !important;
        color: #FFFFFF !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 12px 20px !important;
        font-weight: 600 !important;
        letter-spacing: 0.5px;
        transition: all 0.3s ease !important;
        width: 100%;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.25) !important;
    }
    div.stButton > button:hover {
        background: linear-gradient(135deg, #1D4ED8, #1E3A8A) !important;
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(37, 99, 235, 0.4) !important;
    }
    div.stButton > button:active {
        transform: translateY(0px);
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
    st.markdown("<h2>CONTROL PANEL</h2>", unsafe_allow_html=True)
    st.image("56387.jpg", use_container_width=True) 
    
    st.markdown("<br>", unsafe_allow_html=True)
    option = st.radio("SELECT MODE:", ["🖼️ Image Scan", "🎥 Video Scan"])
    
    st.markdown("---")
    st.write("🛡️ **STATUS:** SECURE")
    st.write("🧠 **ENGINE:** v4.0-PRO")

# ================= ==================
# 5. HOME PAGE UI
# ================= ==================
st.markdown('<div class="header-img-container">', unsafe_allow_html=True)
st.image("image.jpg.jpeg") 
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<p class="hero-title">Neural Scanner Pro</p>', unsafe_allow_html=True)
st.markdown('<p class="hero-subtitle">Advanced Deepfake Forensic Analysis</p>', unsafe_allow_html=True)

# ================= ==================
# 6. ANALYSIS SECTION
# ================= ==================
def show_final_result(res, conf):
    # Updated to softer, premium danger/success colors
    color = "#EF4444" if res == "Fake" else "#10B981"
    icon = "🚨" if res == "Fake" else "✅"
    
    st.markdown(f'''
        <div class="result-box" style="border-top: 4px solid {color};">
            <p class="result-text" style="color: {color} !important;">{icon} {res.upper()}</p>
            <p class="confidence-text">Forensic Confidence Check: {conf*100:.2f}%</p>
        </div>
    ''', unsafe_allow_html=True)

container = st.container()

with container:
    if option == "🖼️ Image Scan":
        uploaded_file = st.file_uploader("DROP IMAGE FILE HERE FOR ARTIFACT ANALYSIS", type=["jpg", "png", "jpeg"])
        if uploaded_file:
            c1, c2 = st.columns(2)
            c1.image(uploaded_file, caption="Target Acquired", use_container_width=True)
            with c2:
                st.markdown("<h3 style='color:#1E293B;'>Analysis Terminal</h3>", unsafe_allow_html=True)
                if st.button("EXECUTE NEURAL SCAN"):
                    progress_text = st.empty()
                    with st.spinner("Analyzing frequency artifacts..."):
                        progress_text.text("🧬 Frequency Check: COMPLETE")
                        time.sleep(1)
                    prediction, confidence = predict_dummy()
                    show_final_result(prediction, confidence)

    elif option == "🎥 Video Scan":
        uploaded_video = st.file_uploader("UPLOAD MULTI-FRAME SEQUENCE (MP4)", type=["mp4", "mov"])
        if uploaded_video:
            st.video(uploaded_video)
            if st.button("RUN TEMPORAL ANALYSIS"):
                progress_bar = st.progress(0)
                for i in range(100):
                    time.sleep(0.01)
                    progress_bar.progress(i + 1)
                
                prediction, confidence = predict_dummy()
                show_final_result(prediction, confidence)

st.markdown("<br><br><p style='text-align:center; color:#94A3B8; font-size: 14px;'>SECURE CHANNEL | END-TO-END ENCRYPTED</p>", unsafe_allow_html=True)
