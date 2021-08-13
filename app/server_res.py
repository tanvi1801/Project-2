from flask_restful import Resource, Api


class ServersRes(Resource):

    def get(self):
        return {'hello': 'world'}

    def post(self):
        return {}


class ServerRes(Resource):

    def get(self):
        return {'hello': 'world'}

    def post(self):
        return {}
