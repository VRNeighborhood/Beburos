# gradio_chat.py – Chat-based Beburos interface with mood support

from helper import load_latest_checkin
import gradio as gr
from beburos_core import ask_beburos  # Import main AI logic
from helper import log_interaction  # Import logging function

# === Global list to simulate persistent session memory ===
chat_history = []

# === Main function to handle user chat messages ===
def chat_with_beburos(message, history):
    from helper import load_latest_checkin

    # Default values
    mood = "Unknown"
    if "mood:" in message.lower():
        mood = message.split(":", 1)[-1].strip().capitalize()

    checkin = load_latest_checkin()
    if checkin:
        sleep = checkin.get("sleep_score", 0)
        strain = checkin.get("strain", 0)
        recovery = checkin.get("recovery_score", 100)
    else:
        sleep, strain, recovery = 0, 0, 100

    response = ask_beburos(sleep, strain, recovery, custom_input=message, mood=mood)

    # Optional log
    from helper import log_interaction
    log_interaction(sleep, strain, recovery, f"User mood: {mood} | Message: {message}\nBeburos: {response}")

    return response


# === Gradio Chat UI Configuration ===
demo = gr.ChatInterface(
    fn=chat_with_beburos,
    title="💬 Chat with Beburos — Your AI Health Companion",
    description="Tell Beburos how you're feeling, ask for guidance, or update your mood."
                "\n💡 Tip: Start a message with `mood: tired` or `mood: great` to set how you're feeling.",
    theme="default"  # Can change to "soft" or "compact" for different layouts
    )

# === Run the App ===
if __name__ == "__main__":
    demo.launch()
