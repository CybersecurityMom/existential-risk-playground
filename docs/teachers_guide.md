# Teacher / Facilitator Guide

This repo can be used in:
- Classrooms
- Workshops
- Community events
- Parent or youth programs

You do NOT need to be a deep technical expert to use it.

---

## Suggested flow for a 45–60 minute session

### 1. Start with a story (10–15 minutes)

Use `examples/misalignment/hungry_robot_story.md`.

- Read the story out loud or have a student read it.
- Ask:
  - "What did the robot do wrong?"
  - "Was it trying to be mean?"
  - "What was the real problem?"

Key takeaway:
> The instructions were too simple for the real-world goal.

---

### 2. Show the tiny code demo (15–20 minutes)

Open `examples/misalignment/reward_misfire_counter.py`.

If you can, run it in front of the group (or show screenshots).

Explain in simple language:
- The “room” is just a list of items.
- The “bad robot” removes everything to get a higher score.
- The “better robot” only removes toys.

Ask:
- "What did we reward in the bad version?"
- "What should we have rewarded instead?"
- "What could this look like in a real system?"

---

### 3. Discuss gaming the rules (10–15 minutes)

Use `examples/specification_gaming/cleaning_robot_game.md`.

Ask:
- "Is the robot cheating, or is it following the rules too well?"
- "Have you ever seen a person 'game' a system like that?"
- "What might this look like in online systems or apps?"

Connect it back to the idea:
> If rules and rewards are not designed carefully, powerful systems can behave in surprising and harmful ways.

---

### 4. Close with the checklist (10 minutes)

Show `examples/safety_patterns/safety_checklist.md`.

Ask participants:
- "Pick one real system you use (bank app, school app, email tool)."
- "Which checklist questions could you ask about it?"

This step helps them connect the abstract ideas back to everyday life.

---

## Tips for facilitators

- Keep the language simple and concrete.
- Use real-life analogies (kids gaming chores, adults gaming workplace metrics).
- Encourage questions; do not pretend to know everything.
- Emphasize that these are **toy examples**, not real-world attack tools.

The goal is understanding, not fear.
