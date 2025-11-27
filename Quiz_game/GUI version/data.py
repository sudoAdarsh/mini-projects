import requests

# Trivia Category Assignment and Default Handling
#
# Category ID assignments:
# "category" : 9        # General Knowledge
# "category" : 10       # Entertainment: Books
# "category" : 11       # Entertainment: Film
# "category" : 12       # Entertainment: Music
# "category" : 13       # Entertainment: Musicals & Theatres
# "category" : 14       # Entertainment: Television
# "category" : 15       # Entertainment: Video Games
# "category" : 16       # Entertainment: Board Games
# "category" : 17       # Science & Nature
# "category" : 18       # Science: Computers (Default category)
# "category" : 19       # Science: Mathematics
# "category" : 20       # Mythology
# "category" : 21       # Sports
# "category" : 22       # Geography
# "category" : 23       # History
# "category" : 24       # Politics
# "category" : 25       # Art
# "category" : 26       # Celebrities
# "category" : 27       # Animals
# "category" : 28       # Vehicles
# "category" : 29       # Entertainment: Comics
# "category" : 30       # Science: Gadgets
# "category" : 31       # Entertainment: Japanese Anime & Manga
# "category" : 32       # Entertainment: Cartoon & Animations
#
# If the user does not want a specific category (i.e., they want "mixed" categories), 
# they can either:
# - Set the category value to 'any' in the parameters dictionary, OR
# - Remove the "category" key entirely from the parameters dictionary.
#
# Example with "category" set to 'any' for mixed categories:
# parameters = {
#     "amount" : 10,
#     "type" : "boolean",
#     "category" : 'any',  # Mixed categories, no specific category
# }
#
# Example with "category" key removed (also for mixed categories):
# parameters = {
#     "amount" : 10,
#     "type" : "boolean",
#     # "category" key is omitted for mixed categories
# }
#

parameters = {
    "amount" : 10,
    "type" : "boolean",
    "category" : 18,     # Default : Computers
}

response = requests.get("https://opentdb.com/api.php", params=parameters)

data = response.json()

question_data = data['results']