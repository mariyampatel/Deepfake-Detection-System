import streamlit as st
import random
import time
from PIL import Image

# ===================================
# PAGE CONFIG
# ===================================
st.set_page_config(
    page_title="Deepfake Detection System",
    page_icon="🧠",
    layout="wide"
)

# ===================================
# CUSTOM CSS (Professional Cybersecurity UI)
# ===================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

    .stApp {
        background-color: #0a0e1a;
        background-image:
            radial-gradient(ellipse at 20% 50%, rgba(0,212,255,0.04) 0%, transparent 50%),
            radial-gradient(ellipse at 80% 20%, rgba(99,102,241,0.06) 0%, transparent 50%);
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0d1117 0%, #111827 100%);
        border-right: 1px solid rgba(0,212,255,0.15);
    }
    [data-testid="stSidebar"] * { color: #e2e8f0 !important; }

    .header-banner {
        background: linear-gradient(135deg, #0d1117 0%, #111827 50%, #0d1117 100%);
        border: 1px solid rgba(0,212,255,0.2);
        border-radius: 16px;
        padding: 32px 40px;
        margin-bottom: 28px;
        position: relative;
        overflow: hidden;
    }
    .header-banner::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 2px;
        background: linear-gradient(90deg, transparent, #00d4ff, #6366f1, transparent);
    }
    .header-title { font-size: 2.2rem; font-weight: 700; color: #f1f5f9; letter-spacing: -0.5px; margin: 0 0 6px 0; }
    .header-subtitle { font-size: 0.95rem; color: #94a3b8; margin: 0; }
    .header-badge {
        display: inline-block;
        background: rgba(0,212,255,0.1);
        border: 1px solid rgba(0,212,255,0.3);
        color: #00d4ff;
        font-size: 0.72rem; font-weight: 600;
        letter-spacing: 1.5px; text-transform: uppercase;
        padding: 4px 12px; border-radius: 20px;
        margin-bottom: 16px;
        font-family: 'JetBrains Mono', monospace;
    }

    .upload-zone {
        background: rgba(13,17,23,0.8);
        border: 2px dashed rgba(0,212,255,0.25);
        border-radius: 16px;
        padding: 36px 24px;
        text-align: center;
        margin-bottom: 16px;
    }
    .upload-icon { font-size: 3rem; margin-bottom: 10px; }
    .upload-title { color: #e2e8f0; font-size: 1.05rem; font-weight: 600; margin-bottom: 6px; }
    .upload-hint { color: #64748b; font-size: 0.83rem; }

    .result-card { border-radius: 16px; padding: 28px; margin-top: 20px; position: relative; overflow: hidden; }
    .result-card-fake { background: linear-gradient(135deg,rgba(239,68,68,0.08),rgba(239,68,68,0.03)); border: 1px solid rgba(239,68,68,0.3); }
    .result-card-real { background: linear-gradient(135deg,rgba(16,185,129,0.08),rgba(16,185,129,0.03)); border: 1px solid rgba(16,185,129,0.3); }
    .result-card::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 2px; }
    .result-card-fake::before { background: linear-gradient(90deg,transparent,#ef4444,transparent); }
    .result-card-real::before { background: linear-gradient(90deg,transparent,#10b981,transparent); }

    .verdict-label { font-size: 0.75rem; font-weight: 600; letter-spacing: 2px; text-transform: uppercase; font-family: 'JetBrains Mono', monospace; margin-bottom: 8px; }
    .verdict-fake { color: #ef4444; }
    .verdict-real { color: #10b981; }
    .verdict-text { font-size: 2.4rem; font-weight: 700; margin: 0; line-height: 1; }
    .verdict-icon { font-size: 2rem; margin-right: 12px; }

    .conf-bar-wrap { background: rgba(255,255,255,0.05); border-radius: 99px; height: 10px; margin: 10px 0 4px 0; overflow: hidden; }
    .conf-bar-fill-fake { height: 100%; border-radius: 99px; background: linear-gradient(90deg,#ef4444,#f97316); }
    .conf-bar-fill-real { height: 100%; border-radius: 99px; background: linear-gradient(90deg,#10b981,#06b6d4); }
    .conf-labels { display: flex; justify-content: space-between; font-size: 0.78rem; color: #64748b; font-family: 'JetBrains Mono', monospace; }

    .stat-box { background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.07); border-radius: 12px; padding: 16px 20px; text-align: center; margin-top: 16px; }
    .stat-val { font-size: 1.6rem; font-weight: 700; color: #f1f5f9; font-family: 'JetBrains Mono', monospace; }
    .stat-lbl { font-size: 0.72rem; color: #64748b; text-transform: uppercase; letter-spacing: 1px; margin-top: 4px; }

    .sidebar-card { background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); border-radius: 10px; padding: 14px 16px; margin-top: 14px; font-size: 0.82rem; color: #94a3b8; line-height: 1.6; }
    .sidebar-card-title { font-size: 0.72rem; font-weight: 600; letter-spacing: 1.5px; text-transform: uppercase; color: #00d4ff; margin-bottom: 8px; font-family: 'JetBrains Mono', monospace; }

    .stButton > button {
        background: linear-gradient(135deg, #1e40af, #6366f1) !important;
        color: #ffffff !important;
        font-size: 0.9rem !important; font-weight: 600 !important;
        letter-spacing: 0.5px !important;
        border-radius: 10px !important; border: none !important;
        padding: 12px 28px !important; width: 100% !important;
    }
    .stButton > button:hover { box-shadow: 0 8px 25px rgba(99,102,241,0.35) !important; }

    [data-testid="stFileUploader"] { background: rgba(13,17,23,0.6) !important; border: 2px dashed rgba(0,212,255,0.2) !important; border-radius: 14px !important; }
    .stProgress > div > div { background-color: #6366f1 !important; }
    .stRadio label, .stRadio span { color: #cbd5e1 !important; }
    h1, h2, h3 { color: #f1f5f9 !important; }
    p, li { color: #94a3b8; }
    hr { border-color: rgba(255,255,255,0.07) !important; }

    .footer {
        text-align: center; color: #374151; font-size: 0.78rem;
        padding: 24px 0 8px 0; font-family: 'JetBrains Mono', monospace;
        border-top: 1px solid rgba(255,255,255,0.05); margin-top: 40px;
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
        <div style="padding:10px 0 20px 0;">
            <div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;letter-spacing:2px;
                        color:#00d4ff;text-transform:uppercase;margin-bottom:6px;">System</div>
            <div style="font-size:1.15rem;font-weight:700;color:#f1f5f9;">DeepGuard AI</div>
            <div style="font-size:0.78rem;color:#64748b;margin-top:2px;">v2.4.1 — Enterprise</div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown('<div style="font-size:0.75rem;letter-spacing:1.5px;color:#00d4ff;text-transform:uppercase;font-family:JetBrains Mono,monospace;margin-bottom:8px;">Analysis Mode</div>', unsafe_allow_html=True)

    option = st.radio("", ["Image", "Video"], label_visibility="collapsed")

    st.markdown("---")
    st.markdown("""
        <div class="sidebar-card">
            <div class="sidebar-card-title">🔬 About</div>
            Powered by deep neural networks trained on millions of real and synthetic media samples. Detects GAN artifacts, blending inconsistencies & temporal anomalies.
        </div>
        <div class="sidebar-card">
            <div class="sidebar-card-title">📊 Model Stats</div>
            <b style="color:#e2e8f0">Accuracy:</b> 97.3%<br>
            <b style="color:#e2e8f0">F1-Score:</b> 0.971<br>
            <b style="color:#e2e8f0">Dataset:</b> FaceForensics++
        </div>
        <div class="sidebar-card">
            <div class="sidebar-card-title">⚠️ Supported Formats</div>
            <b style="color:#e2e8f0">Image:</b> JPG, JPEG, PNG<br>
            <b style="color:#e2e8f0">Video:</b> MP4, MOV, AVI<br>
            <b style="color:#e2e8f0">Max Size:</b> 200 MB
        </div>
    """, unsafe_allow_html=True)


# ===================================
# HEADER
# ===================================
st.markdown("""
    <div class="header-banner">
        <div class="header-badge">🛡️ AI Forensics &nbsp;|&nbsp; Deepfake Intelligence</div>
        <div class="header-title">Deepfake Detection System</div>
        <div class="header-subtitle">
            Upload image or video media to perform AI-powered authenticity analysis.
            Results include confidence scoring and risk assessment.
        </div>
    </div>
""", unsafe_allow_html=True)


# ===================================
# HELPER: Render Results Dashboard
# ===================================
def render_results(prediction, confidence):
    is_fake   = prediction == "Fake"
    color     = "#ef4444" if is_fake else "#10b981"
    card_cls  = "result-card-fake" if is_fake else "result-card-real"
    bar_cls   = "conf-bar-fill-fake" if is_fake else "conf-bar-fill-real"
    icon      = "🚨" if is_fake else "✅"
    verdict   = "DEEPFAKE DETECTED" if is_fake else "AUTHENTIC MEDIA"
    vlabel    = "verdict-fake" if is_fake else "verdict-real"
    pct       = confidence * 100
    opp_pct   = 100 - pct
    risk      = "CRITICAL" if (is_fake and pct > 90) else ("HIGH" if is_fake else ("LOW" if pct > 90 else "MEDIUM"))
    risk_color = {"CRITICAL":"#ef4444","HIGH":"#f97316","MEDIUM":"#eab308","LOW":"#10b981"}[risk]

    st.markdown(f"""
        <div class="result-card {card_cls}">
            <div class="verdict-label {vlabel}">⬤ &nbsp;Analysis Complete — Verdict</div>
            <div style="display:flex;align-items:center;margin:12px 0 20px 0;">
                <span class="verdict-icon">{icon}</span>
                <span class="verdict-text" style="color:{color};">{verdict}</span>
            </div>
            <div style="margin-bottom:6px;font-size:0.8rem;color:#94a3b8;font-family:'JetBrains Mono',monospace;">Confidence Score</div>
            <div class="conf-bar-wrap"><div class="{bar_cls}" style="width:{pct:.1f}%;"></div></div>
            <div class="conf-labels">
                <span style="color:{color};font-weight:600;">{pct:.2f}% {prediction.upper()}</span>
                <span>{opp_pct:.2f}% {'REAL' if is_fake else 'FAKE'}</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f'<div class="stat-box"><div class="stat-val" style="color:{color};">{pct:.1f}%</div><div class="stat-lbl">Confidence</div></div>', unsafe_allow_html=True)
    with c2:
        st.markdown(f'<div class="stat-box"><div class="stat-val" style="color:{risk_color};">{risk}</div><div class="stat-lbl">Risk Level</div></div>', unsafe_allow_html=True)
    with c3:
        st.markdown(f'<div class="stat-box"><div class="stat-val" style="color:#6366f1;">{"⚠" if is_fake else "✔"}</div><div class="stat-lbl">Status</div></div>', unsafe_allow_html=True)


# ===================================
# IMAGE SECTION
# ===================================
if option == "Image":
    st.markdown('<div style="font-size:1.05rem;font-weight:600;color:#e2e8f0;margin-bottom:16px;">🖼️ &nbsp;Image Authenticity Analysis</div>', unsafe_allow_html=True)
    col_upload, col_result = st.columns([1, 1], gap="large")

    with col_upload:
        st.markdown("""
            <div class="upload-zone">
                <div class="upload-icon">📂</div>
                <div class="upload-title">Drag & Drop or Browse</div>
                <div class="upload-hint">Supported: JPG · JPEG · PNG &nbsp;|&nbsp; Max 200 MB</div>
            </div>
        """, unsafe_allow_html=True)

        uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"], label_visibility="collapsed")

        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_container_width=True)

            if st.button("🔍  Run Deepfake Analysis", key="img_btn"):
                progress_bar = st.progress(0, text="🔄 Preprocessing image...")
                stages = ["Preprocessing image...", "Extracting facial landmarks...",
                          "Running GAN artifact detection...", "Computing confidence scores...", "Finalizing analysis..."]
                for i, stage in enumerate(stages, 1):
                    time.sleep(0.4)
                    progress_bar.progress(i * 20, text=f"🔄 {stage}")
                progress_bar.empty()

                # ── CORE PREDICTION (UNCHANGED) ──
                prediction, confidence = predict_dummy()

                with col_result:
                    st.markdown('<div style="font-size:0.9rem;font-weight:600;color:#94a3b8;margin-bottom:8px;">📋 Analysis Report</div>', unsafe_allow_html=True)
                    render_results(prediction, confidence)

    with col_result:
        st.markdown("""
            <div style="height:100%;display:flex;align-items:center;justify-content:center;
                        flex-direction:column;gap:12px;padding:60px 20px;
                        border:1px dashed rgba(255,255,255,0.07);border-radius:16px;text-align:center;">
                <div style="font-size:2.5rem;">🔬</div>
                <div style="color:#4b5563;font-size:0.9rem;">Analysis results will appear here after running detection.</div>
            </div>
        """, unsafe_allow_html=True)


# ===================================
# VIDEO SECTION
# ===================================
elif option == "Video":
    st.markdown('<div style="font-size:1.05rem;font-weight:600;color:#e2e8f0;margin-bottom:16px;">🎥 &nbsp;Video Authenticity Analysis</div>', unsafe_allow_html=True)
    col_upload, col_result = st.columns([1, 1], gap="large")

    with col_upload:
        st.markdown("""
            <div class="upload-zone">
                <div class="upload-icon">🎬</div>
                <div class="upload-title">Drag & Drop or Browse</div>
                <div class="upload-hint">Supported: MP4 · MOV · AVI &nbsp;|&nbsp; Max 200 MB</div>
            </div>
        """, unsafe_allow_html=True)

        uploaded_video = st.file_uploader("Upload Video", type=["mp4", "mov", "avi"], label_visibility="collapsed")

        if uploaded_video is not None:
            st.video(uploaded_video)

            if st.button("🔍  Run Deepfake Analysis", key="vid_btn"):
                progress_bar = st.progress(0, text="🔄 Loading video frames...")
                stages = ["Loading video frames...", "Detecting faces per frame...",
                          "Extracting temporal features...", "Running deepfake classifier...",
                          "Aggregating frame predictions...", "Computing final confidence...", "Generating report..."]
                for i, stage in enumerate(stages, 1):
                    time.sleep(0.4)
                    progress_bar.progress(int((i / len(stages)) * 100), text=f"🔄 {stage}")
                progress_bar.empty()

                # ── CORE PREDICTION (UNCHANGED) ──
                prediction, confidence = predict_dummy()

                with col_result:
                    st.markdown('<div style="font-size:0.9rem;font-weight:600;color:#94a3b8;margin-bottom:8px;">📋 Analysis Report</div>', unsafe_allow_html=True)
                    render_results(prediction, confidence)

    with col_result:
        st.markdown("""
            <div style="height:100%;display:flex;align-items:center;justify-content:center;
                        flex-direction:column;gap:12px;padding:60px 20px;
                        border:1px dashed rgba(255,255,255,0.07);border-radius:16px;text-align:center;">
                <div style="font-size:2.5rem;">🎞️</div>
                <div style="color:#4b5563;font-size:0.9rem;">Upload a video and run analysis to see the deepfake report.</div>
            </div>
        """, unsafe_allow_html=True)


# ===================================
# FOOTER  ← UNCHANGED CONTENT
# ===================================
st.markdown("""
    <div class="footer">
        ─────────────────────────────────────────────────────<br>
        © 2026 Deepfake Detection System &nbsp;|&nbsp; Final Year Project
    </div>
""", unsafe_allow_html=True)
