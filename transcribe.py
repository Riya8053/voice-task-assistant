import os
from dotenv import load_dotenv
import assemblyai as aai

load_dotenv()
aai.settings.api_key = os.getenv("ASSEMBLYAI_API_KEY")

audio_url = "myvoice.mp4.mp4"

transcriber = aai.Transcriber()
transcript = transcriber.transcribe(audio_url)

print(transcript.text)