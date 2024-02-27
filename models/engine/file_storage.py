import json
"""
    File storage class
"""


class FileStorage:
    """ Saka suka ba ba """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects = obj

    def save(self):
        with open('file.json', "w") as f:
            f.write(json.dumps(__class__.__objects))

    def reload(self):
        try:
            with open('file.json', "r") as f:
                self.__objects = json.load(f.read())
        except Exception:
            pass
