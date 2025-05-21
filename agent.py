# agent.py

def get_input():
    print("Welcome to Beburos - your AI health companion!\n")
    sleep = float(input("Enter last night's sleep (hours): "))
    strain = float(input("Enter today's strain score (0–21): "))
    recovery = int(input("Enter recovery score (0–100): "))
    return sleep, strain, recovery

def generate_recommendation(sleep, strain, recovery):
    if recovery < 50:
        status = "🟥 Low recovery"
        suggestion = "Take a rest or active recovery day. Prioritize hydration, breathwork, and extra sleep."
    elif recovery < 70:
        status = "🟡 Moderate recovery"
        suggestion = "Do a light or moderate workout, stay mindful of fatigue, and get at least 8 hours sleep tonight."
    else:
        status = "🟢 High recovery"
        suggestion = "You're good to train hard today. Make sure to fuel well and monitor your strain."

    if sleep < 6:
        suggestion += " You're sleep deprived—aim for a nap or an early bedtime."

    if strain > 17 and recovery < 70:
        suggestion += " Your strain is high—consider adjusting your workload or adding meditation tonight."

    return status, suggestion

def main():
    sleep, strain, recovery = get_input()
    status, suggestion = generate_recommendation(sleep, strain, recovery)
    print(f"\nStatus: {status}")
    print(f"Recommendation: {suggestion}")

if __name__ == "__main__":
    main()