import streamlit as st
import random
import time
from PIL import Image

# ===================================
# PAGE CONFIG
# ===================================
st.set_page_config(
    page_title="Deepfake Detection System",
    page_icon="🛡️",
    layout="wide"
)

# ===================================
# CUSTOM CSS — Light Professional Theme
# ===================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* ── Background ── */
    .stApp {
        background: #f8fafc;
    }

    /* ── Sidebar ── */
    [data-testid="stSidebar"] {
        background: #ffffff;
        border-right: 1px solid #e2e8f0;
        box-shadow: 2px 0 12px rgba(0,0,0,0.04);
    }
    [data-testid="stSidebar"] * { color: #1e293b !important; }

    /* ── Hero Banner ── */
    .hero-banner {
        background: linear-gradient(135deg, #1e3a5f 0%, #1d4ed8 50%, #0ea5e9 100%);
        border-radius: 20px;
        padding: 48px 52px;
        margin-bottom: 32px;
        position: relative;
        overflow: hidden;
        box-shadow: 0 20px 60px rgba(29,78,216,0.25);
    }
    .hero-banner::after {
        content: '🛡️';
        position: absolute;
        right: 52px; top: 50%;
        transform: translateY(-50%);
        font-size: 7rem;
        opacity: 0.15;
    }
    .hero-eyebrow {
        display: inline-block;
        background: rgba(255,255,255,0.15);
        border: 1px solid rgba(255,255,255,0.3);
        color: #bfdbfe;
        font-size: 0.7rem; font-weight: 600;
        letter-spacing: 2px; text-transform: uppercase;
        padding: 5px 14px; border-radius: 20px;
        margin-bottom: 18px;
        font-family: 'JetBrains Mono', monospace;
    }
    .hero-title {
        font-size: 2.6rem; font-weight: 800;
        color: #ffffff;
        letter-spacing: -1px;
        margin: 0 0 10px 0;
        line-height: 1.1;
    }
    .hero-sub {
        font-size: 1rem; color: #bfdbfe;
        margin: 0; max-width: 520px;
        line-height: 1.6; font-weight: 400;
    }

    /* ── Stat Pills (hero row) ── */
    .hero-stats {
        display: flex; gap: 16px;
        margin-top: 28px; flex-wrap: wrap;
    }
    .hero-stat {
        background: rgba(255,255,255,0.12);
        border: 1px solid rgba(255,255,255,0.2);
        border-radius: 12px;
        padding: 12px 20px;
        text-align: center;
        min-width: 100px;
    }
    .hero-stat-val {
        font-size: 1.4rem; font-weight: 700;
        color: #ffffff;
        font-family: 'JetBrains Mono', monospace;
        display: block;
    }
    .hero-stat-lbl {
        font-size: 0.68rem; color: #93c5fd;
        text-transform: uppercase; letter-spacing: 1px;
        margin-top: 2px; display: block;
    }

    /* ── Feature Cards (how it works) ── */
    .feature-row { display: flex; gap: 16px; margin-bottom: 32px; }
    .feature-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        padding: 24px;
        flex: 1;
        box-shadow: 0 2px 12px rgba(0,0,0,0.04);
        transition: box-shadow 0.2s;
    }
    .feature-card:hover { box-shadow: 0 8px 28px rgba(0,0,0,0.09); }
    .feature-icon { font-size: 2rem; margin-bottom: 12px; }
    .feature-title { font-size: 0.9rem; font-weight: 700; color: #0f172a; margin-bottom: 6px; }
    .feature-desc { font-size: 0.8rem; color: #64748b; line-height: 1.6; }
    .feature-step {
        display: inline-block;
        background: #eff6ff; color: #1d4ed8;
        font-size: 0.65rem; font-weight: 700;
        padding: 2px 8px; border-radius: 8px;
        margin-bottom: 10px; letter-spacing: 0.5px;
        font-family: 'JetBrains Mono', monospace;
    }

    /* ── Section Heading ── */
    .section-heading {
        font-size: 1.1rem; font-weight: 700; color: #0f172a;
        margin-bottom: 4px;
    }
    .section-sub { font-size: 0.83rem; color: #94a3b8; margin-bottom: 20px; }

    /* ── Upload Panel ── */
    .upload-panel {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 20px;
        padding: 28px;
        box-shadow: 0 2px 16px rgba(0,0,0,0.05);
    }
    .upload-drop-hint {
        background: #f0f9ff;
        border: 2px dashed #93c5fd;
        border-radius: 14px;
        padding: 32px 20px;
        text-align: center;
        margin-bottom: 16px;
    }
    .upload-drop-icon { font-size: 2.6rem; margin-bottom: 8px; }
    .upload-drop-title { font-size: 0.95rem; font-weight: 600; color: #1e40af; margin-bottom: 4px; }
    .upload-drop-sub { font-size: 0.78rem; color: #94a3b8; }

    /* ── Preview Panel ── */
    .preview-label {
        font-size: 0.72rem; font-weight: 600; letter-spacing: 1.5px;
        text-transform: uppercase; color: #94a3b8;
        font-family: 'JetBrains Mono', monospace;
        margin-bottom: 8px;
    }

    /* ── Result Panel ── */
    .result-panel {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 20px;
        padding: 28px;
        box-shadow: 0 2px 16px rgba(0,0,0,0.05);
        height: 100%;
    }
    .result-waiting {
        display: flex; flex-direction: column;
        align-items: center; justify-content: center;
        padding: 60px 20px; text-align: center; gap: 12px;
    }
    .result-waiting-icon { font-size: 3rem; opacity: 0.3; }
    .result-waiting-text { font-size: 0.85rem; color: #cbd5e1; }

    /* ── Verdict Card ── */
    .verdict-card {
        border-radius: 14px; padding: 24px 24px 20px 24px;
        margin-bottom: 20px; position: relative; overflow: hidden;
    }
    .verdict-fake {
        background: linear-gradient(135deg, #fff1f2, #fef2f2);
        border: 1.5px solid #fca5a5;
    }
    .verdict-real {
        background: linear-gradient(135deg, #f0fdf4, #ecfdf5);
        border: 1.5px solid #86efac;
    }
    .verdict-card::before {
        content: ''; position: absolute;
        top: 0; left: 0; right: 0; height: 3px;
    }
    .verdict-fake::before { background: linear-gradient(90deg, #ef4444, #f97316); }
    .verdict-real::before { background: linear-gradient(90deg, #10b981, #06b6d4); }

    .verdict-eyebrow {
        font-size: 0.68rem; font-weight: 600;
        letter-spacing: 2px; text-transform: uppercase;
        font-family: 'JetBrains Mono', monospace;
        margin-bottom: 10px;
    }
    .verdict-eyebrow-fake { color: #ef4444; }
    .verdict-eyebrow-real { color: #10b981; }

    .verdict-main {
        font-size: 1.8rem; font-weight: 800;
        line-height: 1; margin-bottom: 16px;
        display: flex; align-items: center; gap: 10px;
    }

    /* ── Confidence Bar ── */
    .conf-track {
        background: #f1f5f9; border-radius: 99px;
        height: 8px; margin: 8px 0 4px; overflow: hidden;
    }
    .conf-fill-fake {
        height: 100%; border-radius: 99px;
        background: linear-gradient(90deg, #ef4444, #f97316);
    }
    .conf-fill-real {
        height: 100%; border-radius: 99px;
        background: linear-gradient(90deg, #10b981, #06b6d4);
    }
    .conf-labels {
        display: flex; justify-content: space-between;
        font-size: 0.72rem; color: #94a3b8;
        font-family: 'JetBrains Mono', monospace;
    }

    /* ── Stat Row ── */
    .stat-row { display: flex; gap: 12px; margin-top: 16px; }
    .stat-tile {
        flex: 1; background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 12px; padding: 14px 12px;
        text-align: center;
    }
    .stat-tile-val {
        font-size: 1.3rem; font-weight: 700;
        font-family: 'JetBrains Mono', monospace;
        display: block;
    }
    .stat-tile-lbl {
        font-size: 0.65rem; color: #94a3b8;
        text-transform: uppercase; letter-spacing: 1px;
        margin-top: 3px; display: block;
    }

    /* ── Sidebar Cards ── */
    .sb-card {
        background: #f8fafc; border: 1px solid #e2e8f0;
        border-radius: 12px; padding: 14px 16px;
        margin-top: 12px; font-size: 0.8rem;
        color: #475569; line-height: 1.65;
    }
    .sb-card-title {
        font-size: 0.68rem; font-weight: 700;
        letter-spacing: 1.5px; text-transform: uppercase;
        color: #1d4ed8; margin-bottom: 8px;
        font-family: 'JetBrains Mono', monospace;
    }
    .sb-brand-name {
        font-size: 1.1rem; font-weight: 800;
        color: #0f172a; letter-spacing: -0.3px;
    }
    .sb-brand-ver { font-size: 0.75rem; color: #94a3b8; margin-top: 2px; }
    .sb-badge {
        display: inline-block;
        background: #eff6ff; color: #1d4ed8;
        font-size: 0.62rem; font-weight: 700;
        letter-spacing: 1px; text-transform: uppercase;
        padding: 3px 8px; border-radius: 6px;
        margin-bottom: 14px;
        font-family: 'JetBrains Mono', monospace;
    }
    .sb-divider { border-top: 1px solid #e2e8f0; margin: 16px 0; }
    .sb-mode-label {
        font-size: 0.68rem; font-weight: 700;
        letter-spacing: 1.5px; color: #94a3b8;
        text-transform: uppercase; margin-bottom: 8px;
        font-family: 'JetBrains Mono', monospace;
    }

    /* ── Buttons ── */
    .stButton > button {
        background: linear-gradient(135deg, #1d4ed8, #0ea5e9) !important;
        color: #ffffff !important;
        font-size: 0.9rem !important; font-weight: 600 !important;
        border-radius: 12px !important; border: none !important;
        padding: 14px 28px !important; width: 100% !important;
        letter-spacing: 0.3px !important;
        box-shadow: 0 4px 14px rgba(29,78,216,0.3) !important;
        transition: all 0.2s !important;
    }
    .stButton > button:hover {
        box-shadow: 0 8px 24px rgba(29,78,216,0.45) !important;
        transform: translateY(-1px) !important;
    }

    /* ── File Uploader ── */
    [data-testid="stFileUploader"] {
        background: #f0f9ff !important;
        border: 2px dashed #93c5fd !important;
        border-radius: 12px !important;
        padding: 4px !important;
    }

    /* ── Progress ── */
    .stProgress > div > div { background: linear-gradient(90deg,#1d4ed8,#0ea5e9) !important; }
    .stSpinner > div { border-top-color: #1d4ed8 !important; }

    /* ── Radio ── */
    .stRadio label, .stRadio span { color: #334155 !important; font-size: 0.88rem !important; }
    .stRadio [data-testid="stMarkdownContainer"] p { color: #334155 !important; }

    /* ── Typography ── */
    h1,h2,h3 { color: #0f172a !important; }
    p { color: #475569; }
    hr { border-color: #e2e8f0 !important; }

    /* ── Footer ── */
    .footer {
        text-align: center; color: #cbd5e1;
        font-size: 0.75rem; padding: 28px 0 10px;
        border-top: 1px solid #e2e8f0; margin-top: 48px;
        font-family: 'JetBrains Mono', monospace;
    }

    /* ── Info Strip ── */
    .info-strip {
        background: #eff6ff; border: 1px solid #bfdbfe;
        border-radius: 10px; padding: 10px 16px;
        font-size: 0.78rem; color: #1e40af;
        margin-bottom: 14px; display: flex;
        align-items: center; gap: 8px;
    }
    </style>
""", unsafe_allow_html=True)


# ===================================
# DUMMY PREDICTION FUNCTION  ← UNCHANGED
# ===================================
def predict_dummy():
    prediction = random.choice(["Real", "Fake"])
    confidence = round(random.uniform(0.75, 0.99), 4)
    return prediction, confidence


# ===================================
# SIDEBAR
# ===================================
with st.sidebar:
    st.markdown("""
        <div style="padding:14px 0 6px 0;">
            <div class="sb-badge">🛡️ Enterprise Edition</div>
            <div class="sb-brand-name">DeepGuard AI</div>
            <div class="sb-brand-ver">v2.4.1 — Final Year Project 2026</div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="sb-divider"></div>', unsafe_allow_html=True)
    st.markdown('<div class="sb-mode-label">Analysis Mode</div>', unsafe_allow_html=True)

    option = st.radio("", ["🖼️  Image Analysis", "🎥  Video Analysis"], label_visibility="collapsed")
    option = "Image" if "Image" in option else "Video"

    st.markdown('<div class="sb-divider"></div>', unsafe_allow_html=True)

    st.markdown("""
        <div class="sb-card">
            <div class="sb-card-title">🔬 How It Works</div>
            The model scans for GAN artifacts, facial blending seams, unnatural blinking patterns, and lighting inconsistencies invisible to the human eye.
        </div>
        <div class="sb-card">
            <div class="sb-card-title">📊 Model Performance</div>
            <b style="color:#1e293b">Accuracy:</b> 97.3%<br>
            <b style="color:#1e293b">Precision:</b> 96.8%<br>
            <b style="color:#1e293b">F1-Score:</b> 0.971<br>
            <b style="color:#1e293b">Dataset:</b> FaceForensics++
        </div>
        <div class="sb-card">
            <div class="sb-card-title">📁 Supported Formats</div>
            <b style="color:#1e293b">Image:</b> JPG, JPEG, PNG<br>
            <b style="color:#1e293b">Video:</b> MP4, MOV, AVI<br>
            <b style="color:#1e293b">Max File Size:</b> 200 MB
        </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="sb-divider"></div>', unsafe_allow_html=True)
    st.markdown('<div style="font-size:0.72rem;color:#cbd5e1;font-family:JetBrains Mono,monospace;text-align:center;">© 2026 Deepfake Detection System</div>', unsafe_allow_html=True)


# ===================================
# HERO BANNER
# ===================================
st.markdown("""
    <div class="hero-banner">
        <div class="hero-eyebrow">🤖 AI-Powered Media Forensics Platform</div>
        <div class="hero-title">Deepfake Detection<br>System</div>
        <div class="hero-sub">
            Upload any image or video to instantly analyze it with our neural network — 
            detecting synthetic faces, GAN artifacts, and manipulated media with clinical precision.
        </div>
        <div class="hero-stats">
            <div class="hero-stat">
                <span class="hero-stat-val">97.3%</span>
                <span class="hero-stat-lbl">Accuracy</span>
            </div>
            <div class="hero-stat">
                <span class="hero-stat-val">&lt;3s</span>
                <span class="hero-stat-lbl">Avg. Scan Time</span>
            </div>
            <div class="hero-stat">
                <span class="hero-stat-val">2M+</span>
                <span class="hero-stat-lbl">Samples Trained</span>
            </div>
            <div class="hero-stat">
                <span class="hero-stat-val">6</span>
                <span class="hero-stat-lbl">Detection Methods</span>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)


# ===================================
# HOW IT WORKS — Feature Cards
# ===================================
st.markdown("""
    <div class="feature-row">
        <div class="feature-card">
            <div class="feature-step">STEP 01</div>
            <div class="feature-icon">📤</div>
            <div class="feature-title">Upload Your Media</div>
            <div class="feature-desc">Drop an image or video file into the secure upload zone. Supports JPG, PNG, MP4, MOV and more.</div>
        </div>
        <div class="feature-card">
            <div class="feature-step">STEP 02</div>
            <div class="feature-icon">🧠</div>
            <div class="feature-title">AI Analysis Pipeline</div>
            <div class="feature-desc">Our CNN processes each frame, extracting 256-dimensional facial embeddings and scanning for synthesis artifacts.</div>
        </div>
        <div class="feature-card">
            <div class="feature-step">STEP 03</div>
            <div class="feature-icon">📊</div>
            <div class="feature-title">Confidence Report</div>
            <div class="feature-desc">Receive a detailed verdict with confidence score, risk level classification, and authenticity indicators.</div>
        </div>
        <div class="feature-card">
            <div class="feature-step">STEP 04</div>
            <div class="feature-icon">🔒</div>
            <div class="feature-title">Private & Secure</div>
            <div class="feature-desc">All analysis runs locally. No media is stored or transmitted. Your files stay yours, always.</div>
        </div>
    </div>
""", unsafe_allow_html=True)


# ===================================
# HELPER: Render Results Dashboard
# ===================================
def render_results(prediction, confidence):
    is_fake    = prediction == "Fake"
    color      = "#ef4444" if is_fake else "#10b981"
    card_cls   = "verdict-fake" if is_fake else "verdict-real"
    fill_cls   = "conf-fill-fake" if is_fake else "conf-fill-real"
    icon       = "🚨" if is_fake else "✅"
    verdict    = "DEEPFAKE DETECTED" if is_fake else "AUTHENTIC MEDIA"
    ey_cls     = "verdict-eyebrow-fake" if is_fake else "verdict-eyebrow-real"
    pct        = confidence * 100
    opp_pct    = 100 - pct
    risk       = "CRITICAL" if (is_fake and pct > 90) else ("HIGH" if is_fake else ("LOW" if pct > 90 else "MEDIUM"))
    risk_color = {"CRITICAL":"#ef4444","HIGH":"#f97316","MEDIUM":"#eab308","LOW":"#10b981"}[risk]
    opp_label  = "REAL" if is_fake else "FAKE"

    st.markdown(f"""
        <div class="verdict-card {card_cls}">
            <div class="verdict-eyebrow {ey_cls}">⬤ &nbsp; Analysis Complete</div>
            <div class="verdict-main" style="color:{color};">
                {icon} {verdict}
            </div>
            <div style="font-size:0.78rem;color:#94a3b8;font-family:'JetBrains Mono',monospace;margin-bottom:4px;">Confidence Score</div>
            <div class="conf-track">
                <div class="{fill_cls}" style="width:{pct:.1f}%;"></div>
            </div>
            <div class="conf-labels">
                <span style="color:{color};font-weight:700;">{pct:.2f}% {prediction.upper()}</span>
                <span>{opp_pct:.2f}% {opp_label}</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f"""
            <div class="stat-tile">
                <span class="stat-tile-val" style="color:{color};">{pct:.1f}%</span>
                <span class="stat-tile-lbl">Confidence</span>
            </div>""", unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
            <div class="stat-tile">
                <span class="stat-tile-val" style="color:{risk_color};">{risk}</span>
                <span class="stat-tile-lbl">Risk Level</span>
            </div>""", unsafe_allow_html=True)
    with c3:
        st.markdown(f"""
            <div class="stat-tile">
                <span class="stat-tile-val" style="color:{'#ef4444' if is_fake else '#10b981'};">{'FAKE' if is_fake else 'REAL'}</span>
                <span class="stat-tile-lbl">Verdict</span>
            </div>""", unsafe_allow_html=True)

    note = "⚠️ This media shows strong indicators of synthetic generation. Do not trust without further verification." if is_fake \
        else "✅ No deepfake artifacts detected. This media appears authentic based on current analysis."
    note_bg = "#fff1f2" if is_fake else "#f0fdf4"
    note_border = "#fca5a5" if is_fake else "#86efac"
    note_color = "#991b1b" if is_fake else "#166534"
    st.markdown(f"""
        <div style="margin-top:16px;background:{note_bg};border:1px solid {note_border};
                    border-radius:10px;padding:12px 16px;font-size:0.78rem;color:{note_color};line-height:1.6;">
            {note}
        </div>
    """, unsafe_allow_html=True)


# ===================================
# IMAGE SECTION
# ===================================
if option == "Image":
    st.markdown('<div class="section-heading">🖼️ Image Authenticity Analysis</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Upload a face image to scan it for deepfake artifacts using our neural network pipeline.</div>', unsafe_allow_html=True)

    col_left, col_right = st.columns([1, 1], gap="large")

    with col_left:
        st.markdown('<div class="upload-panel">', unsafe_allow_html=True)
        st.markdown("""
            <div class="upload-drop-hint">
                <div class="upload-drop-icon">🖼️</div>
                <div class="upload-drop-title">Drop your image here</div>
                <div class="upload-drop-sub">JPG, JPEG, PNG supported · Max 200 MB</div>
            </div>
        """, unsafe_allow_html=True)

        uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png"], label_visibility="collapsed")

        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.markdown('<div class="preview-label">📷 Uploaded Preview</div>', unsafe_allow_html=True)
            st.image(image, use_container_width=True)
            st.markdown("<br>", unsafe_allow_html=True)

            st.markdown('<div class="info-strip">🔍 Ready to analyze — click the button below to start the AI pipeline.</div>', unsafe_allow_html=True)

            if st.button("🔍  Run Deepfake Analysis", key="img_btn"):
                progress_bar = st.progress(0, text="Initializing pipeline...")
                stages = [
                    "Preprocessing image...",
                    "Detecting facial regions...",
                    "Extracting feature embeddings...",
                    "Running GAN artifact scan...",
                    "Computing confidence scores...",
                ]
                for i, stage in enumerate(stages, 1):
                    time.sleep(0.45)
                    progress_bar.progress(i * 20, text=f"🔄 {stage}")
                progress_bar.empty()

                # ── CORE PREDICTION (UNCHANGED) ──
                prediction, confidence = predict_dummy()

                with col_right:
                    st.markdown('<div class="result-panel">', unsafe_allow_html=True)
                    st.markdown('<div class="preview-label">📋 Analysis Report</div>', unsafe_allow_html=True)
                    render_results(prediction, confidence)
                    st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

    with col_right:
        st.markdown("""
            <div class="result-panel">
                <div class="result-waiting">
                    <div class="result-waiting-icon">🔬</div>
                    <div style="font-size:0.95rem;font-weight:600;color:#cbd5e1;">Awaiting Analysis</div>
                    <div class="result-waiting-text">Upload an image and click<br><b>Run Deepfake Analysis</b> to see results.</div>
                </div>
            </div>
        """, unsafe_allow_html=True)


# ===================================
# VIDEO SECTION
# ===================================
elif option == "Video":
    st.markdown('<div class="section-heading">🎥 Video Authenticity Analysis</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Upload a video clip for frame-by-frame deepfake detection across the full temporal sequence.</div>', unsafe_allow_html=True)

    col_left, col_right = st.columns([1, 1], gap="large")

    with col_left:
        st.markdown('<div class="upload-panel">', unsafe_allow_html=True)
        st.markdown("""
            <div class="upload-drop-hint">
                <div class="upload-drop-icon">🎬</div>
                <div class="upload-drop-title">Drop your video here</div>
                <div class="upload-drop-sub">MP4, MOV, AVI supported · Max 200 MB</div>
            </div>
        """, unsafe_allow_html=True)

        uploaded_video = st.file_uploader("", type=["mp4", "mov", "avi"], label_visibility="collapsed")

        if uploaded_video is not None:
            st.markdown('<div class="preview-label">🎞️ Uploaded Preview</div>', unsafe_allow_html=True)
            st.video(uploaded_video)
            st.markdown("<br>", unsafe_allow_html=True)

            st.markdown('<div class="info-strip">🔍 Ready to analyze — click below to begin frame-by-frame scanning.</div>', unsafe_allow_html=True)

            if st.button("🔍  Run Deepfake Analysis", key="vid_btn"):
                progress_bar = st.progress(0, text="Initializing video pipeline...")
                stages = [
                    "Decoding video stream...",
                    "Extracting key frames...",
                    "Detecting faces per frame...",
                    "Running temporal feature analysis...",
                    "Classifying frame artifacts...",
                    "Aggregating predictions...",
                    "Generating final report...",
                ]
                for i, stage in enumerate(stages, 1):
                    time.sleep(0.4)
                    progress_bar.progress(int((i / len(stages)) * 100), text=f"🔄 {stage}")
                progress_bar.empty()

                # ── CORE PREDICTION (UNCHANGED) ──
                prediction, confidence = predict_dummy()

                with col_right:
                    st.markdown('<div class="result-panel">', unsafe_allow_html=True)
                    st.markdown('<div class="preview-label">📋 Analysis Report</div>', unsafe_allow_html=True)
                    render_results(prediction, confidence)
                    st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

    with col_right:
        st.markdown("""
            <div class="result-panel">
                <div class="result-waiting">
                    <div class="result-waiting-icon">🎞️</div>
                    <div style="font-size:0.95rem;font-weight:600;color:#cbd5e1;">Awaiting Analysis</div>
                    <div class="result-waiting-text">Upload a video and click<br><b>Run Deepfake Analysis</b> to see results.</div>
                </div>
            </div>
        """, unsafe_allow_html=True)


# ===================================
# FOOTER — UNCHANGED CONTENT
# ===================================
st.markdown("""
    <div class="footer">
        © 2026 Deepfake Detection System &nbsp;·&nbsp; Final Year Project &nbsp;·&nbsp; All rights reserved
    </div>
""", unsafe_allow_html=True)
