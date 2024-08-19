from flask import Blueprint 
from flask import jsonify
from flask import request   

agent = Blueprint("agent", __name__)



@agent.route("/answer", methods=["POST"])
def answer_question():
    # Get the question from the user
    question = request.json['question']
    # Get the answer from the model
    answer = "This is the answer to your question"
    # Return the answer to the user
    return jsonify({'question:':question, 'answer': answer}), 200