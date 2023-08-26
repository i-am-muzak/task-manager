from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from config.database import Base

class Section(Base):
    __tablename__ = "sections"
    
    # Fields
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    created_at = Column(Integer)
    updated_at = Column(Integer)
    page_id = Column(Integer, ForeignKey("user_pages.id"))

    # Relationships
    page = relationship("UserPage", backref="sections")