from flask import Flask, render_template
from flask_restful import Resource, Api
from server_res import ServersRes

app = Flask(__name__, template_folder="templates")
api = Api(app)


@app.route("/home")
def home():
    return render_template("home.html", text="text")

api.add_resource(ServersRes, '/servers')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=80)
