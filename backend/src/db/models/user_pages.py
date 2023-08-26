from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from config.database import Base

class UserPage(Base):
    __tablename__ = "user_pages"
    
    # Fields
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    created_at = Column(Integer)
    updated_at = Column(Integer)
    project_id = Column(Integer, ForeignKey("user_projects.id"))

    # Relationships
    project = relationship("UserProject", backref="user_pages")