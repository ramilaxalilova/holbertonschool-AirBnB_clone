"""
    Save & load dictionary to/from file
"""
import json
from models import base_model


class FileStorage:
    """ 
        file_path is file's name
        objects is dictionary
    """

    __file_path = 'hbbnb.json'
    __objects = {}

    def all(self):
        """ Return dictionary """

        return FileStorage.__objects

    def new(self, obj):
        """ sets in dictionary in dict """

        key = f"{type(obj).__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """ save to file """

        dct1 = {}
        for key, value in FileStorage.__objects.items():
            dct1[key] = value.to_dict()
        with open(FileStorage.__file_path, 'a') as write:
            json.dump(dct1, write)

    def reload(self):
        """ load from file """

        try:
            with open(FileStorage.__file_path, "r") as read:
                json.load(FileStorage.__objects, read) 
        except Exception:
            pass
