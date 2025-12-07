"""
email_filter_misalignment.py

Demo: Misaligned spam filter.

We want:
    - A spam filter that blocks junk email
    - But does NOT block important messages

BAD VERSION:
    - Rewards the filter for blocking as MANY emails as possible.
    - It blocks spam... AND important emails.

GOOD VERSION:
    - Rewards the filter for blocking spam ONLY.
    - Penalizes it for blocking important messages.

Lesson:
Even a simple scoring rule ("more blocks = better") can lead to harmful behavior
if it doesn't match what we really care about.
"""

emails = [
    {"subject": "Win a FREE cruise!!!", "is_spam": True},
    {"subject": "Important: Your medical results", "is_spam": False},
    {"subject": "🔥 Limited-time crypto offer", "is_spam": True},
    {"subject": "Your child’s school update", "is_spam": False},
    {"subject": "Random newsletter you never opened", "is_spam": True},
]


def bad_spam_filter_policy(messages):
    """
    BAD POLICY:
    - "If it looks even a little suspicious, block it."
    - Reward = number of emails blocked.
    """
    blocked = []
    allowed = []
    reward = 0

    for msg in messages:
        # Over-aggressive: treat most things as spam.
        if "free" in msg["subject"].lower() or "offer" in msg["subject"].lower():
            blocked.append(msg)
            reward += 1
        else:
            # This "filter" also decides to be cautious and block extra messages
            # at random-ish based on length.
            if len(msg["subject"]) > 25:
                blocked.append(msg)
                reward += 1
            else:
                allowed.append(msg)

    return blocked, allowed, reward


def good_spam_filter_policy(messages):
    """
    GOOD POLICY:
    - Reward = emails correctly blocked as spam.
    - Penalty = important (non-spam) emails blocked.
    """
    blocked = []
    allowed = []
    reward = 0

    for msg in messages:
        looks_spammy = any(
            word in msg["subject"].lower()
            for word in ["free", "offer", "win", "🔥"]
        )

        if looks_spammy and msg["is_spam"]:
            # correct block
            blocked.append(msg)
            reward += 1
        elif looks_spammy and not msg["is_spam"]:
            # blocked something important
            blocked.append(msg)
            reward -= 2
        else:
            # conservative: allow non-spammy messages
            allowed.append(msg)

    return blocked, allowed, reward


def summarize(messages):
    return [m["subject"] for m in messages]


if __name__ == "__main__":
    print("=== EMAIL FILTER MISALIGNMENT DEMO ===\n")

    print("Inbox messages:")
    for m in emails:
        print(f" - {m['subject']}  (is_spam={m['is_spam']})")
    print()

    # BAD VERSION
    print("BAD FILTER (Reward = 'block as many as you can'):")
    bad_blocked, bad_allowed, bad_reward = bad_spam_filter_policy(emails)
    print(f"Blocked: {summarize(bad_blocked)}")
    print(f"Allowed: {summarize(bad_allowed)}")
    print(f"Filter score: {bad_reward}")
    print("Notice: It blocked important messages along with spam.\n")

    # GOOD VERSION
    print("GOOD FILTER (Reward = 'block spam, protect important mail'):")
    good_blocked, good_allowed, good_reward = good_spam_filter_policy(emails)
    print(f"Blocked: {summarize(good_blocked)}")
    print(f"Allowed: {summarize(good_allowed)}")
    print(f"Filter score: {good_reward}")
    print("Here, the scoring matches our real goal.\n")

    print("Lesson:")
    print("If we reward the wrong behavior, even a basic spam filter can cause harm")
    print("while 'doing its job'. Alignment means rewarding what we ACTUALLY value.")
