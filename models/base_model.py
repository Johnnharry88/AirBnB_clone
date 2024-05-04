#!/usr/bin/env python3


"""
Module defining base class
"""
import models
import uuid
from datetime import datetime


class BaseModel():
    """
    Base class that defines common
    attributes/methods for other class inheritance
    """

    def __init__(self, *args, **kwargs):
        """
        instatiates object using it's
        attributes
        """
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
            return

        self.name = args
        self.my_number = args
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

       # models.storage.new(self)

    def __str__(self):
        """
        Returns string representation
        of instance
        """
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        updates the public instance attribute
        using the current datetime
        """
        self.updated_at = datetime.now()
        #models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        obj_dict = dict(self.__dict__)
        obj_dict['__class__'] = str(type(self).__name__)
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()

        return obj_dict
