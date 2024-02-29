"""
    HBNB console entry point
"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBNB console."""
    
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program when EOF (Ctrl+D) is reached."""
        print("")
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def do_create(self, arg):
        """ Create instance of BaseModel """
        if (arg == ""):
            print("** class name missing **")
        elif (arg != "BaseModel"):
            print("** class doesn't exist **")
        else:
            item = BaseModel()
            item.save()
            print(item.id)

    def do_show(self, arg):
        arg1,arg2 = arg.split()
        print (arg1)
        print (arg2)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
