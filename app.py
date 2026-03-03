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
# 2. INTENSE ULTRA-DARK UI (EYE-FRIENDLY & VISIBLE)
# ================= ==================
st.markdown("""
    <style>
    /* Global Application Background - Deep Navy */
    .stApp {
        background-color: #0F172A;
        color: #F1F5F9;
    }
    
    /* SIDEBAR */
    [data-testid="stSidebar"] {
        background-color: #111827 !important;
        border-right: 2px solid #00E5FF;
    }
    [data-testid="stSidebar"] *, 
    [data-testid="stSidebar"] label, 
    [data-testid="stSidebar"] p { 
        color: #FFFFFF !important; 
        font-weight: 500;
    }
    [data-testid="stSidebar"] h2 {
        color: #00E5FF !important;
        text-shadow: 0px 0px 12px rgba(0, 229, 255, 0.5);
    }

    /* HERO TITLE - BIGGER */
    .hero-title {
        color: #00E5FF;
        font-size: 100px;  /* Increased */
        font-weight: 900;
        text-align: center;
        letter-spacing: 6px;
        text-transform: uppercase;
        margin-top: 10px;
        margin-bottom: 0px;
        text-shadow: 0px 0px 25px rgba(0, 229, 255, 0.6);
    }

    .hero-subtitle {
        color: #94A3B8;
        text-align: center;
        font-size: 18px;
        letter-spacing: 8px;
        margin-top: -15px;
        margin-bottom: 40px;
    }

    /* HEADER IMAGE */
    .header-img-container {
        display: flex;
        justify-content: center;
        margin-top: 10px;
    }
    .header-img-container img {
        max-width: 18% !important;
        border-radius: 12px;
        border: 2px solid #00E5FF;
        box-shadow: 0px 0px 20px rgba(0, 229, 255, 0.4);
    }

    /* RESULT BOX */
    .result-box {
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        background: rgba(255, 255, 255, 0.04);
        backdrop-filter: blur(8px);
        border: 2px solid #FFFFFF22;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.5);
    }

    .result-text {
        font-size: 34px;
        font-weight: bold;
        text-transform: uppercase;
        margin-bottom: 5px;
    }

    .confidence-text {
        font-size: 18px;
        color: #CBD5E1;
    }

    /* INPUT ACCENTS */
    .stFileUploader label { color: #FFFFFF !important; }
    .stProgress > div > div > div > div { background-color: #00E5FF; }
    
    /* BUTTON */
    div.stButton > button {
        background: transparent;
        color: #00E5FF;
        border: 2px solid #00E5FF;
        border-radius: 6px;
        padding: 12px 20px;
        font-weight: 700;
        transition: 0.3s ease;
        width: 100%;
    }

    div.stButton > button:hover {
        background: #00E5FF;
        color: #000000;
        box-shadow: 0px 0px 18px rgba(0, 229, 255, 0.6);
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
# Restoring previous Sidebar code exactly as requested
with st.sidebar:
    st.markdown("<h2 style='color:#00FF7F;'>TERMINAL</h2>", unsafe_allow_html=True)
    st.image("56387.jpg", use_container_width=True) # Technical Sidebar Image
    
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
# Reusable Result Function (Keeping this from request, looks professional)
def show_final_result(res, conf):
    color = "#FF3B3B" if res == "Fake" else "#00E676"
    icon = "🚨" if res == "Fake" else "✅"
    # Result Box (White/Neon styling)
    st.markdown(f'''
        <div class="result-box" style="border-color: {color}; box-shadow: 0px 0px 20px {color}44;">
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
                st.markdown("### Analysis Terminal")
                if st.button("EXECUTE NEURAL SCAN"):
                    # Scanning Text Animation simulated
                    progress_text = st.empty()
                    # Simulating analysis time
                    with st.spinner("Analyzing frequency artifacts..."):
                        progress_text.text("🧬 Frequency Check: COMPLETE")
                        time.sleep(1)
                    prediction, confidence = predict_dummy()
                    show_final_result(prediction, confidence)

    elif option == "🎥 Video Scan":
        uploaded_video = st.file_uploader("UPLOAD MULTI-FRAME SEQUENCE (MP4)", type=["mp4", "mov"])
        if uploaded_video:
            # Reverting st.video back to simple load for faster stream
            st.video(uploaded_video)
            if st.button("RUN TEMPORAL ANALYSIS"):
                progress_bar = st.progress(0)
                # Video scanning progress
                for i in range(100):
                    time.sleep(0.01)
                    progress_bar.progress(i + 1)
                
                # FINAL RESULT (Real/Fake clear notification)
                # Fixed to also show clear red/green box exactly like image scan
                prediction, confidence = predict_dummy()
                show_final_result(prediction, confidence)

st.markdown("<br><br><p style='text-align:center; color:#555;'>SECURE CHANNEL | ENCRYPTION ACTIVE</p>", unsafe_allow_html=True)

