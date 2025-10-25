# frontend.py
import streamlit as st
import requests

# Page setup
st.set_page_config(
    page_title="LARS AI Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS for dark modern theme
st.markdown("""
<style>
body, .stApp {
    background-color: #0e1117;
    color: #f5f5f5;
    font-family: 'Segoe UI', sans-serif;
}
h1 {
    background: linear-gradient(90deg, #00ffd5, #00bba3);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-size: 3rem;
    text-align: center;
    margin-bottom: 5px;
}
h2,h3 {
    color: #00ffd5;
}
.sidebar .sidebar-content {
    background-color: #11141a;
    color: #f5f5f5;
}
.sidebar h2, .sidebar h3 {
    color: #00ffd5;
}
.card {
    background-color: #1c1c2a;
    padding: 25px;
    border-radius: 12px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.7);
    margin-bottom: 25px;
    transition: transform 0.3s, box-shadow 0.3s;
}
.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 25px rgba(0,0,0,0.9);
}
.stButton>button {
    background: linear-gradient(90deg, #00ffd5, #00bba3);
    color: #1c1c17;
    font-weight: bold;
    border-radius: 10px;
    padding: 10px 25px;
    font-size: 16px;
    transition: all 0.3s ease;
}
.stButton>button:hover {
    background: linear-gradient(90deg, #00bba3, #00ffd5);
    color: white;
}
.feature {
    font-size: 24px;
    color: #00ffd5;
    margin-right: 12px;
    vertical-align: middle;
}
.separator {
    height: 30px;
}
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("## LARS AI Assistant")
    st.markdown("Your AI-powered intelligence companion for any domain and role.")
    st.markdown("---")
    st.markdown("### Contact Info")
    st.markdown("📧 Email: support@larsai.com")
    st.markdown("📞 Phone: +91 9876543210")
    st.markdown("🌐 Website: [larsai.com](https://larsai.com)")
    st.markdown("---")
    st.markdown("### Quick Links")
    st.markdown("- About Us")
    st.markdown("- Try Domain Assistant")
    st.markdown("- Features")
    st.markdown("- Contact")

# Hero section
st.markdown("<h1>Welcome to LARS AI Assistant 🤖</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:20px; color:#ccc;'>Your AI companion that generates **personalized intelligence reports** for your industry and role. Stay ahead of trends, make smarter decisions, and leverage insights tailored just for you.</p>", unsafe_allow_html=True)

# About Us
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("### About LARS AI Assistant")
st.markdown(
    """
    LARS AI Assistant is a cutting-edge artificial intelligence designed to empower professionals, 
    researchers, and entrepreneurs with **accurate, real-time insights** in their domains.  
    It analyzes trends, provides actionable intelligence, and generates comprehensive reports 
    personalized to your role.  

    Whether you're exploring new market opportunities, preparing for strategic decisions, 
    or simply staying updated, LARS AI Assistant is your go-to partner for clarity and foresight.
    """
)
st.markdown("</div>", unsafe_allow_html=True)

# Features / Services
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("### Key Features")
st.markdown("""
<p><span class='feature'>💡</span> Real-time trend analysis</p>
<p><span class='feature'>📝</span> Personalized insights for your role</p>
<p><span class='feature'>🚀</span> Easy-to-use AI interface</p>
<p><span class='feature'>📊</span> Exportable professional reports</p>
<p><span class='feature'>⚡</span> Fast, reliable, and always up-to-date</p>
""", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# CTA button above form
st.markdown("<div style='text-align:center; margin-bottom:20px;'>", unsafe_allow_html=True)
if st.button("Try Domain Assistant"):
    st.session_state.show_assistant = True
st.markdown("</div>", unsafe_allow_html=True)

# Assistant form section
if "show_assistant" not in st.session_state:
    st.session_state.show_assistant = False

if st.session_state.show_assistant:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### Generate Your Domain Intelligence Report")
    
    API_URL = "https://lars-ai-backend-7.onrender.com"

    if "history" not in st.session_state:
        st.session_state.history = []

    with st.form("user_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Email Address")
        number = st.text_input("Phone Number")
        domain = st.text_input("Domain / Industry")
        role = st.text_input("Your Role in this Domain")
        submitted = st.form_submit_button("Generate Report")

    if submitted:
        if not domain.strip() or not role.strip():
            st.warning("Please enter both your domain and role.")
        else:
            try:
                payload = {
                    "name": name,
                    "email": email,
                    "number": number,
                    "domain": domain,
                    "role": role
                }
                response = requests.post(f"{API_URL}/generate", json=payload)
                data = response.json()
                answer = data.get("output", data.get("error", "No response"))
            except Exception as e:
                answer = f"Error contacting backend: {e}"

            st.session_state.history.append({
                "user": f"{name} ({email}, {number})\nDomain: {domain}\nRole: {role}",
                "ai": answer
            })

    # Display chat history
    for chat in st.session_state.history:
        st.markdown(f"**You:** {chat['user']}")
        st.markdown(f"**AI:** {chat['ai']}")
        st.markdown("---")
    st.markdown("</div>", unsafe_allow_html=True)
