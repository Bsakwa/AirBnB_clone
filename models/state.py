#!/usr/bin/python3

# Author: Brian Sakwa
""" Defines a State Class"""
from models.base_models import BaseModel


class State(BaseModel):
    """
    Represents a State

    Attribute:
        name (str): The name of the state
    """

    name = ""
