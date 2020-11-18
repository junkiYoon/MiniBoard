from flask import request
from flask_restful import Resource

from server.controller.auth import sign_up


class Auth(Resource):
    def post(self):
        email = request.json['email']
        password = request.json['password']
        name = request.json['name']
        phone_number = request.json['phone_number']
        gender = request.json['gender']

        return sign_up(email, password, name, phone_number, gender)
