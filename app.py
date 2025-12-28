import streamlit as st
from utility.utility import stream_text
from sifra.memory import Memory
from sifra.prompt_controller import PromptController
from sifra.engine import Engine
from sifra.command_handler import CommandHandler

# Configure page settings
st.set_page_config(
    page_title="Sifra - AI powered assistant", page_icon="🤖", layout="wide"
)

# Greeting & Title
st.title("🤖 Sifra - AI Assistant")
# st.write("👋 Hello! I'm Sifra, how can I help you today?")

# Sidebar Controls
st.sidebar.header("⚙️ Controls")
role = st.sidebar.selectbox(
    "Choose Role", ["General", "Command", "Tutor", "Coder", "Mentor"]
)

if st.sidebar.button("Clear Memory"):
    open("conversation.json", "w").write("[]")
    st.sidebar.success("Memory cleared!")

memory = Memory()
prompt_controller = PromptController(role=role)
engine = Engine()
command_handler = CommandHandler()

if not memory.get_history():
    st.chat_message("assistant").write_stream(
        stream_text("Hello! I'm Sifra 😊 How can I assist you today?")
    )

for msg in memory.get_history():
    st.chat_message(msg["role"]).write(msg["message"])


user_input = st.chat_input("Ask Sifra...")


# if user_input:
#     st.chat_message("user").write_stream(stream_text(user_input))

#     prompt = prompt_controller.build_prompt(user_input)
#     response = engine.groq_openai_response(prompt)

#     memory.add("user", user_input)
#     memory.add("assistant", response)

#     st.chat_message("assistant").write(response)

# Chat Input and Response
if user_input:
    st.chat_message("user").write(user_input)

    if role == "Command":
        # Handle command mode
        command_response = command_handler.handle(user_input)
        if command_response:
            st.chat_message("assistant").write(command_response)
        else:
            st.chat_message("assistant").write("❌ Unknown command.")
    else:
        # Assistant mode
        # Build prompt with memory
        prompt = prompt_controller.build_prompt(user_input)

        # Streamed response function (wrap your engine call here)
        def stream_response(prompt_text):
            response = engine.groq_openai_response(prompt_text)
            return response

        response = stream_response(prompt)

        # Save to memory
        memory.add("user", user_input)
        memory.add("assistant", response)

        # Role-based styling
        if role == "Tutor":
            st.chat_message("assistant").write(f"📘 {response}")
        elif role == "Coder":
            st.chat_message("assistant").code(response)
        elif role == "Mentor":
            st.chat_message("assistant").write(f"💼 {response}")
        else:
            st.chat_message("assistant").write(response)
