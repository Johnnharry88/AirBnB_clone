#!/usr/bin/env python3
""" Class holding the model from which others inherits"""
import models
import uuid
from datetime import datetime


class BaseModel:

    
    def __init__(self, *args, **kwargs):
        """Object Constructor  that intiates instacnes

        Arguments:
        *args: list of arguments
        **kwargs: dict holding key value pair
        """
        if kwargs is not None and kwargs != ():
            for k, v in kwargs.items():
                if k == '__class__':
                    continue
                if k == "created_at" or k == "updated_at":
                    v = datetime.fromisoformat(v)
                setattr(self, k, v)
            return
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
            
    def __str__(self):
        """ A representation in string format of object"""
        return "[{}} ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """updates up_time with current fate and time of update and saves"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns modified dictionary with attributes of obj"""
        new_obj = self.__dict__.copy()
        new_obj["__class__"] = type(self).__name__
        new_obj["created_at"] = new_obj["created_at"].isoformat()
        new_obj["updated_at"] = new_obj["updated_at"].isoformat()
        return new_obj
