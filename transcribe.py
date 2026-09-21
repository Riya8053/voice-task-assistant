import os
from dotenv import load_dotenv
import assemblyai as aai
import json
from datetime import datetime

load_dotenv()
aai.settings.api_key = os.getenv("ASSEMBLYAI_API_KEY")

def detect_intent(text):
    text = text.lower()
    if "remind" in text:
        return "SET_REMINDER"
    elif "what" in text or "when" in text or "who" in text:
        return "ASK_QUESTION"
    else:
        return "UNKNOWN"

def extract_reminder_details(text):
    text_lower = text.lower()
    
    trigger_phrases = [
        "remind me to",
        "remind me about",
        "reminder to",
        "remind me",
    ]
    
    for phrase in trigger_phrases:
        if phrase in text_lower:
            task_part = text_lower.split(phrase)[1]
            cleaned = task_part.strip()
            if cleaned:
                return cleaned
    
    return "unspecified task"

def save_reminder(task):
    reminder = {
        "task": task,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    # Load existing reminders (if any)
    if os.path.exists("reminders.json"):
        with open("reminders.json", "r") as f:
            reminders = json.load(f)
    else:
        reminders = []

    # Add the new one
    reminders.append(reminder)

    # Save back to file
    with open("reminders.json", "w") as f:
        json.dump(reminders, f, indent=2)

    print(f"✅ Reminder saved: {task}")

# Main flow
audio_url = "myvoice.mp4.mp4"

transcriber = aai.Transcriber()
transcript = transcriber.transcribe(audio_url)

print(f"Transcribed Text: {transcript.text}")

intent = detect_intent(transcript.text)
print(f"Detected Intent: {intent}")

if intent == "SET_REMINDER":
    task = extract_reminder_details(transcript.text)
    save_reminder(task)
elif intent == "ASK_QUESTION":
    print("🤖 Sorry, I can only help with reminders right now.")
else:
    print("🤖 Sorry, I didn't understand that command.")