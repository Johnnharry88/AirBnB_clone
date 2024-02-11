#!/usr/bin/env python3
"""Class that inherits from the basemodel class"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Defines Amenity blueprint"""
    name = ""
