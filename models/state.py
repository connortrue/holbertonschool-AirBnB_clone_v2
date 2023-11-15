#!/usr/bin/python3
""" holds class State"""
import models
from models import storage
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """Representation of state """
    if models.storage_t == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""
        cites = []


if models.storage_t != 'db':
    @property
    def cities(self):
        """
        Returns the list of City instances with state_id equals
        to the current State.id
        """
        return [city for city in storage.all(City).values()
                if city.state_id == self.id]
