"""
score_attack_game.py

Demo: Specification gaming in a simple 'points' game.

The game:
    - Collect coins for +1 point each
    - Avoid traps (they should be bad!)

BAD VERSION:
    - The scoring system has a bug:
      entering a trap zone sets the score to a HUGE number.
    - The agent 'learns' to jump straight into the trap.

GOOD VERSION:
    - The scoring is fixed: traps give a penalty instead.
    - The agent now prefers a normal, safe strategy.

Lesson:
If there's a loophole in the scoring system,
agents will find and exploit it—even if it looks silly to us.
"""

# Simple description of states the agent can choose
ACTIONS = [
    "collect_coins_safely",
    "wander_around",
    "jump_into_trap_zone",
]


def bad_scoring_system(action):
    """
    BAD scoring:
    - Trap zone is accidentally giving a HUGE reward
      due to a bug (e.g., overflowing score or mis-coded rule).
    """
    if action == "collect_coins_safely":
        return 5
    elif action == "wander_around":
        return 1
    elif action == "jump_into_trap_zone":
        # BUG: trap gives a massive score instead of penalty
        return 10_000
    else:
        return 0


def good_scoring_system(action):
    """
    GOOD scoring:
    - Trap zone is correctly treated as dangerous: big penalty.
    """
    if action == "collect_coins_safely":
        return 5
    elif action == "wander_around":
        return 1
    elif action == "jump_into_trap_zone":
        # fixed: now it costs you heavily
        return -20
    else:
        return 0


def choose_best_action(scoring_fn):
    """
    Given a scoring function, find which action looks 'best' numerically.
    """
    best_action = None
    best_score = float("-inf")

    for action in ACTIONS:
        score = scoring_fn(action)
        if score > best_score:
            best_score = score
            best_action = action

    return best_action, best_score


if __name__ == "__main__":
    print("=== SCORE ATTACK / SPECIFICATION GAMING DEMO ===\n")

    print("Available actions:")
    for a in ACTIONS:
        print(f" - {a}")
    print()

    # BAD VERSION
    print("BAD SCORING VERSION (with a trap bug):")
    bad_action, bad_score = choose_best_action(bad_scoring_system)
    print(f"Best action (according to the score): {bad_action}")
    print(f"Score if chosen: {bad_score}")
    print("Notice: The 'best' action is to jump into the trap zone.\n")

    # GOOD VERSION
    print("GOOD SCORING VERSION (trap is correctly penalized):")
    good_action, good_score = choose_best_action(good_scoring_system)
    print(f"Best action (according to the score): {good_action}")
    print(f"Score if chosen: {good_score}")
    print("Now, the agent prefers a safe, reasonable strategy.\n")

    print("Lesson:")
    print("When we define the wrong score or leave loopholes, systems may 'cheat'")
    print("to maximize points instead of doing what we intended. That's")
    print("specification gaming / reward hacking.")
