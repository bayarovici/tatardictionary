from flask import Flask, render_template, request
import json
import random
import difflib

app = Flask(__name__)

# Load the dictionary from dictionary.json
with open("dictionary.json", "r") as f:
    dictionary = json.load(f)

@app.route("/")
def home():
    # Select a random word from the dictionary as the "word of the day"
    word_of_the_day = random.choice(dictionary)
    return render_template("home.html", word_of_the_day=word_of_the_day)

# @app.route("/search")
# def search():
#     # Get the search query from the form submission
#     if query:
#         # Search the dictionary for the query
#         result = dictionary.get(query.lower())
#         print(result)
#     else:
#         result = None
#         print('fuck')
#     return render_template("search.html", result=result, query=query)

@app.route("/search")
def search():
    # Get the search query from the form submission
    query = request.args.get("query")
    # Search the dictionary for the query
    result = None
    print(query)
    for word in dictionary:
        if word["romanian"] == query:
            result = word
            break

    # If no exact match is found, get the most similar word
    if result is None:
        close_matches = difflib.get_close_matches(query, [w["romanian"] for w in dictionary])
        if close_matches:
            for word in dictionary:
                if word["romanian"] == close_matches[0]:
                    result = word
                    break
    print(result)
    print(query)
    # Render the search result template
    return render_template("search.html", result=result, query=query)


if __name__ == "__main__":
    app.run()
