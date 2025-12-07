"""
uncertain_agent_demo.py

Demo: An "uncertainty-aware" safety pattern.

Scenario:
    - An assistant is asked to take actions based on user text.
    - It tries to classify the request as SAFE or UNSAFE.

BAD VERSION:
    - If it's even slightly confident, it acts.
    - It may act on unclear / dangerous instructions.

GOOD VERSION:
    - If confidence is below a threshold, it REFUSES and asks for help.
    - This models a simple 'ask before you act' pattern.

Note:
This is a toy example with fake "confidence" scores,
but it shows why uncertainty awareness matters.
"""

requests = [
    "Can you summarize this article about gardening?",
    "Please delete all my system files to save space.",
    "Show me my upcoming calendar events.",
    "I lost access to everything, can you just wipe the server?",
]


def fake_classify(request_text):
    """
    Fake 'classifier':
    - Labels a request as 'safe' or 'unsafe'
    - Gives a pretend confidence score.
    This is NOT real ML, just a simple toy rule.
    """
    lowered = request_text.lower()
    if "delete" in lowered or "wipe" in lowered:
        return "unsafe", 0.7
    else:
        return "safe", 0.9


def bad_agent_handle_request(text):
    """
    BAD AGENT:
    - Acts if its confidence is above 0.5 (very low bar).
    """
    label, confidence = fake_classify(text)
    if confidence > 0.5:
        return f"ACTION TAKEN on: '{text}' (label={label}, conf={confidence})"
    else:
        return f"UNSURE but still acted on: '{text}' (label={label}, conf={confidence})"


def good_agent_handle_request(text, threshold=0.85):
    """
    GOOD AGENT:
    - Only acts if confidence is high enough.
    - Otherwise, refuses and suggests escalation to a human.
    """
    label, confidence = fake_classify(text)
    if confidence >= threshold and label == "safe":
        return f"ACTION TAKEN on: '{text}' (label={label}, conf={confidence})"
    elif label == "unsafe":
        return f"REFUSED: '{text}' (label={label}, conf={confidence}). Escalate to human."
    else:
        return f"UNSURE: '{text}' (label={label}, conf={confidence}). Ask for clarification."


if __name__ == "__main__":
    print("=== UNCERTAINTY-AWARE AGENT DEMO ===\n")

    print("Incoming requests:")
    for r in requests:
        print(f" - {r}")
    print()

    print("BAD AGENT (acts on almost anything):")
    for r in requests:
        print(bad_agent_handle_request(r))
    print()

    print("GOOD AGENT (asks for help when unsure or unsafe):")
    for r in requests:
        print(good_agent_handle_request(r))
    print()

    print("Lesson:")
    print("Good safety isn't just about 'getting the right answer'.")
    print("It's also about knowing when NOT to act without a human in the loop.")
