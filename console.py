#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
