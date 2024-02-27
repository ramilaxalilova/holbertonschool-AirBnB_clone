#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
from models import storage
import json
"""
    Base class
"""


class BaseModel:
    """ Class """

    def __init__(self, *args, **kwargs):
        if (kwargs != {}):
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'created_at':
                    self.created_at = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                elif key == 'updated_at':
                    self.updated_at = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()
        storage.save()
        return self.updated_at

    def to_dict(self):
        newdict = self.__dict__.copy()
        newdict['__class__'] = type(self).__name__
        newdict['created_at'] = self.created_at.isoformat()
        newdict['updated_at'] = self.updated_at.isoformat()
        return newdict
