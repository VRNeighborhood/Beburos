import os
from llm import complete_prompt
from prompt_utils import build_prompt_from_metrics  # Optional: if you want to refactor prompt logic
DEBUG = os.getenv("DEBUG", "0") == "1"

def ask_beburos(
    sleep: float,
    strain: float,
    recovery: int,
    sleep_score: float = None,
    restorative_sleep: float = None,
    hrv: int = None,
    rhr: int = None,
    custom_input: str = None,
    mood: str = None
) -> str:
    
    # Assemble dictionary of available metrics
    metrics = {
        "sleep": sleep,
        "strain": strain,
        "recovery": recovery,
        "sleep_score": sleep_score,
        "restorative_sleep": restorative_sleep,
        "hrv": hrv,
        "rhr": rhr,
        "mood": mood,
        "notes": custom_input,
    }

    prompt = build_prompt_from_metrics(metrics)

    try:
        response = complete_prompt(prompt)
        if DEBUG:
            print("📊 Metrics used:\n", metrics)
            print("📝 Final Prompt:\n", prompt)
        return response

    except Exception as e:
        if DEBUG:
            print("❗ Error during LLM call:", e)
    return "⚠️ Sorry, something went wrong with the AI response."
