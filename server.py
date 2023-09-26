from flask import Flask, abort, jsonify

from Controller.StudentController import get_student_data

app = Flask(__name__)


@app.route("/")
def home():
    return "anjaaayyyyyy"


@app.route("/<message_search>")
def search_student(message_search):
    student_data = get_student_data(message_search)

    if student_data is not None and "mahasiswa" in student_data and student_data["mahasiswa"]:
        return jsonify(student_data)
    else:
        abort(404)

@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Data not available"}), 404
