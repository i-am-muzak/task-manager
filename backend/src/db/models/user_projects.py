from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from config.database import Base

class UserProject(Base):
    __tablename__ = "user_projects"
    
    # Fields
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    slug = Column(String)
    created_at = Column(Integer)
    updated_at = Column(Integer)
    creator_id = Column(Integer, ForeignKey("users.id"))

    # Relationships
    creator = relationship("User", backref="user_projects")
