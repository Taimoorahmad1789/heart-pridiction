import base64
import os


def _get_bg_data_uri() -> str:
    # styles.py → ui/ folder mein hai
    # isliye 2 level upar jana hai project root tak
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    #           ↑ ui/ se upar     ↑ project root

    png_path = os.path.join(base_dir, "assets", "static", "background.png")

    print(f"Path: {png_path}")
    print(f"Exists: {os.path.exists(png_path)}")

    try:
        with open(png_path, "rb") as f:
            encoded = base64.b64encode(f.read()).decode("utf-8")
        return f"data:image/png;base64,{encoded}"
    except FileNotFoundError:
        print("❌ Image not found!")
        return ""

_BG_URI = _get_bg_data_uri()

# Background CSS
_BG_IMAGE_CSS = f"""
[data-testid="stAppViewContainer"], [data-testid="stApp"] {{
    background-image:
        linear-gradient(rgba(6, 13, 31, 0.85), rgba(6, 13, 31, 0.85)),
        url("{_BG_URI}") !important;
    background-size: cover !important;
    background-position: center !important;
    background-attachment: fixed !important;
    background-repeat: no-repeat !important;
}}
""" if _BG_URI else ""

PREMIUM_CSS = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

* {{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}}

/* ── Base Layout ── */
html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {{
    font-family: 'Inter', sans-serif;
    background: #060d1f !important;
    color: #e2e8f0 !important;
}}

{_BG_IMAGE_CSS}

/* ── UI Cleanup ── */
[data-testid="stAppViewContainer"] > .main, .main, section.main {{
    background: transparent !important;
}}

/* ── SYMPTOMS LABELS (White Color Fix) ── */
[data-testid="stWidgetLabel"] p, 
[data-testid="stWidgetLabel"] label,
.stSelectbox label p, 
.stSlider label p, 
.stNumberInput label p,
[data-testid="stNumberInput"] label p {{
    color: #ffffff !important;
    font-size: 1.05rem !important;
    font-weight: 600 !important;
    text-shadow: 0px 1px 2px rgba(0,0,0,0.5);
}}

/* ── PREMIUM DOWNLOAD BUTTON (Dark Blue Fix) ── */
[data-testid="stDownloadButton"] button,
.stDownloadButton > button {{
    background: linear-gradient(135deg, #0d1b3e 0%, #112240 60%, #0a2444 100%) !important;
    color: #ffffff !important;
    width: 100% !important;
    border-radius: 14px !important;
    font-weight: 700 !important;
    height: 55px !important;
    border: 1px solid rgba(0, 212, 255, 0.4) !important;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3) !important;
    transition: all 0.3s ease !important;
}}

.stDownloadButton > button:hover {{
    transform: translateY(-2px) !important;
    border-color: #00d4ff !important;
    box-shadow: 0 8px 25px rgba(0, 212, 255, 0.2) !important;
    background: #0a1628 !important;
}}

/* Download Button Text & Icon color */
.stDownloadButton > button p, .stDownloadButton > button span {{
    color: #ffffff !important;
}}

/* ── PRIMARY GENERATE BUTTON ── */
.stButton > button {{
    width: 100% !important;
    background: linear-gradient(135deg, #0057b8 0%, #0284c7 50%, #00d4ff 100%) !important;
    color: #ffffff !important;
    font-weight: 800 !important;
    height: 60px !important;
    border-radius: 16px !important;
    border: none !important;
    box-shadow: 0 8px 24px rgba(0, 132, 199, 0.4) !important;
}}

/* ── Sidebar ── */
[data-testid="stSidebar"] {{
    background: linear-gradient(180deg, #0d1b3e 0%, #0a1628 100%) !important;
}}

/* ── Responsive ── */
@media (max-width: 768px) {{
    .premium-header h1 {{ font-size: 2.2em; }}
}}
</style>
"""
