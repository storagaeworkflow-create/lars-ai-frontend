# frontend.py
import streamlit as st
import requests

st.set_page_config(page_title="LARS AI Assistant", page_icon="🤖")
st.title("LARS AI Assistant 🤖")
st.markdown("Get a detailed intelligence report for your domain and role.")

# Backend API URL
API_URL = "https://lars-ai-frontend.onrender.com"  # Update if using Cloudflare/VPS

# Chat history
if "history" not in st.session_state:
    st.session_state.history = []

# User input form
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
            response = requests.post(API_URL, json=payload)
            data = response.json()
            answer = data.get("output", data.get("error", "No response"))
        except Exception as e:
            answer = f"Error contacting backend: {e}"

        # Save chat history
        st.session_state.history.append({
            "user": f"{name} ({email}, {number})\nDomain: {domain}\nRole: {role}",
            "ai": answer
        })

# Display chat history
for chat in st.session_state.history:
    st.markdown(f"**You:** {chat['user']}")
    st.markdown(f"**AI:** {chat['ai']}")
    st.markdown("---")
