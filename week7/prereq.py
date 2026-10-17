"""
Kunde Code | Week 7: Resource Prerequisite Checker

WHAT IS THIS FILE FOR?
----------------------
Imagine someone finds a food bank or a housing service in Kunde Code.
Before they go, they want to know what they might need to bring or do.

This program shows the information we have about a REAL service.

It can:
  1. Show a list of community services.
  2. Let someone choose a service.
  3. Show the prerequisites (things they may need to bring or do).
  4. Handle a wrong choice without crashing.

IMPORTANT:
An empty list does NOT mean "nothing is needed."
It only means "we checked the website and found nothing listed."
That is why every service needs a source: the page where you looked.


WHAT IS A DICTIONARY?
---------------------
A dictionary stores information using labels and values, like a contact card:

    {"name": "Amina", "city": "Ottawa"}

"name" is the KEY (the label).
"Amina" is the VALUE (the information).


WHAT IS A LIST?
---------------
A list stores more than one item:

    ["Proof of address", "Household information"]

This means there are two things listed.


PREREQUISITE OR ELIGIBILITY?
----------------------------
  - ELIGIBILITY = who can use the service
    (for example "adults", or "people living in certain parts of Ottawa").
    Do NOT put this in the prerequisites list.
  - PREREQUISITE = something a person must bring or do
    (for example ID, proof of address, a referral, an appointment).
    Only put things the website says are REQUIRED.


YOUR STUDENT CHALLENGE
----------------------
This time you are working with REAL services, not made-up ones.
Everything you write must come from the organization's own website.

STEP 1 (before coding): fill up your services using the worksheet (find the missing info).
TODO 1: Fill in the resources dictionary with at least 5 of the services on your section.
TODO 2: Give each service a name, a list of prerequisites,
        and the page where you found the information (the source).
TODO 3: Finish show_prerequisites() so it displays the right message.
TODO 4: Test your program with a valid choice and a wrong choice.

BONUS CHALLENGES
----------------
  - Print the source page for each service.
  - Let people search by typing the service name instead of a number.
  - Let the user choose a language and show services that support it.
  - Add a function that checks whether important information is missing.


RULES
-----
  - Use only information you found on the organization's own website.
  - Do not guess what a real person must bring.
  - Every service needs a source (a page URL). The program will not show
    a service that has no source.
  - An empty prerequisites list means we checked, but no prerequisites
    are currently listed in our records.
  - Be ready to explain where you found each piece of information.


HOW TO RUN THIS FILE
--------------------
Save it as prerequisite_checker.py, then run:

    python prerequisite_checker.py

Choose a number from the list. Type Q when you want to quit.
"""


# ============================================================
# STUDENT TODO 1: FILL IN YOUR  SERVICES
# ============================================================
# Each service is stored in a dictionary with these pieces of information:
#
#   "name"          : the service's name
#   "website"       : the organization's website (where to look)
#   "prerequisites" : a LIST of things the user must bring or do
#   "source"        : the exact page where YOU found the information
#
# This first service is ready for you to research. Its source is empty
# because nobody has checked the website yet.
#
# When you finish checking a service:
#   1. Put what you found in "prerequisites" (as a list).
#   2. Paste the page URL into "source".
#
# ? Example of a finished entry (the format only, not a real service):
#
# "1": {
#     "name": "Example Food Centre",
#     "website": "https://example.org/",
#     "prerequisites": ["Proof of address", "Household information"],
#     "source": "https://example.org/get-help",
# },
#
# The number on the left ("1") is the choice the user types.
# Copy an entry and change the information to add another service.
# Add more real services from your list until you have at least 5 (real ones from our list!!).

resources = {
    "1": {
        "name": "Social Housing Registry of Ottawa",
        "website": "https://housingregistry.ca/",
        "prerequisites": [],
        "source": "",
    }, #add your other services here using the same format
}


# ============================================================
# TODO 2: SHOW THE LIST OF SERVICES
# ============================================================
def show_resources():
    """
    Print each service with its number.

    For example:
      1. Social Housing Registry of Ottawa
      2. Matthew House Ottawa
    """
    print("\nCommunity services:")

    # Go through each number and service in the dictionary.
    for number, resource in resources.items():
        # & HINT: you only need to write ONE LINE of code
        # & YOUR CODE GOES HERE (inside the print statement) !!!!

        print()


