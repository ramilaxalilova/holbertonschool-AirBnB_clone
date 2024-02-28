"""
    Base class for all other classes
"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ class """

    def __init__(self):
        """ initilize instance """

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ print formatted """

        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ update updated_at attribute """

        self.updated_at = datetime.now()

    def to_dict(self):
        """ convert to dictionary """

        dct = self.__dict__.copy()
        for key, value in dct.items():
            if type(value) is datetime:
                dct[key] = value.isoformat()
        dct['__class__'] = type(self).__name__
        return dct
