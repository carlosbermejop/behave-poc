from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/api/health")
def check_health():
    return {"status": "OK"}


@app.route("/user/<username>")
def show_user_profile(username):
    return f"User {escape(username)}"
