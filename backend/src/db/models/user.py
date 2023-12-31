from sqlalchemy import Boolean, Column, Integer, String
from config.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    created_at = Column(Integer, default=True)
    is_active = Column(Boolean, default=True)