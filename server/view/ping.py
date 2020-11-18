from flask_restful import Resource

from server.controller.ping import get_pong


class Ping(Resource):

    def get(self):
        return get_pong()
