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
├── archive/              # Legacy files (not used in core app)
├── logs/                 # Check-in history (ignored in Git)
│   └── .gitkeep
├── .env                  # (User-provided) OpenAI key (not tracked)
├── .gitignore            # Ensures clean version control
├── requirements.txt      # Frozen working dependencies
└── README.md             # You are here

⚙️ Installation
1. 🧪 Create and activate a virtual environment (Python 3.11)

py -3.11 -m venv venv311
.\venv311\Scripts\Activate.ps1

2. 📦 Install dependencies

pip install -r requirements.txt

3. 🔑 Create a .env file with your OpenAI key

OPENAI_API_KEY=your-openai-key-here

🚀 Usage
Run the full Beburos app (check-in + chat):

python main.py --mode app

Optional modes:
python main.py --mode checkin   # Health check-in form only
python main.py --mode chat      # Chat-only mood interface
python CLI_agent.py             # Lightweight CLI interface

🧾 Logs & Privacy
Check-ins are logged to logs/checkins.jsonl, but the logs/ folder is .gitignored.
To preserve the folder in Git, a .gitkeep is used.

🧹 Developer Notes
Old experimental files are in the archive/ folder
All .pyc, .env, venv, and logs are excluded from version control
This repo runs cleanly in any environment using Python 3.11

🌐 Deployment Ready
You can deploy this on:
Hugging Face Spaces (Gradio-ready)
Streamlit Cloud (with minor UI adaptation)
Local server or internal health dashboards

🤝 License
MIT License © 2025 VRNeighborhood
Built for the NVIDIA Agent Intelligence Toolkit Challenge

Want to expand Beburos with wearable integrations, supplement guidance, or mood-driven protocol shifts? Fork it and let's collaborate!
Would you like this saved directly to your repo as `README.md` and committed? I can also generate a `Makefile` or deployment config next.
