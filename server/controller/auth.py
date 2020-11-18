from flask import abort
from werkzeug.security import generate_password_hash

from server.model import session
from server.model.users import User


def sign_up(email, password, name, phone_number, gender):

    user = session.query(User).filter(User.email == email).first()

    if user:
        return abort(409, 'This email already signed up')

    add_user = User(email=email, password=generate_password_hash(password),
                    name=name, phone_number=phone_number, gender=gender)
    session.add(add_user)
    session.commit()

    return {
        'message': 'Sign up successfully'
    }, 201
