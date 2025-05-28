# gradio_app.py

import gradio as gr
from agent import ask_beburos  # assumes agent.py is in the same directory
from helper import log_interaction  # import the CSV logger

# Define the UI logic
def get_recommendation(sleep, strain, recovery):
    try:
        response = ask_beburos(float(sleep), float(strain), int(recovery))

        # Log the inputs and AI response to CSV
        log_interaction(sleep, strain, recovery, response)

        return response
    except Exception as e:
        return f"⚠️ Error: {e}"

# Define input components
inputs = [
    gr.Number(label="Sleep (hours)", value=7.0),
    gr.Number(label="Strain (0–21)", value=15.0),
    gr.Number(label="Recovery (0–100)", value=70)
]

# Set up Gradio interface
demo = gr.Interface(
    fn=get_recommendation,
    inputs=inputs,
    outputs=gr.Textbox(label="🧠 Beburos says:"),
    title="Beburos — Your AI Health Companion",
    description="Enter your daily metrics to receive personalized recovery and wellness guidance."
)

# Launch the app
if __name__ == "__main__":
    demo.launch()
