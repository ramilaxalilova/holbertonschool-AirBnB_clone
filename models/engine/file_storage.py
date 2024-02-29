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

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ Return dictionary """

        return FileStorage.__objects

    def new(self, obj):
        """ sets in dictionary in dict """

        FileStorage.__objects[f"{type(obj).__name__}.{obj.id}"] = obj

    def save(self):
        """ save to file """

        dct1 = {}
        for key, value in FileStorage.__objects.items():
            dct1[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as write:
            json.dump(dct1, write)

    def reload(self):
        """ load from file """

        try:
            with open(FileStorage.__file_path, "r") as read:
                tmp = json.load(read)
            for key, value in tmp.items():
                FileStorage.__objects[key] = base_model.BaseModel(**tmp[key])
        except Exception:
            pass
