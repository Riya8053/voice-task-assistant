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
    
    # List of possible trigger phrases, in order of priority
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
            if cleaned:  # make sure something was actually extracted
                return cleaned
    
    return "unspecified task"

# Test edge cases
test_cases = [
    "Remind me to call mom tomorrow at 5 PM",     # normal case
    "Can you remind me about my meeting",          # different phrasing
    "I need a reminder to buy groceries",          # no "remind me to" at all
    "remind me call dad",                          # missing "to"
]

for text in test_cases:
    intent = detect_intent(text)
    print(f"Input: {text}")
    print(f"Intent: {intent}")
    if intent == "SET_REMINDER":
        task = extract_reminder_details(text)
        print(f"Extracted task: {task}")
    print("---")