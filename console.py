#!/usr/bin/python3
"""Defines and executes the console"""

import cmd
import models
import sys


class HBNBCommand(cmd.Cmd):
    """Defines console commands and behavior"""
    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing"""
        pass

    def do_help(self, line):
        """Display helpful messages"""
        super().do_help(line)

    def do_quit(self, line):
        """Quit command to exit the program"""
        models.storage.save()
        sys.exit()

    def do_EOF(self, line):
        """Quit command to exit the program"""
        print()
        self.do_quit(line)

    def do_all(self, line):
        """Show all instances of a given model or if unspecified, all models"""
        token = line.split()
        objects = models.storage.all()
        if (len(token) < 1):
            print([str(obj) for obj in objects.values()])
        else:
            cls = models.getmodel(token[0])
            if cls is None:
                print("** class doesn't exist **")
            else:
                values = []
                for obj in objects.values():
                    if obj.__class__.__name__ == token[0]:
                        values.append(str(obj))
                print(values)

    def do_count(self, line):
        """Count the instances of a given model"""
        token = line.split()
        if (len(token) < 1):
            print("** class name missing **")
        else:
            cls = models.getmodel(token[0])
            if cls is None:
                print("** class doesn't exist **")
            else:
                count = 0
                for value in models.storage.all().values():
                    if value.__class__.__name__ == token[0]:
                        count += 1
                print(count)

    def do_create(self, line):
        """Instantiate a given model"""
        token = line.split()
        if (len(token) < 1):
            print("** class name missing **")
        else:
            cls = models.getmodel(token[0])
            if cls is None:
                print("** class doesn't exist **")
            else:
                instance = cls()
                models.storage.save()
                print(instance.id)

    def do_destroy(self, line):
        """Delete a given instance of a model"""
        token = line.split()
        if (len(token) < 1):
            print("** class name missing **")
        else:
            cls = models.getmodel(token[0])
            if cls is None:
                print("** class doesn't exist **")
            elif (len(token) < 2):
                print("** instance id missing **")
            elif ('.'.join(token[0:2]) not in models.storage.all()):
                print("** no instance found **")
            else:
                del models.storage.all()['.'.join(token[0:2])]
                models.storage.save()

    def do_show(self, line):
        """Show a given instance of a model"""
        token = line.split()
        if (len(token) < 1):
            print("** class name missing **")
        else:
            cls = models.getmodel(token[0])
            if cls is None:
                print("** class doesn't exist **")
            elif (len(token) < 2):
                print("** instance id missing **")
            elif ('.'.join(token[0:2]) not in models.storage.all()):
                print("** no instance found **")
            else:
                print(models.storage.all()['.'.join(token[0:2])])

    def do_update(self, line):
        """Update a given instance of a model"""
        token = line.split()
        if (len(token) < 1):
            print("** class name missing **")
        else:
            cls = models.getmodel(token[0])
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


if __name__ == "__main__":
    try:
        command_hbnb = HBNBCommand()
        command_hbnb.cmdloop()
    except KeyboardInterrupt:
        print()
        sys.exit(130)
