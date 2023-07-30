from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from config.database import Base

class Blacklist(Base):
    __tablename__ = "blacklists"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    started_at = Column(Integer)
    finish_at = Column(Integer)

    user = relationship("User", backref="blacklists")