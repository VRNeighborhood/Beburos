# === Standard & Third-Party Imports ===
import os
from dotenv import load_dotenv  # To load environment variables from .env
from openai import OpenAI       # OpenAI Python SDK

load_dotenv(dotenv_path=".env")

# === Load OpenAI API Key from .env File ===
api_key = os.getenv("OPENAI_API_KEY")
print("✅ API Key loaded:", "Yes" if api_key else "No")  # TEMP debug print

# === Initialize OpenAI Client ===
client = OpenAI(api_key=api_key)

# === Get User Input From Command Line (Used in CLI mode) ===
def get_input():
    print("Welcome to Beburos – your AI health companion!\n")
    sleep = float(input("Enter last night's sleep (hours): "))
    strain = float(input("Enter today's strain score (0–21): "))
    recovery = int(input("Enter recovery score (0–100): "))
    return sleep, strain, recovery

# === Core AI Function: Ask Beburos for Guidance ===
def ask_beburos(sleep, strain, recovery):
    # Construct the prompt based on user's physiological metrics
    prompt = (
        f"You are an expert health coach. Based on the following data:\n"
        f"- Sleep: {sleep} hours\n"
        f"- Strain: {strain} (out of 21)\n"
        f"- Recovery: {recovery} (out of 100)\n\n"
        f"Give a personalized recommendation in a warm, motivational tone. "
        f"Explain the reasoning behind your guidance and include specific actions to improve recovery and energy today."
    )

    # Make the OpenAI API call to generate guidance
    chat = client.chat.completions.create(
        model="gpt-4o",  # Or use "gpt-3.5-turbo" for faster/cheaper
        messages=[
            {"role": "system", "content": "You are a friendly and knowledgeable AI health coach focused on human longevity, recovery, and daily performance."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    # Return the AI-generated message
    return chat.choices[0].message.content

#def main():
#   sleep, strain, recovery = get_input()
#   print("\n🧠 Beburos says:\n")
#   advice = ask_beburos(sleep, strain, recovery)
#   print(advice)

#if __name__ == "__main__":
#   main()