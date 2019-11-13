#!/usr/bin/python3
"""
Defines and executes the console
"""
import models
from ast import literal_eval
from cmd import Cmd
from re import fullmatch
from shlex import quote, split


class HBNBCommand(Cmd):
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
        return True

    def do_EOF(self, line):
        """Quit command to exit the program"""
        print()
        models.storage.save()
        return True

    def do_all(self, line):
        """Show all instances of a given model or if unspecified, all models"""
        try:
            token = split(line)
        except ValueError:
            return None
        objects = models.storage.all()
        if len(token) < 1:
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
        try:
            token = split(line)
        except ValueError:
            return None
        if len(token) < 1:
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
        try:
            token = split(line)
        except ValueError:
            return None
        if len(token) < 1:
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
        try:
            token = split(line)
        except ValueError:
            return None
        if len(token) < 1:
            print("** class name missing **")
        else:
            cls = models.getmodel(token[0])
            if cls is None:
                print("** class doesn't exist **")
            elif len(token) < 2:
                print("** instance id missing **")
            elif ('.'.join(token[0:2]) not in models.storage.all()):
                print("** no instance found **")
            else:
                del models.storage.all()['.'.join(token[0:2])]
                models.storage.save()

    def do_show(self, line):
        """Show a given instance of a model"""
        try:
            token = split(line)
        except ValueError:
            return None
        if len(token) < 1:
            print("** class name missing **")
        else:
            cls = models.getmodel(token[0])
            if cls is None:
                print("** class doesn't exist **")
            elif len(token) < 2:
                print("** instance id missing **")
            elif ('.'.join(token[0:2]) not in models.storage.all()):
                print("** no instance found **")
            else:
                print(models.storage.all()['.'.join(token[0:2])])

    def do_update(self, line):
        """Update a given instance of a model"""
        try:
            token = split(line)
        except ValueError:
            return None
        if len(token) < 1:
            print("** class name missing **")
        else:
            cls = models.getmodel(token[0])
            if cls is None:
                print("** class doesn't exist **")
            elif len(token) < 2:
                print("** instance id missing **")
            elif ('.'.join(token[0:2]) not in models.storage.all()):
                print("** no instance found **")
            elif len(token) < 3:
                print("** attribute name missing **")
            elif len(token) < 4:
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

    def precmd(self, line):
        """Parse <class>.<command>(<args>) syntax"""
        regex = r"([A-Za-z_][A-Za-z0-9_]*)\.([A-Za-z_][A-Za-z0-9_]*)\((.*)\)"
        match = fullmatch(regex, line.strip())
        if not match:
            return line
        cls, cmd, args = match.groups()
        if cmd != "update" or "," not in args:
            return " ".join([cmd, cls, args])
        inst, args = args.split(",", maxsplit=1)
        try:
            pairs = literal_eval(args.strip())
            for key, value in pairs.items():
                command = " ".join([cmd, cls, inst, quote(key), quote(value)])
                self.cmdqueue.append(command)
            return ""
        except (AttributeError, SyntaxError, ValueError):
            return " ".join([cmd, cls, inst] + args.split(","))


if __name__ == "__main__":
    HBNBCommand().cmdloop()
