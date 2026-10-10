"""
services/context.py

Kunde Code | Week 6: Embeddings & Context

WHAT IS THIS FILE FOR?
----------------------
Imagine someone new to Ottawa opens our app and needs help.
We want to ask them a FEW simple questions (like "Do you have any kids?")
so the app can show them the BEST resources for their specific scenario.

This file does 3 things:
  1. Lists the questions we ask.
  2. Shows an example of what the answers look like.
  3. Has a function that turns the answers into a neat "context" dictionary.

WHAT IS A DICTIONARY?
---------------------
A dictionary is a list of labels with values. Like a contact card:

    {"name": "Amina", "city": "Ottawa"}

"name" is the KEY (the label). "Amina" is the VALUE (the answer).

YOUR JOB (STUDENT CHALLENGE)
----------------------------
  TODO 1: Write 3 to 5 questions (use the intrview sesh, what would be useful to know).
  TODO 2: Write an example of what the answers could look like.
  TODO 3 (BONUS): Finish the function build_user_context().

RULES (please follow these!)
----------------------------
  - Only ask for things that help us FIND resources.
  - Do NOT ask for private stuff (no home address, no ID numbers).
  - People are allowed to SKIP a question. Your code must still work.

HOW TO TEST
-----------
Scroll to the bottom. Run this file in your terminal:

    python context.py

It will ask your questions one by one. Type an answer after "user type here:".
Then it prints the dictionary your code made. Check that it looks right!
"""

from typing import Any


# ============================================================
# TODO 1: WRITE YOUR QUESTIONS
# ============================================================
# Each question is a small dictionary with 3 parts:
#
#   "key"      : the short label for the answer (no spaces, use_underscores)
#   "question" : the sentence we show the user (keep it SIMPLE and friendly)
#   "options"  : the choices we suggest
#
# Some ideas for keys (pick only the ones that are useful):
#   age, preferred_language, kids, cost_preference,
#   accessibility_needs
#
# * Example (copy this and paste it in TODO 1 and then delete the # signs to try it, then write your own):
#
#     {
#         "key": "kids",
#         "question": "How many kids (under 18) do you have?",
#         "options": ["0", "1", "2-4", "5+"],
#     },
#
# Want the user to pick MORE THAN ONE answer? Add this line to the question:
#
#         "allow_many": True,
#
# Then the user can choose answers. (when you test this , that means u can answer by typing each answer separated by commas, like: housing, jobs)
#
CONTEXT_QUESTIONS = [
    # Write your dictionnaries here. Put a comma after each one.
    # ^ Remember: a string starts and ends with....

  {
    },
]


# ============================================================
# TODO 2: WRITE AN EXAMPLE OF THE ANSWERS
# ============================================================
# This shows what the dictionary looks like AFTER someone answers.
# Use the same KEYS as your questions above (this means go to your code in the TODO 1, you should have "key": ____(something), that something is what you write).
# (The values below are just examples. Change them to match YOUR design.)
EXAMPLE_CONTEXT: dict[str, Any] = {
    "location": "Ottawa",
    "preferred_language": "Sudanese Arabic",
    "support_type": ["housing"],
    "cost_preference": "free_or_low_cost",
}


# ============================================================
# TODO 3 (BONUS): FINISH THIS FUNCTION
# ============================================================
def build_user_context(answers: dict[str, Any]) -> dict[str, Any]:
    """
    Take the user's answers and return a clean dictionary.

    INPUT  (answers): the raw answers from the user.
                      Example: {"location": "Ottawa", "support_type": ["housing"]}

    OUTPUT: a NEW dictionary with only the keys our app understands.

    Baby steps to follow:
      * Step 1. Make a LIST of the keys your app allows.
              Example: allowed_keys = _________________
      * Step 2. Make an empty DICTIONARY called context.
              Example: context = _____
      * Step 3. Go through each allowed key.
              If the user answered it, copy the answer into context.
              If the user skipped it, either leave it out or set it to None.
      * Step 4. Return context.

    Important:
      - Do NOT change the original `answers` dictionary.
        Build a brand new one instead.
      - A skipped question must NOT crash your code.
    """
    # Delete this  line when you start writing your code: 
    raise NotImplementedError("Complete build_user_context() during the Week 6 lab.")


# 
# 
#
#   DO NOT TOUCH ANYTHING BELOW THIS LINE
#
#   This part pretends to be the user. It asks YOUR questions
#   in the terminal, records what you type, and sends the
#   answers to YOUR build_user_context() function.
#
# 


def _ask_questions_in_terminal() -> dict[str, Any]:
    """Ask every question in CONTEXT_QUESTIONS and record the typed answers."""
    answers: dict[str, Any] = {}

    for item in CONTEXT_QUESTIONS:
        print()
        print(item["question"])

        if item.get("options"):
            print("Choices: " + ", ".join(item["options"]))
        if item.get("allow_many"):
            print("  (You can type more than one. Separate them with commas.)")
        print("  (Press Enter to skip this question.)")

        typed = input("  user type here: ").strip()

        if typed == "":
            # The user skipped. We record nothing for this key.
            continue

        if item.get("allow_many"):
            # "housing, jobs" becomes ["housing", "jobs"]
            answers[item["key"]] = [
                part.strip() for part in typed.split(",") if part.strip()
            ]
        else:
            answers[item["key"]] = typed

    return answers


if __name__ == "__main__":
    print("=== Kunde Code: user context simulator ===")

    if not CONTEXT_QUESTIONS:
        print()
        print("You have no questions yet.")
        print("Go to TODO 1 and add 3 to 5 questions, then run this again.")
    else:
        typed_answers = _ask_questions_in_terminal()

        print()
        print("What the user typed (raw answers):")
        print(typed_answers)

        try:
            context = build_user_context(typed_answers)
            print()
            print("What YOUR function returned (user context):")
            print(context)
        except NotImplementedError:
            print()
            print("Week 6 TODO: finish build_user_context() first.")