#!/usr/bin/env python3
"""Defines a class that inherits from the BaseMddel class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Defines USer Blueprint"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

