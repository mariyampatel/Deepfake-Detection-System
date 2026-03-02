import streamlit as st
import random
import time
import math
from PIL import Image

# ===================================
# PAGE CONFIG
# ===================================
st.set_page_config(
    page_title="DeepGuard AI | Enterprise Deepfake Detection",
    page_icon="🛡️",
    layout="wide"
)

# ===================================
# CUSTOM CSS — Corporate Light Theme
# ===================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Roboto+Mono:wght@400;500&display=swap');

    /* Global App Styling */
    html, body, [class*="css"] { 
        font-family: 'Inter', sans-serif; 
        color: #1e293b;
    }
    .stApp {
        background-color: #f8fafc;
        background-image: none; /* Clean corporate background */
    }

    /* ── Sidebar ── */
    [data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #e2e8f0;
    }
    .sidebar-logo-container {
        padding: 10px 0 20px 0;
        text-align: center;
        border-bottom: 1px solid #e2e8f0;
        margin-bottom: 20px;
    }
    .sidebar-logo-text {
        font-size: 1.4rem; font-weight: 700; color: #0f172a;
        letter-spacing: -0.5px;
    }

    /* ── Headers & Typography ── */
    h1, h2, h3 { color: #0f172a !important; font-weight: 700 !important; letter-spacing: -0.5px; }
    .mono-text { font-family: 'Roboto Mono', monospace; }

    /* ── Hero Banner ── */
    .hero-container {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 40px;
        margin-bottom: 30px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    .hero-text-area { max-width: 60%; }
    .hero-badge {
        display: inline-block;
        background: #eff6ff;
        color: #2563eb;
        font-size: 0.75rem; font-weight: 600;
        padding: 4px 12px; border-radius: 20px;
        margin-bottom: 16px; border: 1px solid #bfdbfe;
    }
    .hero-title {
        font-size: 2.5rem; font-weight: 800; color: #0f172a;
        margin: 0 0 16px 0; line-height: 1.2;
    }
    .hero-subtitle {
        font-size: 1.1rem; color: #475569; line-height: 1.6;
        margin-bottom: 0;
    }

    /* ── Cards & Panels ── */
    .panel {
        background: #ffffff; border: 1px solid #e2e8f0;
        border-radius: 12px; padding: 24px;
        box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.05);
        margin-bottom: 20px;
    }
    .sec-head { font-size: 1.25rem; font-weight: 600; color: #0f172a; border-bottom: 2px solid #f1f5f9; padding-bottom: 10px; margin-bottom: 20px; }

    /* ── Buttons ── */
    .stButton > button {
        background-color: #0f172a !important;
        color: #ffffff !important;
        font-weight: 500 !important;
        border-radius: 6px !important;
        padding: 10px 24px !important;
        border: none !important;
        transition: all 0.2s ease;
    }
    .stButton > button:hover {
        background-color: #334155 !important;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1) !important;
    }

    /* ── Status Metrics ── */
    .metric-box {
        background: #f8fafc; border: 1px solid #e2e8f0;
        border-radius: 8px; padding: 16px;
        text-align: center;
    }
    .metric-value { font-size: 1.5rem; font-weight: 700; color: #0f172a; font-family: 'Roboto Mono', monospace; }
    .metric-label { font-size: 0.75rem; font-weight: 600; color: #64748b; text-transform: uppercase; letter-spacing: 0.5px; margin-top: 4px; }

    /* ── Upload Area ── */
    [data-testid="stFileUploader"] {
        background-color: #fafafa !important;
        border: 1px dashed #cbd5e1 !important;
        border-radius: 8px !important;
        padding: 20px !important;
    }

    /* Footer */
    .footer {
        text-align: center; color: #94a3b8; font-size: 0.8rem;
        padding: 20px 0; border-top: 1px solid #e2e8f0;
        margin-top: 40px; font-family: 'Inter', sans-serif;
    }
    </style>
""", unsafe_allow_html=True)


# ===================================
# MOCK PREDICTION & VIZ HELPER FUNCTIONS
# ===================================
def predict_dummy():
    prediction = random.choice(["Real", "Fake"])
    confidence = round(random.uniform(0.75, 0.99), 4)
    return prediction, confidence

def render_corporate_metrics(prediction, confidence):
    """Renders sleek, corporate-style metric bars"""
    is_fake = prediction == "Fake"
    rng = random.Random(int(confidence * 1000))

    metrics = [
        ("Facial Landmark Consistency", f"{round(rng.uniform(70,85) if is_fake else rng.uniform(96,99), 1)}%"),
        ("Noise Pattern Analysis", "Irregular" if is_fake else "Standard"),
        ("Compression Artifacts", "Detected" if is_fake else "Clear")
    ]
    
    html = '<div style="margin-top:20px; font-family: Inter, sans-serif;">'
    for label, val in metrics:
        html += f'''
        <div style="display:flex; justify-content:space-between; padding: 10px 0; border-bottom: 1px solid #e2e8f0;">
            <span style="color:#475569; font-size: 0.85rem;">{label}</span>
            <span style="color:#0f172a; font-weight: 600; font-size: 0.85rem;">{val}</span>
        </div>
        '''
    html += '</div>'
    st.markdown(html, unsafe_allow_html=True)


# ===================================
# SIDEBAR
# ===================================
with st.sidebar:
    st.markdown("""
        <div class="sidebar-logo-container">
            <div class="sidebar-logo-text">DeepGuard AI</div>
            <div style="font-size: 0.75rem; color: #64748b; margin-top: 4px;">Enterprise Authentication</div>
        </div>
    """, unsafe_allow_html=True)

    analysis_mode = st.radio("Select Analysis Engine", ["Image Analysis", "Video Analysis"])
    option = "Image" if "Image" in analysis_mode else "Video"

    st.markdown("<br>", unsafe_allow_html=True)
    st.info("ℹ️ System Status: Online\n\nModel Version: v4.2.0-Enterprise\n\nLatency: 42ms")


# ===================================
# HERO SECTION (PROFESSIONAL LAYOUT)
# ===================================
col_hero_text, col_hero_img = st.columns([3, 2])

with col_hero_text:
    st.markdown("""
        <div style="padding: 20px 0 40px 0;">
            <div class="hero-badge">Enterprise Edition</div>
            <h1 class="hero-title">Media Authentication <br> & Deepfake Detection</h1>
            <p class="hero-subtitle">
                Secure your digital ecosystem with our state-of-the-art neural analysis engine. 
                Upload media below to instantly verify authenticity and detect AI manipulation with clinical precision.
            </p>
        </div>
    """, unsafe_allow_html=True)

with col_hero_img:
    # Adding a professional stock image placeholder instead of CSS emojis
    st.image("https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&w=800&q=80", use_container_width=True)


# ===================================
# MAIN UI: IMAGE OR VIDEO SECTION
# ===================================
if option == "Image":
    st.markdown('<div class="sec-head">Image Verification Engine</div>', unsafe_allow_html=True)

    col_upload, col_result = st.columns([1, 1], gap="large")

    with col_upload:
        st.markdown('<div class="panel">', unsafe_allow_html=True)
        st.write("**Upload Suspect Image** (JPG, PNG)")
        
        uploaded_file = st.file_uploader("", type=["jpg","jpeg","png"], label_visibility="collapsed")

        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, use_container_width=True, caption="Source Media")

            if st.button("Initialize Scan Sequence", key="img_btn"):
                pb = st.progress(0, text="Initializing...")
                for i in range(100):
                    time.sleep(0.02)
                    pb.progress(i + 1, text="Analyzing pixel topology...")
                pb.empty()

                prediction, confidence = predict_dummy()
                st.session_state['img_result'] = (prediction, confidence)

        st.markdown('</div>', unsafe_allow_html=True)

    with col_result:
        st.markdown('<div class="panel">', unsafe_allow_html=True)
        st.write("**Analysis Report**")
        
        if 'img_result' in st.session_state and uploaded_file is not None:
            pred, conf = st.session_state['img_result']
            is_fake = pred == "Fake"
            
            # Professional Status Banner
            status_color = "#ef4444" if is_fake else "#10b981"
            status_text = "SYNTHETIC MEDIA DETECTED" if is_fake else "AUTHENTIC MEDIA VERIFIED"
            
            st.markdown(f"""
                <div style="background-color: {status_color}15; border-left: 4px solid {status_color}; padding: 16px; margin-bottom: 20px; border-radius: 4px;">
                    <strong style="color: {status_color}; font-size: 1.1rem; letter-spacing: 0.5px;">{status_text}</strong>
                </div>
            """, unsafe_allow_html=True)

            # Metrics
            mc1, mc2 = st.columns(2)
            with mc1:
                st.markdown(f'<div class="metric-box"><div class="metric-value" style="color:{status_color}">{conf*100:.1f}%</div><div class="metric-label">Confidence Score</div></div>', unsafe_allow_html=True)
            with mc2:
                risk = "High" if is_fake else "Low"
                st.markdown(f'<div class="metric-box"><div class="metric-value">{risk}</div><div class="metric-label">Risk Assessment</div></div>', unsafe_allow_html=True)

            # Professional Corporate Metrics
            render_corporate_metrics(pred, conf)
            
            # Placeholders for actual data charts
            st.markdown("<br><p style='font-size: 0.8rem; color: #64748b; font-weight: 600;'>FORENSIC HEATMAP PREVIEW</p>", unsafe_allow_html=True)
            st.image("https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=800&q=80", use_container_width=True)

        else:
            st.markdown("""
                <div style="text-align: center; padding: 40px 20px; color: #94a3b8;">
                    <p>No media analyzed yet.</p>
                    <p style="font-size: 0.85rem;">Upload an image on the left and initiate the scan to view forensic reports here.</p>
                </div>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

elif option == "Video":
    st.markdown('<div class="sec-head">Video Verification Engine</div>', unsafe_allow_html=True)
    st.info("Video streaming and frame-by-frame analysis module initialized. Awaiting input.")
    
    uploaded_video = st.file_uploader("Upload Suspect Video (MP4, MOV)", type=["mp4","mov","avi"])
    
    if uploaded_video is not None:
        st.video(uploaded_video)
        if st.button("Initialize Frame-by-Frame Scan", key="vid_btn"):
            st.success("Analysis complete. Check the generated PDF report in your enterprise dashboard.")


# ===================================
# FOOTER
# ===================================
st.markdown("""
    <div class="footer">
        © 2026 DeepGuard AI Enterprise Solutions &nbsp;·&nbsp; Privacy Policy &nbsp;·&nbsp; Terms of Service
    </div>
""", unsafe_allow_html=True)
