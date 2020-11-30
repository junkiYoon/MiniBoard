from werkzeug.security import check_password_hash
from flask import abort
from flask_jwt_extended import create_access_token, create_refresh_token

from server.model import session
from server.model.users import User


def login(email, password):
    user = session.query(User).filter(User.email == email).first()
    check_user_pw = check_password_hash(user.passward, password) if user else None

    if check_user_pw:
        access_token = create_access_token(identity=email)
        refresh_token = create_refresh_token(identity=email)

        user.refresh_token = refresh_token

        session.commit()

        return {
            "access_token": access_token,
            "refresh_token": refresh_token
        }

    else:
        return abort(400, "The email or password is incorrect")


def logout(email):
    user = session.query(User).filter(User.email == email).first()

    if user:
        user.refresh_token = None

        session.commit()

        return {
            "message": "logout successfully"
        }

    else:
        return abort(401, "cannot find token user")
