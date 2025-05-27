import argparse
import os
from dotenv import load_dotenv
load_dotenv()

def launch_app():
    # Unified app with form + chat in one Gradio UI
    from app import app
    app().launch()  # ✅ fixed: first build the interface, then launch it

def launch_checkin():
    # Standalone health check-in form
    from checkin_app import checkin_ui
    checkin_ui.launch()

def launch_chat():
    # Standalone mood/chat-style interface
    from gradio_chat import demo
    demo.launch()

def launch_debug():
    # Optional debug/test view if needed later
    print("\n[⚠️] Debug mode not implemented yet.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="🚀 Beburos Launcher")
    parser.add_argument(
        "--mode",
        choices=["app", "checkin", "chat", "debug"],
        default="app",
        help="Choose which interface to launch"
    )
    args = parser.parse_args()

    print(f"\n✨ Launching Beburos in '{args.mode}' mode...")

    if args.mode == "app":
        print("🚀 Launching full UI app...")
        launch_app()
    elif args.mode == "checkin":
        launch_checkin()
    elif args.mode == "chat":
        launch_chat()
    elif args.mode == "debug":
        launch_debug()

