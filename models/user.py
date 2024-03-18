#!/usr/bin/python3
""" User module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    places = relationship("Place", cascade="all, delete",
                          backref="city", passive_deletes=True)
    reviews = relationship("Review", cascade="all, delete",
                           backref="user", passive_deletes=True)
