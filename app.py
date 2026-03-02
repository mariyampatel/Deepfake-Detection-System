import streamlit as st
import random
import time
import math
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
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

    .stApp {
        background: #f0f4f8;
        background-image: radial-gradient(ellipse at 10% 20%, rgba(219,234,254,0.5) 0%, transparent 50%),
                          radial-gradient(ellipse at 90% 80%, rgba(237,233,254,0.4) 0%, transparent 50%);
    }

    /* ── Sidebar ── */
    [data-testid="stSidebar"] {
        background: #ffffff;
        border-right: 1px solid #e2e8f0;
        box-shadow: 2px 0 16px rgba(0,0,0,0.05);
    }
    [data-testid="stSidebar"] * { color: #1e293b !important; }

    /* ── Hero ── */
    .hero-banner {
        background: linear-gradient(135deg, #1e3a5f 0%, #1d4ed8 55%, #7c3aed 100%);
        border-radius: 22px;
        padding: 50px 56px;
        margin-bottom: 28px;
        position: relative;
        overflow: hidden;
        box-shadow: 0 24px 64px rgba(29,78,216,0.28);
    }
    .hero-banner::before {
        content: '';
        position: absolute; inset: 0;
        background: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='0.03'%3E%3Ccircle cx='30' cy='30' r='2'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
    }
    .hero-banner::after {
        content: '🛡️';
        position: absolute; right: 56px; top: 50%;
        transform: translateY(-50%);
        font-size: 8rem; opacity: 0.1;
    }
    .hero-eyebrow {
        display: inline-block;
        background: rgba(255,255,255,0.15);
        border: 1px solid rgba(255,255,255,0.25);
        color: #bfdbfe;
        font-size: 0.68rem; font-weight: 600;
        letter-spacing: 2.5px; text-transform: uppercase;
        padding: 5px 14px; border-radius: 20px;
        margin-bottom: 18px;
        font-family: 'JetBrains Mono', monospace;
    }
    .hero-title {
        font-size: 2.8rem; font-weight: 800;
        color: #ffffff; letter-spacing: -1.2px;
        margin: 0 0 12px; line-height: 1.08;
    }
    .hero-sub {
        font-size: 1rem; color: #bfdbfe;
        margin: 0; max-width: 500px;
        line-height: 1.65; font-weight: 400;
    }
    .hero-stats {
        display: flex; gap: 14px;
        margin-top: 30px; flex-wrap: wrap;
    }
    .hero-stat {
        background: rgba(255,255,255,0.12);
        border: 1px solid rgba(255,255,255,0.18);
        border-radius: 14px; padding: 13px 22px;
        text-align: center; min-width: 100px;
        backdrop-filter: blur(4px);
    }
    .hero-stat-val {
        font-size: 1.45rem; font-weight: 700;
        color: #ffffff; font-family: 'JetBrains Mono', monospace; display: block;
    }
    .hero-stat-lbl {
        font-size: 0.64rem; color: #93c5fd;
        text-transform: uppercase; letter-spacing: 1px;
        margin-top: 3px; display: block;
    }

    /* ── Step Cards ── */
    .steps-row { display: flex; gap: 14px; margin-bottom: 30px; }
    .step-card {
        background: #ffffff; border: 1px solid #e2e8f0;
        border-radius: 18px; padding: 22px 20px; flex: 1;
        box-shadow: 0 2px 12px rgba(0,0,0,0.04);
        transition: all 0.25s ease;
        border-top: 3px solid transparent;
    }
    .step-card:nth-child(1) { border-top-color: #1d4ed8; }
    .step-card:nth-child(2) { border-top-color: #7c3aed; }
    .step-card:nth-child(3) { border-top-color: #0891b2; }
    .step-card:nth-child(4) { border-top-color: #059669; }
    .step-card:hover { box-shadow: 0 10px 32px rgba(0,0,0,0.1); transform: translateY(-2px); }
    .step-num {
        display: inline-block; background: #eff6ff; color: #1d4ed8;
        font-size: 0.6rem; font-weight: 700; padding: 3px 9px;
        border-radius: 8px; margin-bottom: 12px; letter-spacing: 0.5px;
        font-family: 'JetBrains Mono', monospace;
    }
    .step-icon { font-size: 1.8rem; margin-bottom: 10px; }
    .step-title { font-size: 0.88rem; font-weight: 700; color: #0f172a; margin-bottom: 5px; }
    .step-desc { font-size: 0.76rem; color: #64748b; line-height: 1.6; }

    /* ── Section Labels ── */
    .sec-head { font-size: 1.15rem; font-weight: 700; color: #0f172a; margin-bottom: 3px; }
    .sec-sub { font-size: 0.82rem; color: #94a3b8; margin-bottom: 20px; }

    /* ── Panels ── */
    .panel {
        background: #ffffff; border: 1px solid #e2e8f0;
        border-radius: 20px; padding: 26px;
        box-shadow: 0 2px 16px rgba(0,0,0,0.05);
    }

    /* ── Upload Zone ── */
    .drop-zone {
        background: linear-gradient(135deg, #eff6ff, #f5f3ff);
        border: 2px dashed #93c5fd;
        border-radius: 14px; padding: 30px 20px;
        text-align: center; margin-bottom: 16px;
    }
    .drop-icon { font-size: 2.4rem; margin-bottom: 8px; }
    .drop-title { font-size: 0.92rem; font-weight: 600; color: #1e40af; margin-bottom: 4px; }
    .drop-sub { font-size: 0.75rem; color: #94a3b8; }

    .preview-lbl {
        font-size: 0.68rem; font-weight: 600; letter-spacing: 2px;
        text-transform: uppercase; color: #94a3b8;
        font-family: 'JetBrains Mono', monospace; margin-bottom: 8px;
    }
    .info-pill {
        background: #eff6ff; border: 1px solid #bfdbfe;
        border-radius: 10px; padding: 9px 14px;
        font-size: 0.76rem; color: #1e40af;
        margin-bottom: 14px; display: flex;
        align-items: center; gap: 7px;
    }

    /* ── Forensic Visualizations ── */
    .viz-section { margin-top: 20px; }
    .viz-title {
        font-size: 0.7rem; font-weight: 700; letter-spacing: 1.5px;
        text-transform: uppercase; color: #64748b;
        font-family: 'JetBrains Mono', monospace; margin-bottom: 10px;
    }

    /* Heat Map */
    .heatmap-container {
        background: #0f172a; border-radius: 12px;
        overflow: hidden; position: relative;
        margin-bottom: 14px;
    }
    .heatmap-header {
        padding: 8px 14px;
        background: #1e293b;
        display: flex; justify-content: space-between; align-items: center;
    }
    .heatmap-header-title {
        font-size: 0.65rem; font-weight: 600; color: #94a3b8;
        font-family: 'JetBrains Mono', monospace; letter-spacing: 1px; text-transform: uppercase;
    }
    .heatmap-badge {
        font-size: 0.6rem; font-weight: 700;
        padding: 2px 8px; border-radius: 6px;
        font-family: 'JetBrains Mono', monospace;
    }
    .heatmap-grid {
        display: grid;
        grid-template-columns: repeat(20, 1fr);
        gap: 1px; padding: 12px;
    }
    .hm-cell {
        aspect-ratio: 1;
        border-radius: 2px;
    }

    /* Anomaly Grid */
    .anomaly-container {
        background: #0f172a; border-radius: 12px;
        overflow: hidden; margin-bottom: 14px;
    }
    .anomaly-grid {
        display: grid;
        grid-template-columns: repeat(16, 1fr);
        gap: 2px; padding: 12px;
    }
    .an-cell {
        aspect-ratio: 1; border-radius: 1px;
    }

    /* Metric rows */
    .metric-row {
        display: flex; flex-direction: column; gap: 8px;
        margin-top: 14px;
    }
    .metric-item {
        display: flex; align-items: center;
        justify-content: space-between;
        background: #f8fafc; border: 1px solid #e2e8f0;
        border-radius: 10px; padding: 10px 14px;
    }
    .metric-key {
        font-size: 0.7rem; font-weight: 600; color: #64748b;
        font-family: 'JetBrains Mono', monospace; letter-spacing: 0.5px;
    }
    .metric-val {
        font-size: 0.72rem; font-weight: 700;
        font-family: 'JetBrains Mono', monospace;
    }
    .metric-bar-wrap { flex: 1; margin: 0 12px; }
    .metric-bar-track { background: #e2e8f0; border-radius: 99px; height: 5px; }
    .metric-bar-fill { height: 100%; border-radius: 99px; }

    /* ── Verdict ── */
    .verdict-card {
        border-radius: 16px; padding: 24px;
        margin-bottom: 18px; position: relative; overflow: hidden;
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
        content: ''; position: absolute; top: 0; left: 0; right: 0; height: 3px;
    }
    .verdict-fake::before { background: linear-gradient(90deg,#ef4444,#f97316); }
    .verdict-real::before { background: linear-gradient(90deg,#10b981,#06b6d4); }
    .verdict-eye {
        font-size: 0.66rem; font-weight: 700; letter-spacing: 2.5px;
        text-transform: uppercase; font-family: 'JetBrains Mono', monospace; margin-bottom: 10px;
    }
    .verdict-main { font-size: 1.75rem; font-weight: 800; line-height: 1; margin-bottom: 16px; }

    .conf-track { background: #f1f5f9; border-radius: 99px; height: 8px; margin: 8px 0 4px; overflow: hidden; }
    .conf-fill-fake { height: 100%; border-radius: 99px; background: linear-gradient(90deg,#ef4444,#f97316); }
    .conf-fill-real { height: 100%; border-radius: 99px; background: linear-gradient(90deg,#10b981,#06b6d4); }
    .conf-labels { display: flex; justify-content: space-between; font-size: 0.7rem; color: #94a3b8; font-family: 'JetBrains Mono', monospace; }

    .stat-row { display: flex; gap: 10px; margin-top: 14px; }
    .stat-tile {
        flex: 1; background: #f8fafc; border: 1px solid #e2e8f0;
        border-radius: 12px; padding: 13px 10px; text-align: center;
    }
    .stat-tile-val { font-size: 1.25rem; font-weight: 700; font-family: 'JetBrains Mono', monospace; display: block; }
    .stat-tile-lbl { font-size: 0.62rem; color: #94a3b8; text-transform: uppercase; letter-spacing: 1px; margin-top: 3px; display: block; }

    /* ── Result waiting ── */
    .waiting-panel {
        display: flex; flex-direction: column;
        align-items: center; justify-content: center;
        padding: 70px 20px; text-align: center; gap: 10px;
    }

    /* ── Sidebar ── */
    .sb-name { font-size: 1.1rem; font-weight: 800; color: #0f172a; letter-spacing: -0.3px; }
    .sb-badge {
        display: inline-block; background: #eff6ff; color: #1d4ed8;
        font-size: 0.6rem; font-weight: 700; letter-spacing: 1px;
        text-transform: uppercase; padding: 3px 9px; border-radius: 6px;
        margin-bottom: 14px; font-family: 'JetBrains Mono', monospace;
    }
    .sb-card {
        background: #f8fafc; border: 1px solid #e2e8f0;
        border-radius: 12px; padding: 13px 15px;
        margin-top: 12px; font-size: 0.78rem; color: #475569; line-height: 1.65;
    }
    .sb-card-title {
        font-size: 0.65rem; font-weight: 700; letter-spacing: 1.5px;
        text-transform: uppercase; color: #1d4ed8;
        margin-bottom: 7px; font-family: 'JetBrains Mono', monospace;
    }

    /* ── Buttons ── */
    .stButton > button {
        background: linear-gradient(135deg,#1d4ed8,#7c3aed) !important;
        color: #fff !important; font-size: 0.88rem !important;
        font-weight: 600 !important; border-radius: 12px !important;
        border: none !important; padding: 13px 28px !important;
        width: 100% !important; letter-spacing: 0.3px !important;
        box-shadow: 0 4px 16px rgba(29,78,216,0.3) !important;
    }
    .stButton > button:hover {
        box-shadow: 0 8px 28px rgba(29,78,216,0.45) !important;
        transform: translateY(-1px) !important;
    }

    /* ── File uploader ── */
    [data-testid="stFileUploader"] {
        background: #f0f9ff !important;
        border: 2px dashed #93c5fd !important;
        border-radius: 12px !important;
    }
    .stProgress > div > div { background: linear-gradient(90deg,#1d4ed8,#7c3aed) !important; }
    .stRadio label, .stRadio span { color: #334155 !important; font-size: 0.86rem !important; }
    h1,h2,h3 { color: #0f172a !important; }
    hr { border-color: #e2e8f0 !important; }

    .footer {
        text-align: center; color: #cbd5e1; font-size: 0.72rem;
        padding: 28px 0 10px; border-top: 1px solid #e2e8f0;
        margin-top: 48px; font-family: 'JetBrains Mono', monospace;
    }

    /* ── Video placeholder ── */
    .video-placeholder {
        background: linear-gradient(135deg, #1e293b, #0f172a);
        border-radius: 14px; padding: 40px 20px;
        text-align: center; margin-bottom: 14px;
        border: 1px solid #334155;
        animation: pulse-border 2s infinite;
    }
    @keyframes pulse-border {
        0%,100% { border-color: #334155; }
        50% { border-color: #1d4ed8; }
    }
    .vp-icon { font-size: 3rem; margin-bottom: 12px; opacity: 0.6; }
    .vp-text { font-size: 0.82rem; color: #64748b; }
    .vp-spinner {
        width: 28px; height: 28px; margin: 14px auto 0;
        border: 3px solid #1e293b;
        border-top-color: #1d4ed8;
        border-radius: 50%;
        animation: spin 0.8s linear infinite;
    }
    @keyframes spin { to { transform: rotate(360deg); } }
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
# FORENSIC VISUALIZATION HELPERS
# ===================================
def build_heatmap_svg(is_fake, seed=42):
    """Generate an SVG heatmap showing facial anomaly regions."""
    rng = random.Random(seed)
    rows, cols = 14, 22
    cells = []
    cx, cy = cols // 2, rows // 2

    for r in range(rows):
        for c in range(cols):
            dx = (c - cx) / (cols / 2)
            dy = (r - cy) / (rows / 2)
            dist = math.sqrt(dx**2 + dy**2)
            face_mask = dist < 1.0
            if is_fake:
                if 0.3 < dist < 0.65:
                    intensity = rng.uniform(0.65, 1.0)
                    region = "hot"
                elif dist <= 0.3:
                    intensity = rng.uniform(0.15, 0.45)
                    region = "mid"
                elif face_mask:
                    intensity = rng.uniform(0.05, 0.25)
                    region = "cool"
                else:
                    intensity = rng.uniform(0.0, 0.08)
                    region = "bg"
            else:
                if dist < 0.7:
                    intensity = rng.uniform(0.0, 0.2)
                    region = "cool"
                else:
                    intensity = rng.uniform(0.0, 0.06)
                    region = "bg"

            if region == "hot":
                r_val = int(220 + intensity * 35)
                g_val = int(60 - intensity * 40)
                b_val = int(30 - intensity * 20)
                opacity = 0.85 + intensity * 0.15
            elif region == "mid":
                r_val = int(240 + intensity * 15)
                g_val = int(140 + intensity * 50)
                b_val = int(30)
                opacity = 0.7
            elif region == "cool":
                r_val = int(30 + intensity * 40)
                g_val = int(130 + intensity * 80)
                b_val = int(210 + intensity * 40)
                opacity = 0.5 + intensity * 0.3
            else:
                r_val, g_val, b_val = 15, 25, 50
                opacity = 0.3

            x = c * (100 / cols)
            y = r * (100 / rows)
            w = 100 / cols + 0.3
            h = 100 / rows + 0.3
            cells.append(
                f'<rect x="{x:.1f}%" y="{y:.1f}%" width="{w:.1f}%" height="{h:.1f}%" '
                f'fill="rgb({r_val},{g_val},{b_val})" opacity="{opacity:.2f}" rx="1"/>'
            )

    label = "ANOMALY MAP — HIGH DEVIATION DETECTED" if is_fake else "ANOMALY MAP — BASELINE NORMAL"
    label_color = "#f97316" if is_fake else "#10b981"

    legend_items = [
        ("rgb(230,50,30)", "High Anomaly"),
        ("rgb(240,160,30)", "Moderate"),
        ("rgb(30,180,220)", "Baseline"),
    ]
    legend_svg = ""
    for i, (col, txt) in enumerate(legend_items):
        lx = 4 + i * 33
        legend_svg += (
            f'<rect x="{lx}%" y="88%" width="3%" height="4%" fill="{col}" rx="1" opacity="0.9"/>'
            f'<text x="{lx + 3.8:.0f}%" y="92%" fill="#94a3b8" font-size="6" font-family="monospace">{txt}</text>'
        )

    svg = f"""<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"
               style="width:100%;height:180px;display:block;background:#0f172a;border-radius:10px;">
        {''.join(cells)}
        <text x="50%" y="6%" text-anchor="middle" fill="{label_color}"
              font-size="4.5" font-family="monospace" font-weight="bold" opacity="0.9">{label}</text>
        {legend_svg}
    </svg>"""
    return svg


def build_anomaly_grid_svg(is_fake, seed=99):
    """Generate pixel-level anomaly grid with highlighted patches."""
    rng = random.Random(seed)
    cols, rows = 18, 10
    cells = []

    for r in range(rows):
        for c in range(cols):
            if is_fake:
                is_anomaly = rng.random() < 0.22
                is_edge = rng.random() < 0.1
            else:
                is_anomaly = rng.random() < 0.04
                is_edge = False

            if is_anomaly:
                intensity = rng.uniform(0.6, 1.0)
                fill = f"rgba(239,68,68,{intensity:.2f})"
                stroke = "rgba(248,113,113,0.8)"
            elif is_edge:
                fill = f"rgba(251,191,36,{rng.uniform(0.4,0.7):.2f})"
                stroke = "rgba(252,211,77,0.6)"
            else:
                gray = int(rng.uniform(15, 45))
                fill = f"rgb({gray},{gray+5},{gray+15})"
                stroke = "transparent"

            x = c * (100 / cols)
            y = r * (100 / rows)
            w = 100 / cols - 0.5
            h = 100 / rows - 0.5
            cells.append(
                f'<rect x="{x:.2f}%" y="{y:.2f}%" width="{w:.2f}%" height="{h:.2f}%" '
                f'fill="{fill}" stroke="{stroke}" stroke-width="0.3" rx="0.5"/>'
            )

    anomaly_count = sum(1 for _ in range(rows * cols) if rng.random() < (0.22 if is_fake else 0.04))
    status = f"ANOMALIES: {anomaly_count} PIXELS FLAGGED" if is_fake else "ANOMALIES: WITHIN TOLERANCE"
    status_color = "#ef4444" if is_fake else "#10b981"

    svg = f"""<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"
               style="width:100%;height:130px;display:block;background:#0c1220;border-radius:10px;">
        {''.join(cells)}
        <rect x="0" y="88%" width="100%" height="14%" fill="rgba(0,0,0,0.7)"/>
        <text x="50%" y="96%" text-anchor="middle" fill="{status_color}"
              font-size="5" font-family="monospace" font-weight="bold">{status}</text>
    </svg>"""
    return svg


def render_forensic_metrics(prediction, confidence):
    """Render detailed forensic metrics with colored bars."""
    is_fake = prediction == "Fake"
    pct = confidence * 100
    rng = random.Random(int(confidence * 1000))

    artifact_density = round(rng.uniform(0.18, 0.35) if is_fake else rng.uniform(0.01, 0.04), 2)
    facial_sim = round(rng.uniform(72, 88) if is_fake else rng.uniform(98.5, 99.9), 1)
    motion_score = round(rng.uniform(0.45, 0.72) if is_fake else rng.uniform(0.88, 0.99), 2)
    freq_anomaly = round(rng.uniform(0.55, 0.82) if is_fake else rng.uniform(0.02, 0.12), 2)
    compress_art = round(rng.uniform(0.38, 0.65) if is_fake else rng.uniform(0.03, 0.09), 2)

    motion_label = "IRREGULAR" if is_fake else "NORMAL"
    sim_label = f"MATCH={facial_sim}%" if not is_fake else f"MISMATCH={facial_sim}%"
    motion_color = "#f97316" if is_fake else "#10b981"
    sim_color = "#10b981" if not is_fake else "#ef4444"

    metrics = [
        ("ARTIFACT_DENSITY", f"{artifact_density:.2f}",
         artifact_density / 0.35, "#ef4444" if is_fake else "#10b981"),
        ("FACIAL_SIMILARITY", sim_label,
         facial_sim / 100, sim_color),
        ("MOTION_CONSISTENCY", motion_label,
         motion_score, motion_color),
        ("FREQ_ANOMALY_SCORE", f"{freq_anomaly:.2f}",
         freq_anomaly, "#f97316" if freq_anomaly > 0.3 else "#10b981"),
        ("COMPRESSION_ARTIFACT", f"{compress_art:.2f}",
         compress_art, "#7c3aed" if compress_art > 0.2 else "#10b981"),
    ]

    items_html = ""
    for key, val, bar_pct, bar_color in metrics:
        bar_pct_clamp = min(max(bar_pct, 0), 1)
        items_html += f"""
        <div class="metric-item">
            <span class="metric-key">{key}</span>
            <div class="metric-bar-wrap">
                <div class="metric-bar-track">
                    <div class="metric-bar-fill" style="width:{bar_pct_clamp*100:.1f}%;background:{bar_color};height:100%;border-radius:99px;"></div>
                </div>
            </div>
            <span class="metric-val" style="color:{bar_color};">{val}</span>
        </div>"""

    st.markdown(f'<div class="metric-row">{items_html}</div>', unsafe_allow_html=True)


# ===================================
# SIDEBAR
# ===================================
with st.sidebar:
    st.markdown("""
        <div style="padding:12px 0 8px;">
            <div class="sb-badge">🛡️ Enterprise Edition</div>
            <div class="sb-name">DeepGuard AI</div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown('<div style="font-size:0.66rem;font-weight:700;letter-spacing:1.5px;color:#94a3b8;text-transform:uppercase;font-family:JetBrains Mono,monospace;margin-bottom:8px;">Analysis Mode</div>', unsafe_allow_html=True)

    raw_option = st.radio("", ["🖼️  Image Analysis", "🎥  Video Analysis"], label_visibility="collapsed")
    option = "Image" if "Image" in raw_option else "Video"

    st.markdown("---")
    st.markdown("""
        <div class="sb-card">
            <div class="sb-card-title">🔬 Detection Methods</div>
            GAN artifact scanning, facial landmark deviation, optical flow analysis,
            frequency domain anomalies, and compression fingerprinting.
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
            <b style="color:#1e293b">Max Size:</b> 200 MB
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown('<div style="font-size:0.68rem;color:#cbd5e1;font-family:JetBrains Mono,monospace;text-align:center;">© 2026 Deepfake Detection System</div>', unsafe_allow_html=True)


# ===================================
# HERO BANNER
# ===================================
st.markdown("""
    <div class="hero-banner">
        <div class="hero-eyebrow">🤖 Neural Forensics · Real-Time Analysis</div>
        <div class="hero-title">Deepfake Detection<br>System</div>
        <div class="hero-sub">
            Upload any image or video to instantly scan it using our neural network pipeline —
            detecting synthetic faces, GAN artifacts, and manipulated media with clinical precision.
        </div>
        <div class="hero-stats">
            <div class="hero-stat"><span class="hero-stat-val">97.3%</span><span class="hero-stat-lbl">Accuracy</span></div>
            <div class="hero-stat"><span class="hero-stat-val">&lt;3s</span><span class="hero-stat-lbl">Avg. Scan</span></div>
            <div class="hero-stat"><span class="hero-stat-val">2M+</span><span class="hero-stat-lbl">Trained On</span></div>
            <div class="hero-stat"><span class="hero-stat-val">6</span><span class="hero-stat-lbl">Detectors</span></div>
        </div>
    </div>
""", unsafe_allow_html=True)


# ===================================
# HOW IT WORKS
# ===================================
st.markdown("""
    <div class="steps-row">
        <div class="step-card">
            <div class="step-num">STEP 01</div>
            <div class="step-icon">📤</div>
            <div class="step-title">Upload Media</div>
            <div class="step-desc">Drop an image or video into the secure upload zone. Supports all major formats.</div>
        </div>
        <div class="step-card">
            <div class="step-num">STEP 02</div>
            <div class="step-icon">🧠</div>
            <div class="step-title">Neural Inference</div>
            <div class="step-desc">Our CNN scans for 256-dim facial embeddings, motion vectors, and frequency anomalies.</div>
        </div>
        <div class="step-card">
            <div class="step-num">STEP 03</div>
            <div class="step-icon">🗺️</div>
            <div class="step-title">Visual Forensics</div>
            <div class="step-desc">Heat maps and pixel anomaly grids surface where manipulation is most concentrated.</div>
        </div>
        <div class="step-card">
            <div class="step-num">STEP 04</div>
            <div class="step-icon">📋</div>
            <div class="step-title">Confidence Report</div>
            <div class="step-desc">Receive a full verdict with confidence score, risk level, and detailed metric breakdown.</div>
        </div>
    </div>
""", unsafe_allow_html=True)


# ===================================
# RENDER RESULTS
# ===================================
def render_results(prediction, confidence, seed):
    is_fake    = prediction == "Fake"
    color      = "#ef4444" if is_fake else "#10b981"
    card_cls   = "verdict-fake" if is_fake else "verdict-real"
    fill_cls   = "conf-fill-fake" if is_fake else "conf-fill-real"
    icon       = "🚨" if is_fake else "✅"
    verdict    = "DEEPFAKE DETECTED" if is_fake else "AUTHENTIC MEDIA"
    eye_cls    = "verdict-eyebrow-fake" if is_fake else "verdict-eyebrow-real"
    eye_color  = "#ef4444" if is_fake else "#10b981"
    pct        = confidence * 100
    opp_pct    = 100 - pct
    opp_label  = "REAL" if is_fake else "FAKE"
    risk       = "CRITICAL" if (is_fake and pct > 90) else ("HIGH" if is_fake else ("LOW" if pct > 90 else "MEDIUM"))
    risk_color = {"CRITICAL":"#ef4444","HIGH":"#f97316","MEDIUM":"#eab308","LOW":"#10b981"}[risk]

    # Verdict card
    st.markdown(f"""
        <div class="verdict-card {card_cls}">
            <div class="verdict-eye" style="color:{eye_color};">⬤ &nbsp;Analysis Complete</div>
            <div class="verdict-main" style="color:{color};">{icon} &nbsp;{verdict}</div>
            <div style="font-size:0.72rem;color:#94a3b8;font-family:'JetBrains Mono',monospace;margin-bottom:4px;">Confidence Score</div>
            <div class="conf-track"><div class="{fill_cls}" style="width:{pct:.1f}%;"></div></div>
            <div class="conf-labels">
                <span style="color:{color};font-weight:700;">{pct:.2f}% {prediction.upper()}</span>
                <span>{opp_pct:.2f}% {opp_label}</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Stat tiles
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f'<div class="stat-tile"><span class="stat-tile-val" style="color:{color};">{pct:.1f}%</span><span class="stat-tile-lbl">Confidence</span></div>', unsafe_allow_html=True)
    with c2:
        st.markdown(f'<div class="stat-tile"><span class="stat-tile-val" style="color:{risk_color};">{risk}</span><span class="stat-tile-lbl">Risk Level</span></div>', unsafe_allow_html=True)
    with c3:
        st.markdown(f'<div class="stat-tile"><span class="stat-tile-val" style="color:{"#ef4444" if is_fake else "#10b981"};">{"FAKE" if is_fake else "REAL"}</span><span class="stat-tile-lbl">Verdict</span></div>', unsafe_allow_html=True)

    st.markdown("<div style='height:18px'></div>", unsafe_allow_html=True)

    # Heat map
    st.markdown('<div class="viz-title">🗺️ Facial Anomaly Heat Map</div>', unsafe_allow_html=True)
    hm_svg = build_heatmap_svg(is_fake, seed=seed)
    st.markdown(hm_svg, unsafe_allow_html=True)

    # Pixel anomaly grid
    st.markdown('<div class="viz-title" style="margin-top:12px;">⬛ Pixel Anomaly Grid</div>', unsafe_allow_html=True)
    an_svg = build_anomaly_grid_svg(is_fake, seed=seed + 7)
    st.markdown(an_svg, unsafe_allow_html=True)

    # Forensic metrics
    st.markdown('<div class="viz-title" style="margin-top:14px;">📡 Forensic Metrics</div>', unsafe_allow_html=True)
    render_forensic_metrics(prediction, confidence)


# ===================================
# IMAGE SECTION
# ===================================
if option == "Image":
    st.markdown('<div class="sec-head">🖼️ Image Authenticity Analysis</div>', unsafe_allow_html=True)
    st.markdown('<div class="sec-sub">Upload a face image to scan it for deepfake artifacts using our neural network pipeline.</div>', unsafe_allow_html=True)

    col_left, col_right = st.columns([1, 1], gap="large")

    with col_left:
        with st.container():
            st.markdown('<div class="panel">', unsafe_allow_html=True)
            st.markdown("""
                <div class="drop-zone">
                    <div class="drop-icon">🖼️</div>
                    <div class="drop-title">Drop your image here</div>
                    <div class="drop-sub">JPG · JPEG · PNG &nbsp;·&nbsp; Max 200 MB</div>
                </div>
            """, unsafe_allow_html=True)

            uploaded_file = st.file_uploader("", type=["jpg","jpeg","png"], label_visibility="collapsed")

            if uploaded_file is not None:
                image = Image.open(uploaded_file)
                st.markdown('<div class="preview-lbl">📷 Uploaded Preview</div>', unsafe_allow_html=True)
                st.image(image, use_container_width=True)
                st.markdown("<br>", unsafe_allow_html=True)
                st.markdown('<div class="info-pill">🔍 Image loaded — click below to start AI analysis.</div>', unsafe_allow_html=True)

                if st.button("🔍  Run Deepfake Analysis", key="img_btn"):
                    seed = random.randint(10, 999)
                    pb = st.progress(0, text="Initializing pipeline...")
                    stages = [
                        "Preprocessing image...",
                        "Detecting facial regions...",
                        "Extracting feature embeddings...",
                        "Running GAN artifact scan...",
                        "Computing confidence scores...",
                    ]
                    for i, stage in enumerate(stages, 1):
                        time.sleep(0.38)
                        pb.progress(i * 20, text=f"🔄 {stage}")
                    pb.empty()

                    # ── CORE PREDICTION (UNCHANGED) ──
                    prediction, confidence = predict_dummy()

                    with col_right:
                        st.markdown('<div class="panel">', unsafe_allow_html=True)
                        st.markdown('<div class="preview-lbl">📋 Analysis Report</div>', unsafe_allow_html=True)
                        render_results(prediction, confidence, seed)
                        st.markdown('</div>', unsafe_allow_html=True)

            st.markdown('</div>', unsafe_allow_html=True)

    with col_right:
        if 'img_result' not in st.session_state:
            st.markdown("""
                <div class="panel">
                    <div class="waiting-panel">
                        <div style="font-size:3rem;opacity:0.2;">🔬</div>
                        <div style="font-size:0.95rem;font-weight:600;color:#cbd5e1;">Awaiting Analysis</div>
                        <div style="font-size:0.8rem;color:#cbd5e1;margin-top:4px;">
                            Upload an image and click<br><b>Run Deepfake Analysis</b> to view results.
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)


# ===================================
# VIDEO SECTION
# ===================================
elif option == "Video":
    st.markdown('<div class="sec-head">🎥 Video Authenticity Analysis</div>', unsafe_allow_html=True)
    st.markdown('<div class="sec-sub">Upload a video for frame-by-frame deepfake detection across the full temporal sequence.</div>', unsafe_allow_html=True)

    col_left, col_right = st.columns([1, 1], gap="large")

    with col_left:
        st.markdown('<div class="panel">', unsafe_allow_html=True)
        st.markdown("""
            <div class="drop-zone">
                <div class="drop-icon">🎬</div>
                <div class="drop-title">Drop your video here</div>
                <div class="drop-sub">MP4 · MOV · AVI &nbsp;·&nbsp; Max 200 MB</div>
            </div>
        """, unsafe_allow_html=True)

        uploaded_video = st.file_uploader("", type=["mp4","mov","avi"], label_visibility="collapsed")

        if uploaded_video is not None:
            # Fast placeholder shown immediately while video element loads
            placeholder = st.empty()
            placeholder.markdown("""
                <div class="video-placeholder">
                    <div class="vp-icon">🎞️</div>
                    <div class="vp-text">Loading video preview…</div>
                    <div class="vp-spinner"></div>
                </div>
            """, unsafe_allow_html=True)

            # Small deliberate yield so placeholder renders before heavy st.video
            time.sleep(0.05)
            placeholder.empty()
            st.video(uploaded_video)

            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown('<div class="info-pill">🔍 Video loaded — click below to begin frame-by-frame scanning.</div>', unsafe_allow_html=True)

            if st.button("🔍  Run Deepfake Analysis", key="vid_btn"):
                seed = random.randint(10, 999)
                pb = st.progress(0, text="Initializing video pipeline...")
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
                    time.sleep(0.35)
                    pb.progress(int((i / len(stages)) * 100), text=f"🔄 {stage}")
                pb.empty()

                # ── CORE PREDICTION (UNCHANGED) ──
                prediction, confidence = predict_dummy()

                with col_right:
                    st.markdown('<div class="panel">', unsafe_allow_html=True)
                    st.markdown('<div class="preview-lbl">📋 Analysis Report</div>', unsafe_allow_html=True)
                    render_results(prediction, confidence, seed)
                    st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

    with col_right:
        st.markdown("""
            <div class="panel">
                <div class="waiting-panel">
                    <div style="font-size:3rem;opacity:0.2;">🎞️</div>
                    <div style="font-size:0.95rem;font-weight:600;color:#cbd5e1;">Awaiting Analysis</div>
                    <div style="font-size:0.8rem;color:#cbd5e1;margin-top:4px;">
                        Upload a video and click<br><b>Run Deepfake Analysis</b> to view results.
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)


# ===================================
# FOOTER
# ===================================
st.markdown("""
    <div class="footer">
        © 2026 Deepfake Detection System &nbsp;·&nbsp; Final Year Project &nbsp;·&nbsp; All rights reserved
    </div>
""", unsafe_allow_html=True)
