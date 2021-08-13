import os

from flask import Flask, render_template, request, jsonify
from flask_restful import Api, Resource

from extensions import db

app = Flask(__name__, template_folder="templates")
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["DATABASE_URL"]
db.init_app(app)


class Database(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    host = db.Column(db.String(200), unique=False, nullable=True)
    port = db.Column(db.Integer)
    database = db.Column(db.String(200), unique=False, nullable=True)
    user = db.Column(db.String(200), unique=False, nullable=True)
    password = db.Column(db.String(200), unique=False, nullable=True)
    db_type = db.Column(db.String(200), unique=False, nullable=True)


class ListTablesDatabaseRes(Resource):

    def get(self):
        return {'hello': 'world'}


class SelectAllTableDatabaseRes(Resource):

    def get(self):
        return {'hello': 'world'}


class ServerRes(Resource):

    def get(self):
        return {'hello': 'world'}

    def post(self):
        data = request.get_json(force=True)
        host = data["host"]
        port = data["port"]
        database = data["database"]
        user = data["user"]
        password = data["password"]

        db_instance = Database(host=host, port=port, database=database, user=user, password=password)
        db.session.add(db_instance)
        db.session.commit()
        return jsonify({"id": db_instance.id})


@app.route("/home")
def home():
    return render_template("home.html", text="text")


api.add_resource(ServerRes, '/servers')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=80)
