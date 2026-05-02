 
import streamlit as st

def load_css():
    st.markdown("""
    <style>
    /* Light Lavender Background */
    .stApp {
        background: linear-gradient(135deg, #f8f4ff 0%, #f0e8ff 50%, #e8d9ff 100%);
    }
    
    /* Main text color */
    h1, h2, h3, h4, h5, h6, p, li, span {
        color: #2d1b4e !important;
    }
    
    /* ===== TITLE STYLING ===== */
    .main-title {
        text-align: center;
        font-size: 2rem;
        font-weight: bold;
        background: linear-gradient(45deg, #8b5cf6, #d8b4fe);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 10px 0 5px 0;
        padding: 0;
    }
    
    /* ===== COMPACT LOGIN/REGISTER CONTAINER ===== */
    .compact-auth-container {
        max-width: 320px;
        margin: 20px auto;
        padding: 20px 25px;
        background: white;
        border-radius: 16px;
        box-shadow: 0 8px 20px rgba(139, 92, 246, 0.12);
        text-align: center;
    }
    
    .compact-auth-title {
        font-size: 1.4rem;
        font-weight: 600;
        text-align: center;
        margin-bottom: 20px;
        color: #4c1d95 !important;
    }
    
    /* Compact input fields */
    .compact-auth-container .stTextInput > div > div > input {
        padding: 8px 12px !important;
        font-size: 0.85rem !important;
        border: 1.5px solid #e9d5ff !important;
        border-radius: 10px !important;
        background: white !important;
        margin-bottom: 12px !important;
    }
    
    .compact-auth-container .stTextInput > div > div > input:focus {
        border-color: #8b5cf6 !important;
        box-shadow: 0 0 0 2px rgba(139, 92, 246, 0.1) !important;
    }
    
    /* Compact button */
    .compact-auth-container .stButton > button {
        background: linear-gradient(45deg, #8b5cf6, #a78bfa) !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 8px !important;
        font-weight: 600 !important;
        font-size: 0.9rem !important;
        width: 100%;
        margin: 5px 0 10px 0;
    }
    
    .compact-auth-container .stButton > button:hover {
        background: linear-gradient(45deg, #7c3aed, #8b5cf6) !important;
        transform: translateY(-1px);
    }
    
    /* Simple link text */
    .compact-auth-link {
        text-align: center;
        margin-top: 12px;
        color: #6b7280 !important;
        font-size: 0.8rem;
    }
    
    .compact-auth-link a {
        color: #8b5cf6 !important;
        text-decoration: none;
        font-weight: 600;
    }
    
    .compact-auth-link a:hover {
        text-decoration: underline;
    }
    
    /* ===== NAVBAR STYLING ===== */
    .navbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0.6rem 2rem;
        background: white;
        border-radius: 50px;
        box-shadow: 0 4px 6px rgba(139, 92, 246, 0.1);
        margin: 1rem 2rem;
    }
    
    .logo-text {
        font-size: 1.3rem;
        font-weight: bold;
        background: linear-gradient(45deg, #4a1d8c, #6a4cff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        display: inline-block;
    }
    
    /* Logo container */
    .logo-container {
        display: flex;
        align-items: center;
        gap: 12px;
    }
    
    .logo-icon {
        background: linear-gradient(45deg, #8b5cf6, #c084fc);
        width: 40px;
        height: 40px;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 4px 10px rgba(139, 92, 246, 0.3);
    }
    
    .logo-icon span {
        color: white;
        font-size: 1.5rem;
    }
    
    .nav-links {
        display: flex;
        gap: 1.5rem;
        align-items: center;
    }
    
    .nav-link {
        color: #4c1d95 !important;
        text-decoration: none;
        font-weight: 500;
        transition: all 0.3s ease;
        padding: 0.4rem 0.8rem;
        border-radius: 25px;
        cursor: pointer;
        background: transparent;
        border: none;
        font-size: 0.9rem;
    }
    
    .nav-link:hover {
        background: #f3e8ff;
        color: #8b5cf6 !important;
    }
    
    /* Security Level Colors */
    .security-low {
        background: #10b98120;
        color: #10b981 !important;
        border: 1px solid #10b981;
    }
    .security-medium {
        background: #f59e0b20;
        color: #f59e0b !important;
        border: 1px solid #f59e0b;
    }
    .security-high {
        background: #ef444420;
        color: #ef4444 !important;
        border: 1px solid #ef4444;
    }
    
    /* Clickable Link Styling */
    .qr-link {
        background: linear-gradient(45deg, #8b5cf6, #c084fc);
        color: white !important;
        padding: 10px 18px;
        border-radius: 10px;
        text-decoration: none;
        display: inline-block;
        margin: 10px 0;
        font-weight: bold;
        transition: all 0.3s ease;
        font-size: 0.9rem;
    }
    
    .qr-link:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(139, 92, 246, 0.4);
        text-decoration: none;
        color: white !important;
    }
    
    .upi-link {
        background: linear-gradient(45deg, #10b981, #34d399);
        color: white !important;
        padding: 10px 18px;
        border-radius: 10px;
        text-decoration: none;
        display: inline-block;
        margin: 10px 0;
        font-weight: bold;
        transition: all 0.3s ease;
        font-size: 0.9rem;
    }
    
    .upi-link:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(16, 185, 129, 0.4);
        text-decoration: none;
        color: white !important;
    }
    
    /* Model Prediction Cards */
    .model-card {
        background: linear-gradient(135deg, #8b5cf6, #c084fc);
        color: white !important;
        padding: 12px;
        border-radius: 10px;
        text-align: center;
        transition: all 0.3s ease;
    }
    
    .model-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(139, 92, 246, 0.3);
    }
    
    .model-card h4, .model-card p {
        color: white !important;
        font-size: 0.9rem;
        margin: 5px 0;
    }
    
    .model-card h2 {
        font-size: 1.5rem;
        margin: 5px 0;
    }
    
    /* Premium Features Cards */
    .premium-card {
        background: white;
        border: 1px solid #e9d5ff;
        border-radius: 20px;
        padding: 20px;
        box-shadow: 0 10px 30px rgba(139, 92, 246, 0.1);
        transition: all 0.3s ease;
    }
    
    .premium-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 40px rgba(139, 92, 246, 0.2);
        border-color: #c084fc;
    }
    
    /* Metric Cards */
    .metric-card {
        background: #f5f0ff;
        border: 1px solid #e9d5ff;
        border-radius: 15px;
        padding: 12px;
        text-align: center;
        transition: all 0.3s ease;
    }
    
    .metric-card:hover {
        background: #f0e6ff;
        transform: scale(1.02);
    }
    
    .metric-card h4 {
        color: #8b5cf6 !important;
        font-size: 0.9rem;
        margin: 0;
    }
    
    .metric-card h2 {
        color: #4c1d95 !important;
        font-size: 1.8rem;
        margin: 5px 0;
    }
    
    /* Gradient Text */
    .gradient-text {
        background: linear-gradient(45deg, #8b5cf6, #d8b4fe);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2rem;
        font-weight: bold;
    }
    
    /* Sidebar styling */
    .css-1d391kg, .css-1wrcr25 {
        background: white !important;
        box-shadow: 2px 0 15px rgba(139, 92, 246, 0.15);
    }
    
    .sidebar-user-info {
        background: #f5f0ff;
        padding: 15px;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 20px;
    }
    
    /* Sidebar Avatar */
    .sidebar-avatar {
        width: 70px;
        height: 70px;
        border-radius: 50%;
        margin: 0 auto 10px auto;
        display: flex;
        align-items: center;
        justify-content: center;
        background: linear-gradient(135deg, #8b5cf6, #c084fc);
        box-shadow: 0 5px 15px rgba(139, 92, 246, 0.3);
    }
    
    .sidebar-avatar span {
        color: white;
        font-size: 1.8rem;
        font-weight: bold;
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(45deg, #8b5cf6, #a78bfa) !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 8px 20px !important;
        font-weight: 500 !important;
        font-size: 0.9rem !important;
        box-shadow: 0 4px 6px rgba(139, 92, 246, 0.3) !important;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background: linear-gradient(45deg, #7c3aed, #8b5cf6) !important;
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(139, 92, 246, 0.4) !important;
    }
    
    /* Input fields */
    .stTextInput > div > div > input {
        background: white !important;
        border: 2px solid #e9d5ff !important;
        border-radius: 10px !important;
        color: #2d1b4e !important;
        padding: 10px !important;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #8b5cf6 !important;
        box-shadow: 0 0 0 3px rgba(139, 92, 246, 0.2) !important;
    }
    
    /* Tabs styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: white;
        padding: 8px;
        border-radius: 15px;
        border: 1px solid #e9d5ff;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: #f5f0ff;
        border-radius: 10px;
        padding: 6px 14px;
        color: #4c1d95 !important;
        font-size: 0.85rem;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(45deg, #8b5cf6, #a78bfa) !important;
        color: white !important;
    }
    
    /* Analytics Header */
    .analytics-header {
        text-align: center;
        margin-bottom: 30px;
    }
    
    .analytics-icon {
        background: linear-gradient(135deg, #8b5cf6, #c084fc);
        width: 80px;
        height: 80px;
        border-radius: 25px;
        margin: 0 auto 15px auto;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 10px 25px rgba(139, 92, 246, 0.3);
    }
    
    .analytics-icon span {
        color: white;
        font-size: 2.5rem;
    }
    
    /* Chart Icon Headers */
    .chart-header {
        display: flex;
        align-items: center;
        gap: 10px;
        margin-bottom: 15px;
    }
    
    .chart-icon {
        background: #8b5cf6;
        width: 40px;
        height: 40px;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    
    .chart-icon span {
        color: white;
        font-size: 1.2rem;
    }
    
    .chart-title {
        color: #4c1d95;
        margin: 0;
        font-size: 1.2rem;
        font-weight: 600;
    }
    </style>
    """, unsafe_allow_html=True)