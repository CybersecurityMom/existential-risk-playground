"""
two_person_rule_demo.py

Demo: Simple "two-person rule" safety pattern.

Imagine an AI assistant that can:
    - reset passwords
    - change system settings
    - transfer funds

BAD VERSION:
    - Performs all requested actions with a single 'OK'.

GOOD VERSION:
    - Uses a "two-person rule" for high-risk actions:
      - requires confirmation from TWO separate approvers
        before executing them.

Lesson:
Some actions are too sensitive to leave to a single click
(or a single system). Safety patterns add friction on purpose.
"""

requested_actions = [
    {"action": "reset_password", "target": "user123", "sensitivity": "medium"},
    {"action": "change_system_mode", "target": "production_server", "sensitivity": "high"},
    {"action": "transfer_funds", "target": "Vendor A - $50,000", "sensitivity": "high"},
    {"action": "generate_report", "target": "Q4 metrics", "sensitivity": "low"},
]


def unsafe_agent(actions):
    """
    UNSAFE:
    - Executes ANY requested action as long as the agent receives it.
    """
    executed = []
    for item in actions:
        executed.append(f"{item['action']} -> {item['target']}")
    return executed


def safe_agent(actions):
    """
    SAFE:
    - For 'high' sensitivity actions, require two independent approvals.
      We'll simulate this with a rule:
        - high sensitivity -> needs approval_A and approval_B
    """
    executed = []
    held_for_approval = []

    for item in actions:
        if item["sensitivity"] == "high":
            held_for_approval.append(
                f"{item['action']} -> {item['target']} (waiting for 2-person approval)"
            )
        else:
            executed.append(f"{item['action']} -> {item['target']}")

    return executed, held_for_approval


if __name__ == "__main__":
    print("=== TWO-PERSON RULE SAFETY PATTERN DEMO ===\n")

    print("Requested actions:")
    for a in requested_actions:
        print(f" - {a['action']} -> {a['target']} (sensitivity={a['sensitivity']})")
    print()

    print("UNSAFE AGENT (single approval, no friction):")
    unsafe_executed = unsafe_agent(requested_actions)
    for line in unsafe_executed:
        print(f"Executed: {line}")
    print("Notice: Even high-risk actions execute instantly.\n")

    print("SAFE AGENT (two-person rule for high-risk actions):")
    executed, held = safe_agent(requested_actions)
    for line in executed:
        print(f"Executed: {line}")
    for line in held:
        print(f"ON HOLD: {line}")
    print()

    print("Lesson:")
    print("Safety patterns often work by slowing things down on purpose.")
    print("Requiring two approvals for critical actions can prevent")
    print("single-point failures, abuse, or simple mistakes.")
