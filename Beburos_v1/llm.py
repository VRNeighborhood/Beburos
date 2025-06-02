# llm.py – Centralized LLM Interface

import os
from openai import OpenAI
from dotenv import load_dotenv

# === Load Environment Variables ===
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# === Global Debug and Mock Flags ===
DEBUG = os.getenv("DEBUG", "0") == "1"
MOCK = os.getenv("MOCK_LLM", "0") == "1"

def complete_prompt(prompt: str, model: str = "gpt-4", temperature: float = 0.7, fallback_model: str = "gpt-3.5-turbo") -> str:
    """
    Sends the prompt to the OpenAI LLM and returns the assistant response.
    Includes debug printing, mock fallback, and optional model fallback.
    """
    if MOCK:
        if DEBUG:
            print("🧪 MOCK_LLM enabled. Returning simulated response.")
        return "[MOCK RESPONSE] This is a simulated AI response."

    try:
        if DEBUG:
            print("🧠 Sending prompt to OpenAI LLM...")
            print("🔍 Prompt content:\n", prompt)

        chat = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a knowledgeable AI health coach."},
                {"role": "user", "content": prompt},
            ],
            temperature=temperature,
        )

        response = chat.choices[0].message.content

        if DEBUG:
            print("✅ LLM Response:\n", response)

        return response

    except Exception as e:
        if DEBUG:
            print("❌ Error during LLM call:", e)

        return "⚠️ Sorry, something went wrong while contacting the AI. Please try again later."




