from sqlalchemy import Column, Integer, VARCHAR, DATETIME, text

from server.model import Base


class Posts(Base):
    __tablename__ = 'post'

    id = Column(Integer, nullable=False, primary_key=True)
    title = Column(VARCHAR(40), nullable=False)
    content = Column(VARCHAR(3000), nullable=False)
    created_at = Column(DATETIME, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
