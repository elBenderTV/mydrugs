from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.sql.expression import text
from config.database import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    user_handle = Column(String(50), unique=True, nullable=False)
    user_password = Column(String(50), nullable=False)
    user_email = Column(String(50), unique=True, nullable=False)
    user_name = Column(String(100), nullable=False)
    user_number = Column(String(12), unique=True, nullable=False)
    created_at = Column(TIMESTAMP, server_default=text('NOW()'))