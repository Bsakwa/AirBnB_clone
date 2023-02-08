#!/usr/bin/python3

# Author: Brian Sakwa

"""Defines an amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Represents an amenity

    Attributes:
        name (str): The name of the amenity.
    """

    name = ""
