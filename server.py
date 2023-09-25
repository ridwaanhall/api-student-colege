from flask import Flask

app = Flask(__name__)


@app.route("/search_student/<message_search>")
def search_student():
  return ""