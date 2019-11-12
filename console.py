#!/usr/bin/python3
"""
"""

import cmd
import re
import shlex
import sys
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


def getcls(module, name):
    """
    """
    for item in dir(module):
        attr = getattr(module, item)
        if type(attr) is type(models) and name in dir(attr):
            return getattr(attr, name)
    return None


class HBNBCommand(cmd.Cmd):
    """
    """
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Quit command to exit the program"""
        print()
        models.storage.save()
        sys.exit()

    def do_quit(self, line):
        """Quit command to exit the program"""
        models.storage.save()
        sys.exit()

    def emptyline(self):
        """
        """
        pass

    def do_create(self, line):
        """
        """
        token = shlex.split(line)
        if (len(token) < 1):
            print("** class name missing **")
        else:
            cls = getcls(models, token[0])
            if cls is None:
                print("** class doesn't exist **")
            else:
                instance = cls()
                models.storage.save()
                print(instance.id)

    def do_show(self, line):
        """
        """
        token = shlex.split(line)
        if (len(token) < 1):
            print("** class name missing **")
        else:
            cls = getcls(models, token[0])
            if cls is None:
                print("** class doesn't exist **")
            elif (len(token) < 2):
                print("** instance id missing **")
            elif ('.'.join(token[0:2]) not in models.storage.all()):
                print("** no instance found **")
            else:
                print(models.storage.all()['.'.join(token[0:2])])

    def do_destroy(self, line):
        """
        """
        token = shlex.split(line)
        if (len(token) < 1):
            print("** class name missing **")
        else:
            cls = getcls(models, token[0])
            if cls is None:
                print("** class doesn't exist **")
            elif (len(token) < 2):
                print("** instance id missing **")
            elif ('.'.join(token[0:2]) not in models.storage.all()):
                print("** no instance found **")
            else:
                del models.storage.all()['.'.join(token[0:2])]
                models.storage.save()

    def do_all(self, line):
        """
        """
        token = shlex.split(line)
        dictionary = models.storage.all()
        if (len(token) < 1):
            for key in dictionary:
                print(dictionary[key])
        else:
            cls = getcls(models, token[0])
            if cls is None:
                print("** class doesn't exist **")
            else:
                for _, value in dictionary.items():
                    if value.__class__.__name__ == token[0]:
                        print(value)

    def do_update(self, line):
        """
        """
        token = shlex.split(line)
        if (len(token) < 1):
            print("** class name missing **")
        else:
            cls = getcls(models, token[0])
            if cls is None:
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
                try:
                    setattr(obj, token[2], int(token[3]))
                except ValueError:
                    try:
                        setattr(obj, token[2], float(token[3]))
                    except ValueError:
                        setattr(obj, token[2], token[3])
                obj.save()

    def do_count(self, line):
        """
        """
        token = shlex.split(line)
        if (len(token) < 1):
            print("** class name missing **")
        else:
            cls = getcls(models, token[0])
            if cls is None:
                print("** class doesn't exist **")
            else:
                count = 0
                for value in models.storage.all().values():
                    if value.__class__.__name__ == token[0]:
                        count += 1
                print(count)

    def precmd(self, line):
        """
        """
        match = re.match(
            r'\s*([_A-Za-z]+[_A-Za-z0-9]*)\.([_A-Za-z]+[_A-Za-z0-9]*)\((.*)\)',
            line
        )
        if match:
            cls, cmd, args = match.groups()
            return ' '.join([cmd, cls] + args.split(','))
        return line


if __name__ == "__main__":
    command_hbnb = HBNBCommand()
    command_hbnb.cmdloop()
