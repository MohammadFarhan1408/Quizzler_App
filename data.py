import requests

response = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
response.raise_for_status()
data = response.json()
question_data = data['results']

# question_data = [
#     {"question": "A shrimp's heart is in its head.", "answer": "True"},
#     {"question": "The Great Wall of China is visible from space with the naked eye.", "answer": "False"},
#     {"question": "An octopus has three hearts.", "answer": "True"},
#     {"question": "Venus is the hottest planet in our solar system.", "answer": "True"},
#     {"question": "Humans and dinosaurs coexisted.", "answer": "False"},
#     {"question": "The shortest war in history lasted 38 minutes.", "answer": "True"},
#     {"question": "The unicorn is the national animal of Scotland.", "answer": "True"},
#     {"question": "Lightning never strikes the same place twice.", "answer": "False"},
#     {"question": "Honey never spoils.", "answer": "True"},
#     {"question": "Bats are blind.", "answer": "False"},
#     {"question": "Goldfish only have a memory span of three seconds.", "answer": "False"},
#     {"question": "There are more stars in the universe than grains of sand on Earth.", "answer": "True"},
#     {"question": "Humans have more than five senses.", "answer": "True"},
#     {"question": "The inventor of the lightbulb was Thomas Edison.", "answer": "False"},
#     {"question": "Some turtles can breathe through their butts.", "answer": "True"}
# ]


response.close()