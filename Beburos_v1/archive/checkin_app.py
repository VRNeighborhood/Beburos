# checkin_app.py - Daily Health Check-In UI

CHAT_URL = "http://127.0.0.1:7860"

import subprocess
import webbrowser
import threading
import gradio as gr
import json
import os
from datetime import datetime
from gradio_chat import demo as chat_ui

# === Define Log File Path ===
CHECKIN_LOG_FOLDER = "logs"
CHECKIN_LOG_FILE = os.path.join(CHECKIN_LOG_FOLDER, "checkins.jsonl")

# === Ensure logs/ folder exists ===
os.makedirs(CHECKIN_LOG_FOLDER, exist_ok=True)

# === Function to save the check-in ===
def save_checkin(date, wake_time, sleep_score, restorative_sleep, hours_sleep,
                 hrv, rhr, recovery_score, strain, resp_rate, mental, physical, notes):

    entry = {
        "timestamp": datetime.now().isoformat(),
        "date": date,
        "wake_time": wake_time,
        "sleep_score": sleep_score,
        "restorative_sleep": restorative_sleep,
        "hours_sleep": hours_sleep,
        "hrv": hrv,
        "rhr": rhr,
        "recovery_score": recovery_score,
        "strain": strain,
        "respiratory_rate": resp_rate,
        "mental_status": mental,
        "physical_status": physical,
        "notes": notes
    }

    with open(CHECKIN_LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")

    return "✅ Check-in saved!"

# === Build the Gradio Form ===
with gr.Blocks() as checkin_ui:
    gr.Markdown("""
    ## 📋 Daily Health Check-In
    Enter your key metrics and notes for the day.
    """)

    with gr.Row():
        date = gr.Text(label="📅 Date", value=str(datetime.now().date()))
        wake_time = gr.Text(label="⏰ Wake Time")

    with gr.Row():
        sleep_score = gr.Number(label="😴 Sleep Score (%)")
        restorative_sleep = gr.Number(label="🛌 Restorative Sleep (%)")
        hours_sleep = gr.Text(label="⏱️ Hours of Sleep")

    with gr.Row():
        hrv = gr.Number(label="❤️ HRV")
        rhr = gr.Number(label="💓 RHR")
        recovery_score = gr.Number(label="🏋️ Recovery Score (%)")
        strain = gr.Number(label="🔥 Strain")

    with gr.Row():
        resp_rate = gr.Number(label="🌬️ Respiratory Rate")
        mental = gr.Text(label="🧠 Mental Status")
        physical = gr.Text(label="💪 Physical Status")

    notes = gr.Textbox(label="📝 Notes", lines=6)

    submit_btn = gr.Button("Submit Check-In")
    status = gr.Textbox(label="Status")

    #def open_chat():
    #    print(f"🚀 Launching chat at {CHAT_URL}...")
    #    subprocess.Popen(['start', CHAT_URL], shell=True)

    def open_chat():
        print("✅ Launching Beburos chat...")
        threading.Thread(target=chat_ui.launch, kwargs={"share": False}).start()

        
    submit_btn.click(
        fn=save_checkin,
        inputs=[date, wake_time, sleep_score, restorative_sleep, hours_sleep,
            hrv, rhr, recovery_score, strain, resp_rate, mental, physical, notes],
        outputs=status
    )
    
    # Run this after check-in to open chat in browser
    threading.Timer(2.0, open_chat).start()

# === Launch if run directly ===
if __name__ == "__main__":
    checkin_ui.launch()
