# ui.py - Gradio UI Components
import gradio as gr
from datetime import datetime
from logic import handle_submit


def build_ui():
    with gr.Blocks() as app:
        gr.Markdown("""
        ## 🧠 Beburos Daily Check-In & Chat
        Enter your data below. Once submitted, Beburos will offer tailored advice.
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

        notes = gr.Textbox(label="📝 Notes", lines=4)
        output = gr.Textbox(label="🤖 Beburos says")

        submit = gr.Button("Submit Check-In + Get Guidance")
        submit.click(
            fn=handle_submit,
            inputs=[date, wake_time, sleep_score, restorative_sleep, hours_sleep,
                    hrv, rhr, recovery_score, strain, resp_rate, mental, physical, notes],
            outputs=output
        )

    return app
