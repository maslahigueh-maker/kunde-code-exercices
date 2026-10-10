resources = [
    {"name": "Sandy Hill Community Health Centre", "category": "healthcare", "source": "KundeCodeResource"},
    {"name": "Ottawa Food Bank", "category": "food", "source": "KundeCodeResource"},
    {"name": "Legal Aid Ottawa", "category": "legal", "source": "Google"},
    {"name": "Random Food Blog", "category": "food", "source": "Google"},
    {"name": "Community Legal Clinic", "category": "legal", "source": "KundeCodeResource"},
]

# let's simulate a RAG implementation, return all the results that come from our internal documents and match the category the user is asking for choose between : legal, food, healthcare
# Retrieval
def find_resources(category):
    results = []

    for resource in resources:
        if resource["category"] == category and resource["source"] == "KundeCodeResource":

            results.append(resource)

    return results

# Augmented (adding to the promp )
result = find_resources("food")
# What happens if i ask for a category that my res bank doesnt have? 
result_list = []
for r in result:
    result_list.append(r["name"])

result = find_resources("food")

# Generation (simulation of AI response)
# Extra: we want to join the items in the list using a comma to seperate them, how
print(f"here are the resources we found for you: {','.join(result_list)}")