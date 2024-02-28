#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models import storage
"""
    Defines the HBnB console.
"""


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBNB console."""
    
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        quit()
        return True

    def do_EOF(self, arg):
        """Exit the program when EOF is reached."""
        print("")
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def do_create(self, arg):
        if (arg == ""):
            print("** class name missing **")
        elif (arg != "BaseModel"):
            print("** class doesn't exist **")
        else:
            item = BaseModel()
            item.save()
            print(item.id)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
