import streamlit as st

# Configure page settings
st.set_page_config(
    page_title="Sifra - AI powered assistant", page_icon="🤖", layout="wide"
)

# Greeting & Title
st.title("🤖 Sifra - AI Assistant")
st.write("👋 Hello! I'm Sifra, how can I help you today?")

# Sidebar Controls
st.sidebar.header("⚙️ Controls")
role = st.sidebar.selectbox("Choose MEHU Role", ["General", "Command", "Tutor", "Coder", "Mentor"])
