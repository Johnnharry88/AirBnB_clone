#!/usr/bin/env python3
"""Defines Class that inherits form BaseModels"""
from models.base_model import BaseModel


class City(BaseModel):
    """Defiens City blueprint"""
    state_id = ""
    name = ""
