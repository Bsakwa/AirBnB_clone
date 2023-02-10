#!/usr/bin/python3

# Author: Brian Sakwa
"""Initializes a unique FileStorage instance for the AirBnB"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
