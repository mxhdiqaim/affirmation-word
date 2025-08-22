import random
from flask import Flask, jsonify

app = Flask(__name__)

# This is your list of affirmations. You can add as many as you like!
affirmations = [
    "You are my favorite person in the whole world.",
    "Your smile makes my day brighter.",
    "I am so proud of everything you do.",
    "I can't wait to see you again.",
    "You are beautiful, inside and out.",
    "Thinking of you always brings a smile to my face.",
    "You are strong and capable of amazing things.",
    "I am so lucky to have you in my life.",
    "Every moment with you is a gift.",
    "You inspire me every day."
]

# The main API endpoint that will return a random affirmation
@app.route('/affirmation', methods=['GET'])
def get_affirmation():
    """Returns a random affirmation from the list."""
    random_affirmation = random.choice(affirmations)
    return jsonify({"affirmation": random_affirmation})

if __name__ == '__main__':
    app.run(debug=True)