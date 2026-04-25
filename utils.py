import streamlit as st
import pyttsx3
import os
import base64
import uuid

def _read_image_as_data_url(path: str) -> str | None:
    try:
        with open(path, "rb") as f:
            encoded = base64.b64encode(f.read()).decode("utf-8")
        ext = os.path.splitext(path)[1].lower().lstrip(".") or "png"
        mime = "png" if ext == "png" else ("jpeg" if ext in ("jpg", "jpeg") else ext)
        return f"data:image/{mime};base64,{encoded}"
    except Exception:
        return None

def apply_css():
    """Injects custom CSS for a premium dark neon theme and UI styling."""
    local_bg_path = os.path.join(os.path.dirname(__file__), "assets", "home_bg.png")
    cursor_uploaded_bg_path = (
        r"C:\Users\Nayanashree\.cursor\projects\c-Users-Nayanashree-OneDrive-Desktop-InterviewSense-AI\assets\c__Users_Nayanashree_AppData_Roaming_Cursor_User_workspaceStorage_63b1ce8b70f142bba92b9ec17a2690c1_images_image-e17b92da-e006-4856-9c14-ca9a340955f0.png"
    )
    bg_data_url = _read_image_as_data_url(local_bg_path) or _read_image_as_data_url(cursor_uploaded_bg_path)

    background_css = (
        f"""
            background-color: #020617 !important;
            background-image:
                radial-gradient(circle at 50% 38%, rgba(14, 165, 233, 0.22) 0%, rgba(2, 6, 23, 0.0) 48%),
                radial-gradient(circle at 78% 74%, rgba(37, 99, 235, 0.18) 0%, rgba(2, 6, 23, 0.0) 52%),
                linear-gradient(rgba(2, 6, 23, 0.48), rgba(2, 6, 23, 0.82)),
                url('{bg_data_url}') !important;
            background-size: cover, cover, cover, cover !important;
            background-position: center, center, center, center !important;
            background-repeat: no-repeat !important;
        """
        if bg_data_url
        else """
            background-color: #020617 !important;
            background-image:
                radial-gradient(circle at 85% 22%, rgba(56, 189, 248, 0.18) 0%, rgba(56, 189, 248, 0.0) 55%),
                radial-gradient(circle at 12% 45%, rgba(192, 132, 252, 0.14) 0%, rgba(192, 132, 252, 0.0) 60%),
                radial-gradient(circle at 18% 25%, rgba(56, 189, 248, 0.10) 0%, rgba(56, 189, 248, 0.0) 35%),
                radial-gradient(circle at 50% 35%, #061938 0%, #020617 70%),
                radial-gradient(circle at 20% 30%, rgba(255,255,255,0.10) 0 1px, transparent 2px),
                radial-gradient(circle at 75% 40%, rgba(255,255,255,0.08) 0 1px, transparent 2px),
                radial-gradient(circle at 40% 60%, rgba(255,255,255,0.06) 0 1px, transparent 2px),
                radial-gradient(circle at 60% 20%, rgba(255,255,255,0.06) 0 1px, transparent 2px);
            background-size:
                cover,
                cover,
                cover,
                cover,
                420px 420px,
                520px 520px,
                680px 680px,
                760px 760px;
            background-position:
                center,
                center,
                center,
                center,
                0 0,
                80px 120px,
                120px 40px,
                30px 200px;
            background-repeat: no-repeat !important;
        """
    )

    st.markdown("""
        <style>
        /* 1 & 2. FULL BACKGROUND COLOR FIX & REMOVE TOP WHITE GAP */
        html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
    """ + background_css + """
            background-attachment: fixed !important;
            color: #ffffff !important;
            font-family: 'Inter', sans-serif !important;
            margin: 0 !important;
            padding: 0 !important;
            min-height: 100vh !important;
            width: 100vw !important;
        }

        /* Add a soft global glow film to create depth on top of the background image */
        [data-testid="stAppViewContainer"]::before {
            content: "";
            position: fixed;
            inset: 0;
            pointer-events: none;
            z-index: 0;
            background:
                radial-gradient(circle at 50% 38%, rgba(14, 165, 233, 0.22) 0%, rgba(2, 6, 23, 0) 46%),
                radial-gradient(circle at 85% 20%, rgba(56, 189, 248, 0.14) 0%, rgba(2, 6, 23, 0) 40%),
                radial-gradient(circle at 10% 80%, rgba(147, 51, 234, 0.12) 0%, rgba(2, 6, 23, 0) 44%);
            mix-blend-mode: screen;
        }

        /* Keep app content above the glow layer */
        [data-testid="stAppViewContainer"] > .main,
        [data-testid="stAppViewContainer"] > header {
            position: relative;
            z-index: 1;
        }

        /* Make Streamlit top header transparent to remove white gap */
        [data-testid="stHeader"] {
            background-color: transparent !important;
        }

        /* 4. CENTER PERFECTLY & FULL SCREEN LAYOUT */
        .main .block-container {
            max-width: 850px !important;
            min-height: 100vh !important;
            display: flex !important;
            flex-direction: column !important;
            justify-content: center !important; /* Centers content vertically */
            align-items: center !important;
            padding: 2rem !important; /* Remove default top padding */
            margin: 0 auto !important;
            animation: fadeIn 0.8s ease-out;
        }

        /* SUBTLE ANIMATION */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(15px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        /* IMPROVE TEXT ALIGNMENT AND SPACING */
        h1, h2, h3 {
            color: #ffffff !important;
            text-align: center !important;
            margin-top: 0 !important;
            margin-bottom: 0.5rem !important; 
            text-shadow: 0 0 18px rgba(56, 189, 248, 0.22) !important;
        }
        
        p, .stMarkdown {
            color: #f8fafc !important;
            text-align: center !important;
            font-size: 1.1rem;
            line-height: 1.6;
            margin-bottom: 0.5rem !important; /* Reduced gap before button */
            width: 100%;
            text-shadow: 0 0 14px rgba(56, 189, 248, 0.14) !important;
        }

        .question-text {
            font-size: 2.5rem;
            font-weight: 800;
            text-align: center;
            margin-top: 0;
            margin-bottom: 2rem;
            color: #38bdf8 !important;
            text-shadow: 0 0 10px rgba(56, 189, 248, 0.3); 
        }

        /* 3. FIX BUTTON SPACING & DESIGN */
        .stButton {
            width: 100%;
            display: flex;
            justify-content: center;
            margin-top: 1rem !important;
            margin-bottom: 1rem !important;
        }

        button[kind="primary"] {
            background: linear-gradient(135deg, #2563eb, #0ea5e9) !important;
            color: #ffffff !important;
            font-weight: 900 !important;
            text-shadow: none !important;
            border-radius: 12px !important;
            border: 1px solid rgba(255, 255, 255, 0.2) !important;
            padding: 1.2rem 2.5rem !important;
            font-size: 1.4rem !important;
            letter-spacing: 1px !important;
            text-transform: uppercase !important;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
            box-shadow: 0 6px 20px rgba(14, 165, 233, 0.5) !important;
            width: 100% !important;
            max-width: 360px !important;
            display: block !important;
            margin: 0 auto !important;
        }

        button[kind="primary"]:hover {
            transform: scale(1.05) translateY(-2px) !important;
            filter: brightness(1.15) !important;
            box-shadow: 0 10px 30px rgba(14, 165, 233, 0.7) !important;
            color: #ffffff !important;
        }

        button[kind="primary"]:active {
            transform: scale(0.98) translateY(0) !important;
            box-shadow: 0 2px 8px rgba(6, 182, 212, 0.4) !important;
        }

        button[kind="secondary"] {
            background: rgba(255, 255, 255, 0.05) !important;
            color: #94a3b8 !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            border-radius: 8px !important;
            padding: 0.5rem 1rem !important;
            font-size: 0.9rem !important;
            font-weight: 600 !important;
            transition: all 0.3s ease !important;
            margin-bottom: 1rem !important;
            width: auto !important;
        }
        
        button[kind="secondary"]:hover {
            background: rgba(255, 255, 255, 0.1) !important;
            color: #ffffff !important;
            border-color: #38bdf8 !important;
        }

        /* Verdict colors */
        .verdict-Ready { color: #22c55e !important; font-weight: 800; font-size: 1.75rem; text-shadow: 0 0 10px rgba(34, 197, 94, 0.3); }
        .verdict-Improve { color: #f59e0b !important; font-weight: 800; font-size: 1.75rem; text-shadow: 0 0 10px rgba(245, 158, 11, 0.3); }
        .verdict-NotReady { color: #ef4444 !important; font-weight: 800; font-size: 1.75rem; text-shadow: 0 0 10px rgba(239, 68, 68, 0.3); }
        
        /* Metric values */
        div[data-testid="stMetricValue"] {
            color: #38bdf8 !important;
            font-size: 2.5rem !important;
            font-weight: 800 !important;
            text-align: center !important;
            text-shadow: 0 0 15px rgba(56, 189, 248, 0.4) !important;
        }
        div[data-testid="stMetricLabel"] {
            text-align: center !important;
            font-size: 1.1rem !important;
            color: #cbd5e1 !important;
        }
        
        /* Center image/camera input */
        .stImage {
            margin: 0 auto !important;
            max-width: 600px !important;
            border-radius: 16px !important;
            overflow: hidden !important;
            box-shadow: 0 10px 30px -5px rgba(0, 0, 0, 0.4) !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            display: flex;
            justify-content: center;
        }
        .stImage > img {
            border-radius: 16px !important;
            max-width: 100% !important;
        }

        /* 6. MEDIA QUERY FOR MOBILE RESPONSIVENESS */
        @media (max-width: 768px) {
            .main .block-container {
                padding: 1.5rem !important; /* Proper padding on left and right */
                padding-top: 5rem !important;
            }
            h1 { font-size: 2rem !important; }
            h2 { font-size: 1.75rem !important; }
            h3 { font-size: 1.5rem !important; }
            
            p, .stMarkdown {
                font-size: 1rem !important;
                padding-left: 0.5rem;
                padding-right: 0.5rem;
            }
            
            .question-text {
                font-size: 2rem !important;
                margin-bottom: 1.5rem !important;
            }
            
            .stButton > button {
                width: 100% !important;
                max-width: 100% !important; /* Make button full-width */
                padding: 1.2rem 1rem !important; /* Slightly larger height for touch */
                font-size: 1.1rem !important;
            }
            
            div[data-testid="stMetricValue"] {
                font-size: 2rem !important;
            }
            
            .custom-navbar {
                flex-wrap: wrap;
                padding: 0.5rem !important;
            }
            .custom-navbar a {
                margin: 0.5rem;
                font-size: 0.9rem;
            }
            .about-section {
                flex-direction: column !important;
            }
        }

        /* 7. SINGLE PAGE NAVIGATION UI CSS */
        html {
            scroll-behavior: smooth !important;
        }
        
        .main .block-container {
            padding-top: 5rem !important; /* Make room for fixed navbar */
        }
        
        /* Hide navbar class */
        .hide-navbar div[data-testid="stRadio"] {
            display: none !important;
        }

        /* Style st.radio as a navbar */
        div[data-testid="stRadio"] {
            position: fixed !important;
            top: 0 !important;
            left: 0 !important;
            width: 100% !important;
            z-index: 999999 !important;
            background: rgba(15, 23, 42, 0.85) !important;
            backdrop-filter: blur(10px) !important;
            padding: 1rem 0 !important;
            display: flex !important;
            justify-content: center !important;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1) !important;
            pointer-events: auto !important;
        }
        
        div[data-testid="stRadio"] > div[role="radiogroup"] {
            display: flex !important;
            flex-direction: row !important;
            justify-content: center !important;
            gap: 2rem !important;
            pointer-events: auto !important;
        }
        
        /* Make the radio option relatively positioned */
        div[data-testid="stRadio"] div[role="radio"] {
            position: relative !important;
            pointer-events: auto !important;
            display: flex;
            align-items: center;
        }

        /* Completely hide the radio circle SVG so only text remains */
        div[data-testid="stRadio"] label[data-baseweb="radio"] > div:first-child {
            display: none !important;
            opacity: 0 !important;
            width: 0 !important;
        }
        
        .stRadio div[role="radiogroup"] label > div:first-child {
            display: none !important;
        }

        /* Remove "Navigation" label if it appears */
        div[data-testid="stRadio"] > label {
            display: none !important;
        }
        
        /* Style text */
        div[data-testid="stRadio"] label {
            font-size: 1.1rem !important;
            font-weight: 600 !important;
            color: #cbd5e1 !important;
            cursor: pointer !important;
            padding: 0.5rem 1.5rem !important;
            transition: color 0.3s ease !important;
            margin: 0 !important;
            position: relative !important;
            pointer-events: auto !important;
            display: inline-block;
        }
        
        div[data-testid="stRadio"] label:hover {
            color: #38bdf8 !important;
        }

        /* Hover and active underline effect */
        div[data-testid="stRadio"] label::after {
            content: '';
            position: absolute;
            width: 0;
            height: 2px;
            display: block;
            margin-top: 5px;
            right: 0;
            bottom: 0;
            background: #38bdf8;
            transition: width 0.3s ease;
        }

        div[data-testid="stRadio"] label:hover::after,
        div[data-testid="stRadio"] label:has(input:checked)::after,
        div[data-testid="stRadio"] label[aria-checked="true"]::after,
        div[data-testid="stRadio"] div[role="radio"][aria-checked="true"] label::after {
            width: 100%;
            left: 0;
            background: #38bdf8;
        }
        
        /* Active state text color */
        div[data-testid="stRadio"] label:has(input:checked) p,
        div[data-testid="stRadio"] label[aria-checked="true"] p,
        div[data-testid="stRadio"] div[role="radio"][aria-checked="true"] label p {
            color: #38bdf8 !important;
        }

        /* SECTION STYLING */
        .page-section {
            padding-top: 3rem;
            padding-bottom: 3rem;
            width: 100%;
            display: flex;
            flex-direction: column;
            justify-content: center;
            flex-grow: 1;
            animation: fadeIn 0.6s cubic-bezier(0.4, 0, 0.2, 1);
        }

        .section-title {
            font-size: 2.2rem;
            font-weight: 800;
            color: #ffffff;
            text-align: center;
            margin-bottom: 2rem;
            letter-spacing: 1px;
        }

        /* About Section Flex Layout */
        .about-section {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 2rem;
            background: rgba(255, 255, 255, 0.03);
            padding: 2rem;
            border-radius: 16px;
            border: 1px solid rgba(255, 255, 255, 0.05);
        }
        
        .about-text {
            flex: 1;
            font-size: 1.1rem;
            line-height: 1.8;
            color: #e2e8f0;
            text-align: left !important;
        }

        .about-icon {
            flex: 1;
            text-align: center;
            font-size: 5rem;
            animation: float 4s ease-in-out infinite;
        }

        @keyframes float {
            0% { transform: translateY(0px); }
            50% { transform: translateY(-15px); }
            100% { transform: translateY(0px); }
        }

        /* Features Grid Layout */
        .features-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1.5rem;
            width: 100%;
            margin-top: 1rem;
        }

        .feature-card {
            background: rgba(255, 255, 255, 0.05);
            padding: 1.5rem;
            border-radius: 16px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            text-align: center;
            transition: all 0.3s ease;
        }

        .feature-card:hover {
            transform: translateY(-5px);
            background: rgba(255, 255, 255, 0.08);
            border-color: #38bdf8;
            box-shadow: 0 10px 25px rgba(56, 189, 248, 0.15);
        }

        .feature-icon {
            font-size: 2.5rem;
            margin-bottom: 1rem;
        }

        .feature-title {
            font-size: 1.2rem;
            font-weight: 700;
            color: #ffffff;
            margin-bottom: 0.5rem;
        }

        .feature-desc {
            font-size: 0.95rem;
            color: #94a3b8;
            line-height: 1.5;
        }

        /* Guidelines Styling */
        .guideline-list {
            list-style-type: none;
            padding-left: 0;
            text-align: left;
            margin: 0 auto;
            max-width: 800px;
        }
        
        .guideline-list li {
            margin-bottom: 0.8rem;
            padding-left: 1.5rem;
            position: relative;
            color: #e2e8f0;
            font-size: 1.05rem;
            line-height: 1.5;
        }
        
        .guideline-list li::before {
            content: "•";
            color: #38bdf8;
            font-weight: bold;
            font-size: 1.5rem;
            position: absolute;
            left: 0;
            top: -5px;
        }
        
        /* Interview Mode Badge */
        .mode-badge {
            display: inline-block;
            background: rgba(56, 189, 248, 0.15);
            border: 1px solid rgba(56, 189, 248, 0.4);
            color: #e0f2fe;
            padding: 0.4rem 1rem;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 600;
            letter-spacing: 0.5px;
            margin-bottom: 1.5rem;
            text-align: center;
            width: fit-content;
            margin-left: auto;
            margin-right: auto;
            box-shadow: 0 0 10px rgba(56, 189, 248, 0.2);
        }

        </style>
    """, unsafe_allow_html=True)

def speak_question(text):
    """
    Generates TTS audio for the given text using pyttsx3 and plays it automatically in Streamlit.
    Saving to a file avoids Streamlit threading/blocking issues with pyttsx3.
    """
    filename = f"temp_{uuid.uuid4().hex}.wav"
    try:
        engine = pyttsx3.init()
        # Set properties (optional)
        engine.setProperty('rate', 150)
        engine.save_to_file(text, filename)
        engine.runAndWait()
        
        # Read the audio file and create an HTML audio element with autoplay
        with open(filename, "rb") as f:
            audio_bytes = f.read()
        audio_base64 = base64.b64encode(audio_bytes).decode()
        audio_html = f'''
            <audio autoplay="true" style="display:none;">
                <source src="data:audio/wav;base64,{audio_base64}" type="audio/wav">
            </audio>
        '''
        st.markdown(audio_html, unsafe_allow_html=True)
    except Exception as e:
        st.error(f"TTS Error: {e}")
    finally:
        # Cleanup temp file if it exists
        if os.path.exists(filename):
            try:
                os.remove(filename)
            except:
                pass
