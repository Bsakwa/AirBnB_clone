#!/usr/bin/python3

# Author: Brian Sakwa
"""Defines a review Class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Represents a review

    Attributes:
        user_id (str): The id of the user
        place_id (str): The id of the place to be reviewed
        text (str): The review of the user
    """

    user_id = ""
    place_id = ""
    text = ""
