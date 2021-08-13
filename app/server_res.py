from flask_restful import Resource, Api


class ListDatabaseRes(Resource):

    def get(self):
        return {'hello': 'world'}


class SelectDatabaseRes(Resource):

    def get(self):
        return {'hello': 'world'}


class ServerRes(Resource):

    def get(self):
        return {'hello': 'world'}

    def post(self):
        # accept url, port, db name
        return {}
