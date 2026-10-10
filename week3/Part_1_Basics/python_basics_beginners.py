# Week 3  "Build a Resource" CORE EXERCISE (STARTER)
# Write each part yourself, in order; if you get stuck, ask.

# TASK 1 : Variable
# Create a variable called "question" that stores a question a newcomer
# would ask our resource finder.

question = input ("Would ask our resource finder?")

# TASK 2 : List
# Create a list called "needs" with at least two things a person might
# need to bring with them  (example: health card).

needs = [health card, passport]


# TASK 3 : Dictionary
# Create a dictionary called "resource" for ONE resource.
# It must include a name, a phone number, and an address.

Resource :{"name": "Maslah", 
"phone num": "613-567-1664", 
"address": "123 slater rd "}

# TASK 4 : List of dictionaries
# Create a list called "list_of_resources" with at least two dictionaries,
# each shaped like the one you built in Task 3.

List_of_clients = [ {"name": "ouassim", "role": "student", "adress": "st-laurent"},
{"name": ""}]

# TASK 5 : Function
# Write a function called "final_output" that:
#   - takes ONE input: a person's name
#   - returns a message that includes: their name, the items from "needs",
#     and the name of the first resource in "list_of_resource"
#
# ^ Helper reminder if you get stuck:
#   ", ".join(your_list_name) turns a list into one readable string
# uncomment this and write your code here
# def final_output(user_name):
#      return 

# Don't forget to call your function and print the result:
# print(final_output("your name"))


# BONUS (optional)
# Try building the "needs" part of your message using a loop instead of .join()