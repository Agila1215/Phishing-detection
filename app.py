 
import streamlit as st
import time
from streamlit_option_menu import option_menu

from frontend.styles import load_css
from frontend.components import navbar, about_page, services_page, contact_page
from frontend.pages import (
    home_page, login_page, register_page, 
    qr_scanner_page, dashboard_page, analytics_page,
    profile_page, admin_panel
)
from backend.database import init_database
from backend.models import train_models

# Page config must be first
st.set_page_config(
    page_title="AI QR Shield",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load CSS
load_css()

# Initialize database
init_database()

# Train models globally
models = train_models()

# Session state initialization
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
    st.session_state.user = None
    st.session_state.page = 'home'
    st.session_state.auth_tab = 'login'

def navigation():
    with st.sidebar:
        st.markdown("""
        <div style="text-align: center; padding: 15px;">
            <div style="background: linear-gradient(45deg, #8b5cf6, #c084fc); width: 50px; height: 50px; border-radius: 15px; margin: 0 auto 10px auto; display: flex; align-items: center; justify-content: center;">
                <span style="color: white; font-size: 1.8rem;">🛡️</span>
            </div>
            <h1 class="gradient-text" style="font-size: 1.5rem;">AI QR Shield</h1>
            <p style="color: #8b5cf6; font-weight: 500; font-size: 0.8rem;">Premium Security System</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.session_state.authenticated:
            full_name = st.session_state.user['full_name']
            initials = ''.join(word[0].upper() for word in full_name.split()[:2]) if full_name else "U"
            
            st.markdown(f"""
            <div class="sidebar-user-info">
                <div class="sidebar-avatar">
                    <span>{initials}</span>
                </div>
                <h3 style="color: #4c1d95; margin-top: 8px; font-size: 1rem;">{st.session_state.user['full_name']}</h3>
                <p style="color: #8b5cf6; font-weight: 500; font-size: 0.7rem;">{'👑 Admin' if st.session_state.user['is_admin'] else '👤 User'}</p>
            </div>
            """, unsafe_allow_html=True)
        
        options = ['Home', 'QR Scanner', 'Dashboard', 'Analytics', 'Profile'] + \
                  (['Admin Panel'] if st.session_state.authenticated and st.session_state.user['is_admin'] else []) + \
                  ['Logout']
        
        icons = ['house', 'qr-code-scan', 'bar-chart', 'graph-up', 'person'] + \
                (['shield-lock'] if st.session_state.authenticated and st.session_state.user['is_admin'] else []) + \
                ['box-arrow-right']
        
        selected = option_menu(
            menu_title=None,
            options=options,
            icons=icons,
            menu_icon="cast",
            default_index=0,
            styles={
                "container": {"padding": "0!important", "background-color": "transparent"},
                "icon": {"color": "#8b5cf6", "font-size": "18px"},
                "nav-link": {
                    "font-size": "14px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#f3e8ff",
                    "color": "#4c1d95"
                },
                "nav-link-selected": {
                    "background": "linear-gradient(45deg, #8b5cf6, #c084fc)",
                    "color": "white"
                },
            }
        )
        return selected

def main():
    if 'page' not in st.session_state:
        st.session_state.page = 'home'
    
    query_params = st.query_params
    url_page = query_params.get("page", st.session_state.page)
    
    if url_page != st.session_state.page:
        st.session_state.page = url_page
    
    if not st.session_state.authenticated:
        navbar()
        if st.session_state.page == "login":
            login_page()
        elif st.session_state.page == "register":
            register_page()
        elif st.session_state.page == "about":
            about_page()
        elif st.session_state.page == "services":
            services_page()
        elif st.session_state.page == "contact":
            contact_page()
        else:
            st.session_state.page = 'home'
            home_page()
    else:
        selected = navigation()
        if selected == 'Home':
            from frontend.pages.home import home_page_auth
            home_page_auth()
        elif selected == 'QR Scanner':
            qr_scanner_page()
        elif selected == 'Dashboard':
            dashboard_page()
        elif selected == 'Analytics':
            analytics_page()
        elif selected == 'Profile':
            profile_page()
        elif selected == 'Admin Panel':
            admin_panel()
        elif selected == 'Logout':
            st.session_state.authenticated = False
            st.session_state.user = None
            st.session_state.page = 'home'
            st.query_params["page"] = "home"
            st.rerun()

if __name__ == '__main__':
    main()