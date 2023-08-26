from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from config.database import Base

class SectionField(Base):
    __tablename__ = "section_fields"
    
    # Fields
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    created_at = Column(Integer)
    updated_at = Column(Integer)
    section_id = Column(Integer, ForeignKey("sections.id"))

    # Relationships
    section = relationship("Section", backref="section_fields")