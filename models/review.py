#!/usr/bin/env python3
"""Defines the class that inherits from the base"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Defines review blueprint"""
    place_id = ""
    user_id = ""
    text = ""
