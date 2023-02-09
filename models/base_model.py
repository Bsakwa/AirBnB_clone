#!/usr/bin/python3

# Author: Brian Sakwa
"""Defines a BaseModel Class"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ Represents the BaseModel of the AirBnb clone project"""

    def __init__(self, *args, **kwargs):
        """Instanciate the new BaseModel

        Arguments:
            * args : Unused
            **kwargs (dict): key/value pairs of attributes
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for key, val in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(val, tform)
                else:
                    self.__dict__[key] = val

    def save(self):
        """Save update_at with the current date time"""
        self.updated_at = datetime.today()

    def to_dict(self):
        """ Returns the dictionary of our BaseModel instance

        Returns the key/value pair __class__ that represents
        the class name of the object

        """
        my_dict = self.__dict__.copy()
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        my_dict["__class__"] = self.__class__.__name__
        return my_dict

    def __str__(self):
        """Return the str representation of the BaseModel Instancee"""
        cls = self.__class__.__name__
        return "[{}] ({}) {}".format(cls, self.id, self.__dict__)
