from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")

# test imports
import mysql.connector
import psycopg2

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/home")
def home():
    return render_template("home.html", text="text")


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=80)
