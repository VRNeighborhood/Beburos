# Beburos 🧠💪  
*A personal AI health companion built for daily wellness and recovery optimization.*

![License](https://img.shields.io/github/license/VRNeighborhood/beburos?style=flat-square)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg?style=flat-square)

---

## 🧠 What It Does

**Beburos** is a lightweight health agent that takes your daily metrics—like **sleep**, **strain**, and **recovery**—and returns smart, structured guidance using simple heuristics and LLM reasoning (via OpenAI).  

You can interact via:
- A **form-based check-in**
- A **chat-style mood interface**
- A **CLI for terminal users**

---

## 🔍 Features

- Manual input for WHOOP-style health metrics  
- Personalized recommendations in motivational, coach-like language  
- Gradio interfaces for both form and chat
- CSV + JSONL logging for insights over time  
- Modular core logic for future expansion (voice, sensors, etc.)

---

## ⚙️ Architecture

User → Gradio UI (form/chat) → Metric-to-prompt builder → OpenAI LLM → Personalized feedback → Logs

| Component         | Role                                              |
|------------------|---------------------------------------------------|
| `main.py`        | CLI entry point (mode: app, chat, checkin)        |
| `app.py`         | Combined app UI (form + chat)                     |
| `logic.py`       | Data handling, LLM prompt submission              |
| `beburos_core.py`| Health logic + LLM interface                      |
| `gradio_chat.py` | Mood-based chat UI                                |
| `checkin_app.py` | Daily check-in form only                          |
| `prompt_utils.py`| Prompt crafting from metrics                      |
| `helper.py`      | JSON/CSV logging and check-in retrieval           |

---
2. Install dependencies
pip install -r requirements.txt

3. Set your API key
OPENAI_API_KEY=your-key-here

4. Run the app
# Full UI (check-in + chat)
python main.py --mode app

# Standalone daily check-in
python main.py --mode checkin

# Standalone chat with mood input
python main.py --mode chat

🛠️ Project Structure
beburos/
├── app.py              # Unified interface
├── main.py             # Launcher
├── logic.py            # Core logic and handling
├── beburos_core.py     # ask_beburos() logic
├── gradio_chat.py      # Chat interface
├── checkin_app.py      # Health check-in UI
├── CLI_agent.py        # CLI-based input (optional)
├── llm.py              # LLM API connection
├── prompt_utils.py     # Prompt creation logic
├── helper.py           # Logging and file utilities
├── ui.py               # Gradio components
├── .gitignore
├── README.md
└── LICENSE

🛣️ Roadmap
✅ Current: Mood + health inputs to LLM

🔄 In Progress: Persistent chat memory

🔜 Coming Soon:

WHOOP API integration

Multi-day trend analysis

Supplement + training guidance

Guided recovery routines

Voice assistant mode

📄 License
Apache 2.0 License
© VRNeighborhood – Built for the NVIDIA Agent Intelligence Toolkit

If you like this project, consider giving it a ⭐ on GitHub!
