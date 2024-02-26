import uuid
import datetime
"""
    Base class
"""


class BaseModel:
    """ Class """

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        self.__dict__[self.created_at] = self.created_at.isoformat()
        self.__dict__[self.created_at] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.__dict__[self.updated_at] = self.updated_at.isoformat()
        self.__dict__[self.updated_at] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.__dict__["__class__"] = self.__class__.__name__
        return f"{self.__dict__}"
