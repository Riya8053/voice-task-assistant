def detect_intent(text):
    text = text.lower()  # makes matching case-insensitive

    if "remind" in text:
        return "SET_REMINDER"
    elif "what" in text or "when" in text or "who" in text:
        return "ASK_QUESTION"
    else:
        return "UNKNOWN"

# Test with example sentences
test_sentences = [
    "Remind me to call mom tomorrow at 5 PM",
    "What time is it?",
    "Turn off the lights"
]

for sentence in test_sentences:
    intent = detect_intent(sentence)
    print(f"Text: {sentence}")
    print(f"Detected Intent: {intent}")
    print("---")