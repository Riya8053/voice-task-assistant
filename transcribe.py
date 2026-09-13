import assemblyai as aai

# Paste your API key here
aai.settings.api_key = "88e03cd5cfa749c7936c375e70b05bf0"

# A sample audio file URL to test with
audio_url = "myvoice.mp4.mp4"

# Create a transcriber and transcribe the audio
transcriber = aai.Transcriber()
transcript = transcriber.transcribe(audio_url)

# Print the resulting text
print(transcript.text)