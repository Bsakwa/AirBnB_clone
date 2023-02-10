#!/usr/bin/python3

# Author: Brian Sakwa
"""Defines a City Class"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Represents a city

    Attributes:
        state_id (str): The state id of the city
        name (str): The name of the city
    """

    state_id = ""
    name = ""
