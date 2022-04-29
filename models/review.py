#!/usr/bin/python3
""" Review class definitiont """

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

from os import getenv


class Review(BaseModel, Base):
    """ The review class """

    __tablename__ = 'reviews'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=True)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=True)

    else:
        place_id = ""
        user_id = ""
        text = ""
