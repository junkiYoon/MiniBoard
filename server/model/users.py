from sqlalchemy import Column, VARCHAR, Enum

from server.model import Base


class User(Base):
    __tablename__ = 'user'

    email = Column(VARCHAR(40), nullable=False, primary_key=True)
    password = Column(VARCHAR(100), nullable=False)
    name = Column(VARCHAR(20), nullable=True)
    phone_number = Column(VARCHAR(20), nullable=True)
    gender = Column(Enum('male', 'female', 'unchosen'))
    refresh_token = Column(VARCHAR(500))
