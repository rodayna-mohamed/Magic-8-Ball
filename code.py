import random

responses=[
    "yes,definitely!",
    "no not now",
    "ask again later",
    "it is certain",
    "very doubtful",
    "outlook is good",
    "better not  tell you now ",
    "concentrate and ask again "   
]

def get_rendom_response():
    return random.choice(responses)