# ============================================================
# TODO 3: SHOW THE PREREQUISITES
# ============================================================
def show_prerequisites(resource):
    """
    Show the prerequisite information for ONE service.

    TODO:
    Write code for these 2 situations:

    1. If resource["prerequisites"] contains items:
       Print "Known prerequisites:"
       Use a for loop to print each item with a dash.
       Then remind the user to check with the organization.

    2. Otherwise:
       Print that no prerequisites are currently listed in our records.

    HINTS:
      - Use if / else.
      - Use `for item in resource["prerequisites"]:` to go through the list.
      - Use `print(f"- {item}")` to print one item.
      - Run the practice tests from the menu to check your work.

    * BONUS:
    * - If the service has a "source", print it after your message.
    *   (Careful: the practice examples have no "source", so your code
    *   must not crash when it is missing.)
    """
    print(f"\nService: {resource['name']}")

    # & YOUR CODE GOES HERE
    # & Write your if / else code here and remove pass when you're done.
    pass


# ============================================================

# ! THERE'S NOTHING TO CHANGE AFTER THIS, DON'T TOUCH!!!
# ============================================================
def main():
    """Run the program and let the user check more than one service."""
    print("Welcome to the Kunde Code Prerequisite Checker!")
    print("These are real services.")

    while True:
        show_resources()
        choice = input("\nType a service number, or Q to quit: ").strip()

        if choice.lower() == "q":
            print("Thanks for trying Kunde Code!")
            break

        # this finds the service the user chose.
        # If the number is not in the dictionary, .get() gives us None.
        resource = resources.get(choice)

        if resource is None:
            print("That choice isn't on the list. Please try again.")
            continue

        # A service with no source has not been researched yet.
        # We never show it as "nothing needed" without a source.
        if not resource.get("source"):
            print(f"\nService: {resource['name']}")
            print("We don't have researched information for this service yet.")
            continue

        show_prerequisites(resource)


# ============================================================
# PRACTICE TESTS: USE THESE TO CHECK YOUR WORK
# ============================================================
def run_practice_tests():
    """
    Try show_prerequisites() with two example services.
    The tests use made-up examples, so they check your function,
    not your research.
    The tests check the words your function prints (capital letters
    do not matter).
    """
    from contextlib import redirect_stdout
    from io import StringIO

    test_cases = [
        (
            "A service with prerequisites",
            {
                "name": "Example Food Centre",
                "prerequisites": ["Proof of address", "Household information"],
            },
            ["Known prerequisites:", "Proof of address", "Household information"],
        ),
        (
            "A service with an empty list",
            {
                "name": "Example Youth Centre",
                "prerequisites": [],
            },
            ["No prerequisites are currently listed"],
        ),
    ]

    print("\n=== Practice tests ===")
    passed = 0

    for test_name, example, expected_words in test_cases:
        saved_output = StringIO()

        # Capture what the function prints so the test can check it.
        with redirect_stdout(saved_output):
            show_prerequisites(example)

        output = saved_output.getvalue().lower()
        missing_words = [
            word for word in expected_words if word.lower() not in output
        ]

        if not missing_words:
            print(f"[PASS] {test_name}")
            passed += 1
        else:
            print(f"[NOT YET] {test_name}")
            print("  Your function still needs to print:")
            for word in missing_words:
                print(f"  - {word}")

    print(f"\nResult: {passed} out of {len(test_cases)} tests passed.")

    if passed == len(test_cases):
        print("Nice work! Your function passed all the practice tests.")
    else:
        print("This is expected until you finish TODO 3.")
        print("Follow the hints in show_prerequisites(), save, then test again.")


# ============================================================
# This is the interactive part:
#   1. Try the program like a user would.
#   2. Run practice tests to check your function.
#   3. Choose another option or quit whenever you want.
# ============================================================
if __name__ == "__main__":
    print("=== Kunde Code: Week 7 Coding Challenge ===")
    print()
    print("YOUR MISSION")
    print("Build the part of Kunde Code that tells people what they may need")
    print("to prepare before visiting a real community service.")
    print()
    print("WHAT YOU NEED TO DO")
    print("1. Research your services on their websites (use the worksheet).")
    print("2. Fill in the resources dictionary with what you found.")
    print("3. Find TODO 3 in show_prerequisites().")
    print("4. Write code for these two situations:")
    print("   - The service has one or more prerequisites.")
    print("   - The service has no prerequisites listed on its website.")
    print("5. Save your file, then choose an option below to try your code.")
    print()
    print("YOU CAN WORK INDEPENDENTLY")
    print("- Choose 1 to try the program like a user.")
    print("- Choose 2 to run practice tests and get feedback.")
    print("- If a test does not pass, go back to TODO 3 and try again.")
    print()
    print("REMEMBER: an empty list means 'we checked and found nothing listed',")
    print("not 'nothing is needed'. Always add your source.")
    print()
    print("1. Try the program")
    print("2. Run practice tests")
    print("Q. Quit")

    while True:
        mode = input("\nType 1, 2, or Q: ").strip().lower()

        if mode == "1":
            main()
        elif mode == "2":
            run_practice_tests()
        elif mode == "q":
            print("Good luck with your coding challenge!")
            break
        else:
            print("Please type 1, 2, or Q.")