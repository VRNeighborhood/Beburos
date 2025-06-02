import csv                      # For writing data to CSV files
import os                       # For file and directory path operations
import json                     # For reading and writing JSON files
from datetime import datetime   # For timestamping log entries

# === Define the folder and file path for logging ===
LOG_FOLDER = "logs"             # Folder where log file will be saved
LOG_FILE = os.path.join(LOG_FOLDER, "beburo_logs.csv")   # Full path to log file

# === Ensure the log folder exists ===
def ensure_log_folder():
    os.makedirs(LOG_FOLDER, exist_ok=True) # Create the folder if it doesn't exist

# === Function to log user interaction to a CSV file ===
def log_interaction(sleep, strain, recovery, response):
    """
    Logs the user's daily input and AI response to a CSV file.
    Includes timestamp, sleep (hours), strain (0–21), recovery (0–100), and response.
    """
    ensure_log_folder()                         # Make sure the log directory exists
    timestamp = datetime.now().isoformat()      # Get the current timestamp in ISO format

  # Collect the data to log as a list
    log_data = [timestamp, sleep, strain, recovery, response]

  # Check if the log file already exists
    file_exists = os.path.isfile(LOG_FILE)
  # Open the file in append mode (create if it doesn't exist)
    with open(LOG_FILE, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
   # If the file doesn't exist, write the CSV header first
        if not file_exists:
            writer.writerow(["timestamp", "sleep", "strain", "recovery", "response"])
   # Write the log data row
        writer.writerow(log_data)

def load_latest_checkin():
    """
    Loads the most recent health check-in entry from checkins.json.
    Returns None if file is missing or empty.
    """
    checkin_path = os.path.join("logs", "checkins.json")
    if not os.path.isfile(checkin_path):
        return None

    with open(checkin_path, "r", encoding="utf-8") as f:
        entries = [json.loads(line) for line in f if line.strip()]
        if not entries:
            return None
        # Sort by timestamp and return most recent
        latest = sorted(entries, key=lambda x: x["timestamp"])[-1]
        return latest


def log_prompt_debug(prompt: str):
    print("\n===== FINAL PROMPT SENT TO OPENAI =====\n")
    print(prompt)
    print("\n=======================================\n")
