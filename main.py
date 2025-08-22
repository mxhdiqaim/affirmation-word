import random
from flask import Flask, jsonify

app = Flask(__name__)

# This is your list of affirmations. You can add as many as you like!
affirmations = [
    "Your smile makes will my day brighter."
    "You've got a great sense of humor."
    "Your positive energy is contagious."
    "I always have a good time with you."
    "I can't wait to see you again.",
    "You are beautiful, inside and out.",
    "Thinking of you always brings a smile to my face.",
    "You are strong and capable of amazing things.",
    "I am so lucky to have you in my life.",
    "Every moment with you is a gift.",
    "It's always great to hear from you."
    "You are smart and capable of amazing things."
    "You have a great sense of style."
    "It's always great to hear from you."
    "You're such a thoughtful person."
    "You have a killer sense of style.",
    "You always know how to make me laugh.",
    "I love hearing about what you're passionate about.",
    "Your mind works in a really cool way.",
    "You're a really good problem solver.",
    "Your perspective on things is so unique.",
    "It's always fun when we're hanging out.",
    "You have a way of making people feel comfortable.",
    "You're so dedicated to your goals.",
    "You brighten up the whole room."
]

# The main API endpoint that will return a random affirmation
@app.route('/affirmation', methods=['GET'])
def get_affirmation():
    """Returns a random affirmation from the list."""
    random_affirmation = random.choice(affirmations)
    return jsonify({"affirmation": random_affirmation})

if __name__ == '__main__':
    app.run(debug=True)