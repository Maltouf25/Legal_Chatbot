import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from models.model_registry import model_registry


# --- Page Configuration ---
st.set_page_config(page_title="Legal Chatbot", layout="wide")
# --- Model Selector Styling ---
st.markdown("""
    <style>
    .model-select-box {
        position: absolute;
        top: 20px;
        left: 20px;
        z-index: 9999;
        width: 200px;
    }
    </style>
""", unsafe_allow_html=True)

# --- Inject Bootstrap Icons ---
st.markdown("""
    <link
        rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css"
    />
""", unsafe_allow_html=True)

# --- Sidebar with icons ---
with st.sidebar:
    st.markdown("""
        <div style="font-size: 16px; line-height: 2;">
            <i class="bi bi-search"></i> &nbsp; <strong>Ask a Legal Question</strong><br>
            <i class="bi bi-upload"></i> &nbsp; <strong>Upload Document</strong><br>
            <i class="bi bi-clock-history"></i> &nbsp; <strong>Conversation History</strong><br>
            <i class="bi bi-folder2-open"></i> &nbsp; <strong>Legal Files</strong><br>
            <i class="bi bi-gear"></i> &nbsp; <strong>Settings</strong>
        </div>
        <hr style="margin-top: 1rem; margin-bottom: 1rem;">
        <small style="color: gray;">© 2025 LegalBot</small>
    """, unsafe_allow_html=True)

# --- Page Title with Icon ---
st.markdown("""
    <div style='display: flex; align-items: center; gap: 15px; margin-top: 10px;'>
        <i class="bi bi-shield-check" style="font-size: 40px; color: black;"></i>
        <h1 style='font-size: 40px; font-weight: 700; margin: 0;'>Legal Chatbot</h1>
    </div>
""", unsafe_allow_html=True)

# --- Custom Styling for Chat UI ---
st.markdown("""
    <style>
    html, body, [class*="css"] {
        height: 100%;
        margin: 0;
        padding: 0;
        font-family: 'Segoe UI', sans-serif;
        background-color: #FAFAFA;
    }

    .chat-container {
        max-height: calc(100vh - 180px);
        overflow-y: auto;
        padding-bottom: 100px;
        padding-left: 10px;
        padding-right: 10px;
    }

    .chatbox-wrapper {
        position: fixed;
        bottom: 20px;
        left: 50%;
        transform: translateX(-50%);
        width: 60%;
        max-width: 700px;
        background: white;
        padding: 12px 18px;
        border-radius: 30px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        z-index: 999;
    }

    .user-msg, .bot-msg {
        max-width: 75%;
        padding: 12px;
        margin: 10px;
        border-radius: 30px;
        line-height: 1.5;
        font-size: 15px;
    }

    .user-msg {
        background-color: #f1f0f0;
        margin-left: auto;
    }

    .bot-msg {
        
        margin-right: auto;
    }
    </style>
""", unsafe_allow_html=True)

# --- Session State for Messages ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- Chat Display Area ---
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
for msg in st.session_state.messages:
    role_class = "user-msg" if msg["role"] == "user" else "bot-msg"
    st.markdown(f'<div class="{role_class}">{msg["content"]}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- Fixed Chat Input at Bottom ---
st.markdown('<div class="chatbox-wrapper">', unsafe_allow_html=True)
user_input = st.chat_input("Ask your legal question here...")
st.markdown('</div>', unsafe_allow_html=True)


with st.container():
    st.markdown('<div class="model-select-box">', unsafe_allow_html=True)
    model_name = st.selectbox(
        "Model:",
        ["Embedding_Model", "GPT_model"],
        label_visibility="collapsed"  # hide the label to make it cleaner
    )
    model = model_registry[model_name]()
    st.markdown('</div>', unsafe_allow_html=True)
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    response = model.answer(user_input)
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.rerun()
