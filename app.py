import streamlit as st

# ==============================
# PAGE CONFIG
# ==============================
st.set_page_config(
    page_title="Wisdom Agbom | Web3 Developer",
    page_icon="🚀",
    layout="wide"
)

# ==============================
# PREMIUM CSS
# ==============================
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #0f172a, #020617);
    color: white;
    font-family: Arial, sans-serif;
}

/* HERO */
.hero {
    text-align: center;
    padding: 40px;
}

.hero-name {
    font-size: 50px;
    font-weight: bold;
    background: linear-gradient(90deg, #00f5ff, #9333ea);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-sub {
    font-size: 20px;
    color: #94a3b8;
}

/* GLASS CARD */
.glass {
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(10px);
    border-radius: 20px;
    padding: 25px;
    margin-top: 30px;
}

/* SKILLS */
.skill-bar {
    background: rgba(255,255,255,0.1);
    border-radius: 10px;
    margin-bottom: 15px;
}

.skill-fill {
    background: linear-gradient(90deg, #00f5ff, #9333ea);
    height: 15px;
    border-radius: 10px;
}

/* SOCIAL BUTTONS */
.social-btn {
    display: block;
    width: 100%;
    padding: 18px;
    margin-bottom: 20px;
    border-radius: 15px;
    font-size: 20px;
    font-weight: bold;
    text-align: center;
    text-decoration: none;
    color: white;
    transition: 0.3s ease;
}

.email-btn { background: linear-gradient(90deg, #06b6d4, #0ea5e9); }
.x-btn { background: linear-gradient(90deg, #9333ea, #6366f1); }
.whatsapp-btn { background: linear-gradient(90deg, #22c55e, #16a34a); }

.social-btn:hover {
    transform: scale(1.05);
    box-shadow: 0px 0px 30px rgba(147,51,234,0.8);
}

/* FOOTER */
.footer {
    text-align: center;
    margin-top: 50px;
    color: #64748b;
}
</style>
""", unsafe_allow_html=True)

# ==============================
# SIDEBAR NAVIGATION
# ==============================
st.sidebar.title("🚀 Navigation")
page = st.sidebar.radio("", ["Home", "About", "Skills", "Projects", "Contact"])

# ==============================
# HOME
# ==============================
if page == "Home":
    st.markdown("""
    <div class="hero">
        <div class="hero-name">Wisdom Agbom</div>
        <div class="hero-sub">Web3 Enthusiast | Python Developer | Crypto Researcher</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="glass">
        🚀 Building decentralized solutions and exploring blockchain innovation.<br><br>
        💡 Focused on AI, Automation & Crypto Intelligence.
    </div>
    """, unsafe_allow_html=True)

# ==============================
# ABOUT
# ==============================
elif page == "About":
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.markdown("""
    ### About Me
    Hi, I'm **Wisdom Agbom** — a driven Web3 enthusiast and Python developer passionate about building in the decentralized ecosystem.
    
    My journey started with curiosity about blockchain and crypto systems and evolved into actively researching on-chain opportunities, automation tools, and emerging Web3 technologies.
    
    I specialize in:
    - 🚀 Web3 & Airdrop Research
    - 🐍 Python Development & Automation
    - 📊 Crypto Analysis & Portfolio Tracking
    - 🤖 AI & Machine Learning Fundamentals
    
    I believe in continuous learning, consistency, and leveraging decentralized technologies to create financial and technological freedom.
    
    Currently open to collaborations, internships, and Web3 opportunities where I can contribute, learn, and grow.
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ==============================
# SKILLS
# ==============================
elif page == "Skills":
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.markdown("### Technical Skills")

    skills = {
        "Python": 90,
        "Web3 Research": 85,
        "AI / ML": 75,
        "Automation": 80
    }

    for skill, level in skills.items():
        st.markdown(f"{skill}")
        st.markdown(f"""
        <div class="skill-bar">
            <div class="skill-fill" style="width:{level}%"></div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ==============================
# PROJECTS
# ==============================
elif page == "Projects":
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.markdown("""
    ### Projects

    🚀 **Web3 Airdrop Tracker** – Track eligibility & optimize farming strategies.

    📊 **Crypto Portfolio Tracker** – Monitor and analyze digital assets.

    🤖 **Automation Scripts** – Improve workflow efficiency with Python tools.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ==============================
# CONTACT
# ==============================
elif page == "Contact":
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.markdown("### Let’s Connect 🚀")

    st.markdown("""
    <a href="mailto:wisdomagbom9@gmail.com" class="social-btn email-btn">📧 Email Me</a>
    <a href="https://x.com/WizHumble999" target="_blank" class="social-btn x-btn">🐦 Follow on X</a>
    <a href="https://wa.me/message/DPSYTKTDLTT7P1" target="_blank" class="social-btn whatsapp-btn">💬 WhatsApp Me</a>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ==============================
# FOOTER
# ==============================
st.markdown('<div class="footer">© 2026 Wisdom Agbom | Built with Streamlit</div>', unsafe_allow_html=True)