#!/usr/bin/python3
"""
THE module that implements the BaseModel class.
"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    The class that defines all common attributes/methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the BaseModel class.
        """

        from models import storage
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)

    def __str__(self):
        """
        Returns A string representation of BaseModel object.
        [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                     self.__dict__)

    def save(self):
        """
        Updates 'self.updated_at' with the current datetime.
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns the dictionary containing all keys/values of __dict__
        of the instance:

        -only instance attributes set will be returned.
        -a key __class__ is added with the class name of the object.
        -created_at and updated_at must be converted to string object in ISO.
        object
        """
        dict_1 = self.__dict__.copy()
        dict_1["__class__"] = self.__class__.__name__
        for ki, vi in self.__dict__.items():
            if ki in ("created_at", "updated_at"):
                vi = self.__dict__[ki].isoformat()
                dict_1[ki] = vi
        return dict_1
