# logic.py - Business Logic: Saving, Loading, and Handling Submissions
import os
import json
from datetime import datetime
from helper import log_prompt_debug
from helper import log_interaction
from beburos_core import ask_beburos

# === Paths ===
LOG_FOLDER = "logs"
CHECKIN_LOG_FILE = os.path.join(LOG_FOLDER, "checkins.jsonl")
os.makedirs(LOG_FOLDER, exist_ok=True)

# === Save a new check-in ===
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
    return entry

# === Load latest check-in ===
def load_latest_checkin():
    if not os.path.exists(CHECKIN_LOG_FILE):
        return None
    with open(CHECKIN_LOG_FILE, "r", encoding="utf-8") as f:
        entries = [json.loads(line) for line in f if line.strip()]
    return sorted(entries, key=lambda x: x["timestamp"])[-1] if entries else None

# === Handle UI submission and generate response ===
def handle_submit(date, wake_time, sleep_score, restorative_sleep, hours_sleep,
                  hrv, rhr, recovery_score, strain, resp_rate, mental, physical, notes):
    try:
        data = save_checkin(date, wake_time, sleep_score, restorative_sleep, hours_sleep,
                            hrv, rhr, recovery_score, strain, resp_rate, mental, physical, notes)

        prompt = notes or ""

        response = ask_beburos(
            float(sleep_score),
            float(strain),
            int(recovery_score),
            sleep_score=sleep_score,
            restorative_sleep=restorative_sleep,
            hrv=hrv,
            rhr=rhr,
            custom_input=prompt,
            mood=mental
        )

        log_interaction(sleep_score, strain, recovery_score, response)
        return response

    except Exception as e:
        return "⚠️ Beburos ran into an issue. Please try again or check your logs."
