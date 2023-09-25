from flask import Flask, jsonify

from Controller.StudentController import get_student_data

app = Flask(__name__)


@app.route("/")
def home():
    return "anjaaayyyyyy"


@app.route("/<message_search>")
def search_student(message_search):
    student_data = get_student_data(message_search)

    if student_data is not None:
        return jsonify(student_data)
    else:
        return "Error fetching data from API", 500
