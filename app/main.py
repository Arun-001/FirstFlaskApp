from flask import Flask

app = Flask(__name__)

@app.route("/")
def home_view():
		return "<h1>Welcome to my First Flask App</h1>"
