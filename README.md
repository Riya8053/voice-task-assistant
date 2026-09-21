# Voice Task Assistant 🎙️

A voice-based AI agent built for the AssemblyAI Voice Agent Hackathon. It listens to spoken commands, transcribes them using AssemblyAI's speech-to-text API, detects the user's intent, and takes action — currently specializing in setting reminders.

## How it works

1. **Transcribe** — Audio input is sent to AssemblyAI's API and converted to text
2. **Understand** — The transcribed text is analyzed to detect intent (e.g., reminder request, question, unknown)
3. **Act** — If a reminder is detected, the task is extracted and saved to a local JSON file, with a confirmation message

## Tech Stack

- Python
- AssemblyAI API (speech-to-text)
- python-dotenv (for secure API key management)

## Setup Instructions

1. Clone this repository
2. Install dependencies: pip install assemblyai python-dotenv
3. Create a .env file in the project root with your AssemblyAI API key: ASSEMBLYAI_API_KEY=your_key_here
4. Run the script: python transcribe.py

## Example

Input (spoken): "Remind me to call mom tomorrow at 5 PM"

Output:
Transcribed Text: Remind me to call mom tomorrow at 5 PM
Detected Intent: SET_REMINDER
✅ Reminder saved: call mom tomorrow at 5 pm

## Future Improvements

- Support for more intent types (e.g., answering questions, canceling reminders)
- Real-time voice recording instead of pre-recorded audio files
- Notification/calendar integration for actual reminder delivery

## Author

Built by Riya, AI & Robotics Engineering student, as a solo submission.