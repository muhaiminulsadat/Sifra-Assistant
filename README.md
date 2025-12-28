# Sifra - AI Assistant with Memory & Roles 🤖

[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/) 
[![Streamlit](https://img.shields.io/badge/Streamlit-UI-orange.svg)](https://streamlit.io/) 
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A modular AI-powered assistant with **persistent conversation memory** and **role-based behavior**.  
Switch between **Tutor**, **Coding Assistant**, **Mentor**, or **General Assistant** to get tailored responses.

---

## ✨ Features

- 🧠 **Persistent Memory**: Retains conversation history across sessions.  
- 🎭 **Role-Based Personalities**: Tutor, Coder, Mentor, or General Assistant.  
- ⚡ **Streaming Responses**: Messages appear in real-time as the AI generates them.  
- 🔎 **Command Mode**: Execute predefined commands (e.g., open websites, run scripts).  
- 🛠 **Modular Architecture**: Clean OOP design for easy maintenance and extension.  
- 🌐 **Multi-Engine Support**: Works with OpenAI, Gemini API, or Groq API.

---

## 🛠 Tech Stack

- **Languages & Frameworks**
  - Python 3.10+  
  - Streamlit (UI & chat interface)  
  - OpenAI / Google Gemini API / Groq API (LLM integration)  
  - python-dotenv (environment management)  

- **Architecture**
  - Object-Oriented Programming (OOP)  
  - Modular design:
    - `memory.py` – manages chat history  
    - `prompt_controller.py` – builds dynamic prompts  
    - `engine.py` – interacts with AI engine  
    - `command_handler.py` – handles system commands  
    - `utility/utility.py` – helper functions (e.g., streaming text)

---

## 📦 Requirements

- Python 3.10 or higher  
- streamlit  
- openai / google-generativeai / groq-openai  
- python-dotenv  

Install dependencies:

```bash
pip install -r requirements.txt
```
## Project Structure

Sifra-Assistant/
│
├─ sifra/
│   ├─ __init__.py
│   ├─ engine.py
│   ├─ memory.py
│   ├─ prompt_controller.py
│   ├─ command_handler.py
│
├─ utility/
│   ├─ __init__.py
│   └─ utility.py
│
├─ app.py
├─ requirements.txt
├─ .env
└─ README.md

## 👤 Author

Muhaiminul Islam Sadat

AI & ML Enthusiast