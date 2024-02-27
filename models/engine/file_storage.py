import json
"""
    File storage class
"""


class FileStorage:
    """ Saka suka ba ba """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = f"{type(obj).__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        new_dict = {}
        for k in self.__objects:
            new_dict[k] = self.__objects[k].to_dict()
        with open('file.json', "w") as f:
            json.dump(new_dict, f)

    def reload(self):
        try:
            with open('file.json', "r") as f:
                FileStorage.__objects = json.loads(f.read())
        except Exception:
            pass
