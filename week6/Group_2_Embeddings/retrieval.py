"""
services/retrieval.py

Kunde Code | Part 3: The Teams | Job: Resource Retrieval

WHAT IS THIS FILE FOR?
----------------------
A user types a question like:  "Where can I get a lawyer?"

Our app needs to find the BEST matching resources in our database
(like a lawyer clinic, a housing help office, etc).

This file is the "finder". It doesn't write the answer.
It just finds the right resources and hands them back.

THE BIG IDEA (3 simple steps)
-----------------------------
  1. TURN THE QUESTION INTO NUMBERS (embeddings).
     Computers compare numbers better than words.
     A list of numbers that stands for the meaning of a sentence is
     called an EMBEDDING, like I alr explained. We already have a function for this:
     get_embedding().

  2. ASK SUPABASE "WHAT IS SIMILAR TO THESE NUMBERS?"
     Supabase has a helper (called an RPC function) named "match_res".
     We send it our numbers, and it sends back the closest resources.

  3. RETURN THE RESULTS.
     Each result is a dictionary (a contact card with labels and values).

WORDS YOU WILL SEE
------------------
  question         : the sentence the user typed
  embedding        : the question turned into a list of numbers
  match_count      : how many results we want back (the "top 5")
  match_threshold  : the minimum "how similar" score to be allowed in.
                     Bigger number = stricter. 0.1 = pretty relaxed.
  similarity       : a score showing how close a result is to the question.
                     Closer to 1 = better match.
  RPC              : a way to ask Supabase to run a ready-made function.

YOUR JOB
--------
  Finish search_similar_resources() below (look for TODO).
  Then run:   python retrieval.py
  Type real questions a user could ask, and check if the results make sense.

HOW TO TEST
-----------
Run this file in your terminal. When you see "user type here:", type a
question and press Enter. The results will print. Type "quit" to stop.
Try at least 5 different questions!
"""

# These two lines are already done for you.
#   supabase       : our connection to the database
#   get_embedding  : turns text into a list of numbers
from db.supabase_client import supabase
from services.embeddings import get_embedding


# ============================================================
# TODO: FINISH THIS FUNCTION
# ============================================================
def search_similar_resources(
    question: str, match_count: int = 5, match_threshold: float = 0.1
) -> list[dict]:
    """
    Take a plain-English question and return the best matching resources.

    INPUT:
        question         : text, like "Where can I get a lawyer?"
        match_count      : how many results we want (default 5)
        match_threshold  : minimum similarity score (default 0.1)

    OUTPUT:
        A list of dictionaries. Each dictionary is one resource with
        labels like: id, category, group_id, name, address, contact,
        hours, eligibility, description, prerequisites, sources,
        similarity

    Baby steps to follow:

      Step 1. Make the embedding for the question.
              Use get_embedding(...) and give it the question.
              *IMPORTANT: also give it  input_type="search_query"
              (because this is a QUESTION, not a document).
              Save the answer in a variable, like query_embedding.

      Step 2. Call Supabase. The pattern looks like this:

                  response = supabase.rpc(
                      "match_res",
                      {
                          "query_embedding": ...,   # what do you think this should have? you're passing something onto the function, look at the name
                          "match_count": ...,       
                          "match_threshold": ...,  
                      },
                  ).execute()

              Careful: the labels in the curly brackets { } must be spelled
              EXACTLY like above, or Supabase will not understand.

      Step 3. The results live inside  response.data 
              Return that.
    """
    
    # Delete the next line when you start writing your code:
    raise NotImplementedError("Finish search_similar_resources() first.")


# 
# ############################################################
#
#   DONT TOUCH!!!!! Ask me if u have any questions abt this code
#
#   This part pretends to be the user. It lets you type
#   questions in the terminal, sends each one to YOUR
#   search_similar_resources() function, and prints what
#   comes back so you can check if it makes sense.
#
# ############################################################


def _show_results(results) -> None:
    """Print the results in a simple, readable way."""
    if not results:
        print("  No results found.")
        print("  Tip: your match_threshold might be too high, or the")
        print("  question might not match anything in the database.")
        return

    print(f"  Found {len(results)} result(s):")
    for number, item in enumerate(results, start=1):
        name = item.get("name", "(no name)")
        category = item.get("category", "(no category)")
        similarity = item.get("similarity")
        description = item.get("description") or ""

        if isinstance(similarity, (int, float)):
            score_text = f"{similarity:.3f}"
        else:
            score_text = "(no score)"

        print()
        print(f"  {number}. {name}")
        print(f"     Category   : {category}")
        print(f"     Similarity : {score_text}   (closer to 1 = better match)")
        if description:
            short = description if len(description) <= 120 else description[:120] + "..."
            print(f"     About      : {short}")


if __name__ == "__main__":
    print("=== Kunde Code: retrieval simulator ===")
    print("Type a question a user could ask, then press Enter.")
    print("Examples:")
    print("  Where can I get a lawyer?")
    print("  I need help finding a place to live")
    print("  Where can I learn English for free?")
    print('Type "quit" to stop.')

    while True:
        print()
        typed_question = input("user type here: ").strip()

        if typed_question.lower() in ("quit", "exit", "q"):
            print("Bye! Great testing.")
            break

        if typed_question == "":
            print("  You typed nothing. Type a question, or type quit.")
            continue

        try:
            found = search_similar_resources(typed_question)
            print()
            print(f"Question: {typed_question}")
            _show_results(found)
        except NotImplementedError:
            print("  TODO: finish search_similar_resources() first.")
            break
        except Exception as error:
            print("  Oops, something went wrong while searching:")
            print(f"  {error}")
            print("  Check: spelling of the RPC name and the 3 labels,")
            print("  and that your .env keys are set.")