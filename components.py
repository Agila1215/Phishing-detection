 
import streamlit as st

def navbar():
    col1, col2 = st.columns([1, 3])
    with col1:
        st.markdown("""
        <div class="logo-container">
            <div class="logo-icon">
                <span>🛡️</span>
            </div>
            <div class="logo-text">AI QR Shield</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        cols = st.columns(6)
        with cols[0]:
            if st.button("🏠 Home", key="nav_home", width='stretch'):
                st.session_state.page = 'home'
                st.query_params["page"] = "home"
                st.rerun()
        with cols[1]:
            if st.button("📖 About", key="nav_about", width='stretch'):
                st.session_state.page = 'about'
                st.query_params["page"] = "about"
                st.rerun()
        with cols[2]:
            if st.button("⚙️ Services", key="nav_services", width='stretch'):
                st.session_state.page = 'services'
                st.query_params["page"] = "services"
                st.rerun()
        with cols[3]:
            if st.button("📞 Contact", key="nav_contact", width='stretch'):
                st.session_state.page = 'contact'
                st.query_params["page"] = "contact"
                st.rerun()
        with cols[4]:
            if st.button("🔐 Login", key="nav_login", width='stretch'):
                st.session_state.page = 'login'
                st.query_params["page"] = "login"
                st.rerun()
        with cols[5]:
            if st.button("📝 Register", key="nav_register", width='stretch'):
                st.session_state.page = 'register'
                st.query_params["page"] = "register"
                st.rerun()

def about_page():
    st.markdown("""
    <div class="about-section" style="display: flex; align-items: center; gap: 3rem; padding: 2rem; margin: 1rem; background: white; border-radius: 30px; box-shadow: 0 15px 30px rgba(139, 92, 246, 0.1);">
        <div style="flex: 1;">
            <h2 style="color: #4c1d95;">About Us</h2>
            <p style="color: #4b5563; line-height: 1.6;">
                AI QR Shield is an advanced QR code security scanner powered by artificial intelligence. 
                Our mission is to protect users from phishing attacks and malicious QR codes through real-time 
                analysis and multi-model machine learning predictions.
            </p>
            <p style="color: #4b5563; line-height: 1.6;">
                With support for both website URLs and UPI payment QR codes, we provide comprehensive security 
                analysis with risk scoring, security level detection, and detailed reports.
            </p>
        </div>
        <div style="flex: 1; text-align: center;">
            <div style="font-size: 6rem;">🛡️</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def services_page():
    st.markdown("""
    <div style="padding: 2rem; text-align: center;">
        <h2 style="color: #4c1d95;">Our Services</h2>
        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5rem; margin-top: 2rem;">
            <div style="background: white; padding: 1.5rem; border-radius: 20px; box-shadow: 0 10px 25px rgba(139, 92, 246, 0.1);">
                <div style="font-size: 2rem;">📱</div>
                <h3 style="color: #4c1d95;">QR Code Scanning</h3>
                <p style="color: #6b7280;">Scan any QR code instantly with our advanced decoder supporting multiple formats</p>
            </div>
            <div style="background: white; padding: 1.5rem; border-radius: 20px; box-shadow: 0 10px 25px rgba(139, 92, 246, 0.1);">
                <div style="font-size: 2rem;">🛡️</div>
                <h3 style="color: #4c1d95;">Phishing Detection</h3>
                <p style="color: #6b7280;">Identify malicious URLs and protect your sensitive data from cyber attacks</p>
            </div>
            <div style="background: white; padding: 1.5rem; border-radius: 20px; box-shadow: 0 10px 25px rgba(139, 92, 246, 0.1);">
                <div style="font-size: 2rem;">💰</div>
                <h3 style="color: #4c1d95;">UPI Verification</h3>
                <p style="color: #6b7280;">Verify UPI payment QR codes before scanning to avoid payment scams</p>
            </div>
            <div style="background: white; padding: 1.5rem; border-radius: 20px; box-shadow: 0 10px 25px rgba(139, 92, 246, 0.1);">
                <div style="font-size: 2rem;">📊</div>
                <h3 style="color: #4c1d95;">Analytics Dashboard</h3>
                <p style="color: #6b7280;">Track your scan history and threat patterns with interactive charts</p>
            </div>
            <div style="background: white; padding: 1.5rem; border-radius: 20px; box-shadow: 0 10px 25px rgba(139, 92, 246, 0.1);">
                <div style="font-size: 2rem;">📧</div>
                <h3 style="color: #4c1d95;">Email Reports</h3>
                <p style="color: #6b7280;">Share scan results via email with detailed analysis</p>
            </div>
            <div style="background: white; padding: 1.5rem; border-radius: 20px; box-shadow: 0 10px 25px rgba(139, 92, 246, 0.1);">
                <div style="font-size: 2rem;">📱</div>
                <h3 style="color: #4c1d95;">WhatsApp Sharing</h3>
                <p style="color: #6b7280;">Share results directly on WhatsApp with one click</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def contact_page():
    st.markdown("""
    <div style="padding: 2rem; margin: 1rem; background: white; border-radius: 30px; box-shadow: 0 15px 30px rgba(139, 92, 246, 0.1); text-align: center;">
        <h2 style="color: #4c1d95;">Contact Us</h2>
        <p style="color: #4b5563; margin-bottom: 2rem;">Have questions or need support? Reach out to us!</p>
        <div style="font-size: 1.1rem; margin: 1rem 0;">
            📧 <span style="color: #8b5cf6; font-weight: bold;">qrcodeprojectphishing@gmail.com</span>
        </div>
    </div>
    """, unsafe_allow_html=True)