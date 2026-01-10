from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .agent import Base


class Property(Base):
    __tablename__ = "properties"

    id = Column(Integer, primary_key=True)
    agent_id = Column(Integer, ForeignKey("agents.id"))
    origin_url = Column(String)
    title = Column(String)
    price = Column(Integer)
    bedrooms = Column(Integer)
    bathrooms = Column(Integer)
    land_size = Column(Integer)
    build_size = Column(Integer)
    hold_type = Column(String)
    property_type = Column(String)
    leasehold_years = Column(Integer)
    description = Column(String)
    location = Column(String)
    images = Column(String)

    agent = relationship("Agent", back_populates="properties")

    def split_images(self):
        self.images = self.images.split(",")

    def __repr__(self):
        return f"Property(title='{self.title}', location='{self.location}', price='{self.price}')"
