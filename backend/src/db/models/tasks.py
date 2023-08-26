from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from config.database import Base

class Task(Base):
    __tablename__ = "tasks"
    
    # Fields
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    created_at = Column(Integer)
    updated_at = Column(Integer)
    page_id = Column(Integer, ForeignKey("user_pages.id"))
    creator_id = Column(Integer, ForeignKey("users.id"))

    # Relationships
    page = relationship("UserPage", backref="tasks")
    creator = relationship("User", backref="tasks")