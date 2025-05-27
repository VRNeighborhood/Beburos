# prompt_utils.py — Handles prompt construction from user health data

def build_prompt_from_metrics(metrics: dict) -> str:
    """
    Converts a user metrics dictionary into a health guidance prompt.
    """
    prompt = "You are an expert health coach. Based on the following data:\n"

    if metrics.get("sleep") is not None:
        prompt += f"- Sleep: {metrics['sleep']} hours\n"
    if metrics.get("sleep_score") is not None:
        prompt += f"- Sleep Score: {metrics['sleep_score']}%\n"
    if metrics.get("restorative_sleep") is not None:
        prompt += f"- Restorative Sleep: {metrics['restorative_sleep']}%\n"
    if metrics.get("hrv") is not None:
        prompt += f"- HRV: {metrics['hrv']} ms\n"
    if metrics.get("rhr") is not None:
        prompt += f"- RHR: {metrics['rhr']} bpm\n"
    if metrics.get("strain") is not None:
        prompt += f"- Strain: {metrics['strain']} (out of 21)\n"
    if metrics.get("recovery") is not None:
        prompt += f"- Recovery: {metrics['recovery']} (out of 100)\n"
    if metrics.get("mood") is not None:
        prompt += f"- User reported mood: {metrics['mood']}\n"
    if metrics.get("notes") is not None:
        prompt += f"- User note: {metrics['notes']}\n"

    prompt += (
        "\nGive a personalized recommendation in a warm, motivational tone. "
        "Explain the reasoning behind your guidance and include specific actions "
        "to improve recovery, energy, or cognitive performance today."
    )

    return prompt
