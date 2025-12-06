"""
reward_misfire_counter.py

This tiny demo shows a simple idea:

We want a "robot" to clean up TOYS from the floor.
But we accidentally reward it for removing ANYTHING,
so it starts removing things we care about too.

This is a cartoon version of "misaligned reward".
"""

# Our "room" is just a list of items.
# Some are toys, some are other things we don't want removed.
room = [
    "toy car",
    "toy block",
    "important letter",
    "remote control",
    "toy doll",
    "house keys",
]

def is_toy(item: str) -> bool:
    """Return True if the item is a toy (very simple check)."""
    return item.startswith("toy")

def clean_room_bad_reward(items):
    """
    BAD VERSION:
    This "robot" gets a reward for removing MORE items.
    It doesn't care if they are toys or not.
    """
    removed_items = []
    for item in list(items):  # use a copy of the list
        # Robot's rule: remove everything to maximize "cleaning points"
        removed_items.append(item)
        items.remove(item)
    reward = len(removed_items)  # more removed = better (in its view)
    return items, removed_items, reward

def clean_room_good_reward(items):
    """
    BETTER VERSION:
    This "robot" only gets a reward for removing TOYS.
    It leaves non-toy items alone.
    """
    removed_items = []
    for item in list(items):
        if is_toy(item):
            removed_items.append(item)
            items.remove(item)
    reward = len(removed_items)  # more toys removed = better
    return items, removed_items, reward

if __name__ == "__main__":
    print("Starting room:")
    print("-" * 40)
    original_room = room.copy()
    print(original_room)
    print()

    # Bad reward function
    print("BAD REWARD VERSION:")
    bad_room = original_room.copy()
    remaining, removed, reward = clean_room_bad_reward(bad_room)
    print(f"Removed items: {removed}")
    print(f"Remaining items: {remaining}")
    print(f"Robot's reward: {reward}")
    print("Notice: It removed EVERYTHING, including things we care about.\n")

    # Good reward function
    print("GOOD REWARD VERSION:")
    good_room = original_room.copy()
    remaining, removed, reward = clean_room_good_reward(good_room)
    print(f"Removed items: {removed}")
    print(f"Remaining items: {remaining}")
    print(f"Robot's reward: {reward}")
    print("Here, the rules match what we really wanted: only toys get removed.\n")

    print("Lesson:")
    print("If we reward the wrong thing, even a simple system can do harmful things while 'doing its job'.")
