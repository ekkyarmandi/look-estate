from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class Agent(Base):
    __tablename__ = "agents"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    phonenumber = Column(String)
    whatsapp = Column(String)
    company = Column(String)
    photograph = Column(String)

    properties = relationship("Property", back_populates="agent")

    def __repr__(self):
        return f"Agent(name='{self.name}', company='{self.company}', phonenumber='{self.phone_number}')"
