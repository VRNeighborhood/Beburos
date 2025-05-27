# cli_agent.py – Lightweight CLI test runner for Beburos logic
import os
from logic import ask_beburos

# Load .env variables (for DEBUG, MOCK_LLM, etc.)
load_dotenv()

def get_input():
    print("👋 Welcome to Beburos (CLI Mode)")
    sleep = float(input("🛌 Sleep hours: "))
    strain = float(input("🔥 Strain (0–21): "))
    recovery = int(input("💪 Recovery score (0–100): "))
    return sleep, strain, recovery

def main():
    sleep, strain, recovery = get_input()
    print("\n🧠 Sending to Beburos...\n")

    # Optionally log debug if enabled
    if os.getenv("DEBUG") == "1":
        print(f"[DEBUG] Inputs → Sleep: {sleep}, Strain: {strain}, Recovery: {recovery}")

    response = ask_beburos(sleep, strain, recovery)
    print("\n🤖 Beburos says:\n")
    print(response)

if __name__ == "__main__":
    main()


