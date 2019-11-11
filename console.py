#!/usr/bin/python3
"""
"""

import cmd
import sys
import shlex
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    """
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Quit command to exit the program"""
        print()
        sys.exit()

    def do_quit(self, line):
        """Quit command to exit the program"""
        sys.exit()

    def emptyline(self):
        pass

    def do_create(self, line):
        token = shlex.split(line)
        if (len(token) < 1):
            print("** class name missing **")
        elif token[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            Base = BaseModel()
            Base.save()
            print(Base.id)

    def do_show(self, line):
        token = shlex.split(line)
        if (len(token) < 1):
            print("** class name missing **")
        elif token[0] != "BaseModel":
            print("** class doesn't exist **")
        elif (len(token) < 2):
            print("** instance id missing **")
        elif ('.'.join(token[0:2]) not in models.storage.all()):
            print("** no instance found **")
        else:
            print(models.storage.all()['.'.join(token[0:2])])

    def do_destroy(self, line):
        token = shlex.split(line)
        if (len(token) < 1):
            print("** class name missing **")
        elif token[0] != "BaseModel":
            print("** class doesn't exist **")
        elif (len(token) < 2):
            print("** instance id missing **")
        elif ('.'.join(token[0:2]) not in models.storage.all()):
            print("** no instance found **")
        else:
            del models.storage.all()['.'.join(token[0:2])]

    def do_all(self, line):
        token = shlex.split(line)
        dictionary = models.storage.all()
        if (len(token) < 1):
            for key in dictionary:
                print(dictionary[key])
        elif token[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            for _, value in dictionary.items():
                if value.__class__.__name__ == token[0]:
                    print(value)

    def do_update(self, line):
        dictionary = models.storage.all()
        token = shlex.split(line)
        if (len(token) < 1):
            print("** class name missing **")
        elif token[0] != "BaseModel":
            print("** class doesn't exist **")
        elif (len(token) < 2):
            print("** instance id missing **")
        elif ('.'.join(token[0:2]) not in models.storage.all()):
            print("** no instance found **")
        elif (len(token) < 3):
            print("** attribute name missing **")
        elif (len(token) < 4):
            print("** value missing **")
        else:
            obj = models.storage.all()['.'.join(token[0:2])]
            setattr(obj, token[2], token[3])
            obj.save()


if __name__ == "__main__":
    command_hbnb = HBNBCommand()
    command_hbnb.cmdloop()
