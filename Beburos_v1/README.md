# 🧠 Beburos – AI Health Companion

Beburos is a personal health agent that transforms your daily physiological inputs — such as sleep, recovery, and strain — into smart, structured wellness recommendations using GPT-4.

Built with Gradio, OpenAI, and Python 3.11.

---

## 📦 Features

- ✅ Manual input of WHOOP-style metrics  
- ✅ Personalized guidance via OpenAI (GPT-4)  
- ✅ Friendly chat or structured check-in mode  
- ✅ Modular design for easy customization  
- ✅ Clean architecture, log tracking, `.env` support

---

## 🛠️ Project Structure

```plaintext
beburos/
├── main.py               # Launch entry point (app/chat/checkin)
├── app.py                # Unified Gradio interface
├── ui.py                 # Gradio components (check-in + chat)
├── logic.py              # Submission logic + check-in handling
├── beburos_core.py       # Central prompt + LLM brain
├── prompt_utils.py       # Formats prompts from metrics
├── llm.py                # Handles GPT-4 interaction
├── helper.py             # Log utils + check-in loader
├── CLI_agent.py          # (Optional) terminal-mode access
├── archive/
│   ├── checkin_app.py
│   ├── gradio_app.py
│   └── gradio_chat.py
├── logs/                 # Check-in history (ignored in Git)
│   └── .gitkeep
├── .env                  # (User-provided) OpenAI key (not tracked)
├── .gitignore            # Ensures clean version control
├── requirements.txt      # Frozen working dependencies
└── README.md             # You are here


### 1. Create and activate a virtual environment (Python 3.11)

```bash
py -3.11 -m venv venv311
.\venv311\Scripts\Activate.ps1

### 2. Install dependencies
    pip install -r requirements.txt

### 3. Add your OpenAI key
    OPENAI_API_KEY=your-openai-key-here

🚀 How to Run Beburos
🟦 Option 1: Windows Users – Double-click to launch
Use the included launch.bat:
    📁 BEBUROS/
    ├── launch.bat ← Double-click this file to run the full UI
It activates the virtual environment and runs Beburos.

🖥️ Option 2: Command-Line (Git Bash or terminal)
    make run

Other commands:
    make install     # Create venv + install dependencies
    make clean        # Remove venv + cache files
📝 Requires make to be installed (works best in Git Bash or WSL)

🔑 API Key Reminder
You’ll need a .env file containing:
    OPENAI_API_KEY=your-openai-key

🧾 Logs & Privacy
    Check-ins are logged to logs/checkins.jsonl
    The logs/ folder is .gitignored
    A .gitkeep ensures the folder remains in the repo without logs

🧹 Developer Notes
    Legacy files are stored in the archive/ folder
    .pyc, .env, venv/, and logs are excluded from Git
    Runs cleanly with Python 3.11 and a locked requirements.txt

🌐 Deployment Ready
You can deploy Beburos on:
    Hugging Face Spaces (Gradio-ready)
    Streamlit Cloud (with minor UI adaptation)
    Local server or private health tools

🤝 License
    MIT License © 2025 VRNeighborhood
    Built for the NVIDIA Agent Intelligence Toolkit Challenge

---


