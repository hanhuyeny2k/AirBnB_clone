#!/usr/bin/python3
"""
Defines and executes the console
"""
import models
import sys
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
            tokens = split(line)
        except ValueError:
            return None
        objects = models.storage.all()
        if len(tokens) < 1:
            print([str(obj) for obj in objects.values()])
        else:
            cls = models.getmodel(tokens[0])
            if cls is None:
                print("** class doesn't exist **")
            else:
                matches = []
                for obj in objects.values():
                    if type(obj) is cls:
                        matches.append(str(obj))
                print(matches)

    def do_count(self, line):
        """Count the instances of a given model"""
        try:
            tokens = split(line)
        except ValueError:
            return None
        objects = models.storage.all()
        if len(tokens) < 1:
            print("** class name missing **")
        else:
            cls = models.getmodel(tokens[0])
            if cls is None:
                print("** class doesn't exist **")
            else:
                matches = 0
                for obj in objects.values():
                    if type(obj) is cls:
                        matches += 1
                print(matches)

    def do_create(self, line):
        """Instantiate a given model"""
        try:
            tokens = split(line)
        except ValueError:
            return None
        if len(tokens) < 1:
            print("** class name missing **")
        else:
            cls = models.getmodel(tokens[0])
            if cls is None:
                print("** class doesn't exist **")
            else:
                instance = cls()
                models.storage.save()
                print(instance.id)

    def do_destroy(self, line):
        """Delete a given instance of a model"""
        try:
            tokens = split(line)
        except ValueError:
            return None
        if len(tokens) < 1:
            print("** class name missing **")
        else:
            objects = models.storage.all()
            cls = models.getmodel(tokens[0])
            if cls is None:
                print("** class doesn't exist **")
            elif len(tokens) < 2:
                print("** instance id missing **")
            elif ".".join(tokens[:2]) not in objects:
                print("** no instance found **")
            else:
                del objects[".".join(tokens[:2])]
                models.storage.save()

    def do_show(self, line):
        """Show a given instance of a model"""
        try:
            tokens = split(line)
        except ValueError:
            return None
        if len(tokens) < 1:
            print("** class name missing **")
        else:
            objects = models.storage.all()
            cls = models.getmodel(tokens[0])
            if cls is None:
                print("** class doesn't exist **")
            elif len(tokens) < 2:
                print("** instance id missing **")
            elif ".".join(tokens[:2]) not in objects:
                print("** no instance found **")
            else:
                print(objects[".".join(tokens[:2])])

    def do_update(self, line):
        """Update a given instance of a model"""
        try:
            tokens = split(line)
        except ValueError:
            return None
        if len(tokens) < 1:
            print("** class name missing **")
        else:
            objects = models.storage.all()
            cls = models.getmodel(tokens[0])
            if cls is None:
                print("** class doesn't exist **")
            elif len(tokens) < 2:
                print("** instance id missing **")
            elif ".".join(tokens[:2]) not in objects:
                print("** no instance found **")
            elif len(tokens) < 3:
                print("** attribute name missing **")
            elif len(tokens) < 4:
                print("** value missing **")
            else:
                obj = objects[".".join(tokens[:2])]
                for key, value in zip(tokens[2::2], tokens[3::2]):
                    try:
                        setattr(obj, key, int(value))
                    except ValueError:
                        try:
                            setattr(obj, key, float(value))
                        except ValueError:
                            try:
                                setattr(obj, key, str(value))
                            except ValueError:
                                pass
                obj.save()

    def precmd(self, line):
        """Parse <class>.<command>(<args>) syntax"""
        regex = r"([A-Za-z_][A-Za-z0-9_]*)\.([A-Za-z0-9_]+)\((.*)\)"
        match = fullmatch(regex, line.strip())
        if not match:
            return line
        cls, cmd, args = match.groups()
        if "," not in args:
            return " ".join([cmd, cls, args])
        if cmd != "update":
            return " ".join([cmd, cls] + args.split(","))
        inst, args = args.split(",", maxsplit=1)
        try:
            pairs = literal_eval(args.strip())
        except (SyntaxError, ValueError):
            pairs = ""
        if type(pairs) is not dict:
            return " ".join([cmd, cls, inst] + args.split(",", maxsplit=1))
        args = []
        for key, value in pairs.items():
            args.extend([quote(str(key)), quote(str(value))])
        return " ".join([cmd, cls, inst] + args)


if __name__ == "__main__":
    try:
        HBNBCommand().cmdloop()
    except KeyboardInterrupt:
        sys.exit(130)
