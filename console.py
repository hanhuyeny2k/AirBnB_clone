#!/usr/bin/python3
"""
Defines and executes the console
"""
import cmd
import models
import re
import shlex
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
        try:
            token = shlex.split(line)
        except ValueError:
            return
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
            token = shlex.split(line)
        except ValueError:
            return
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
            token = shlex.split(line)
        except ValueError:
            return
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
            token = shlex.split(line)
        except ValueError:
            return
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
            token = shlex.split(line)
        except ValueError:
            return
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
            token = shlex.split(line)
        except ValueError:
            return
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
        ident = r"[A-Za-z_][A-Za-z0-9_]*"
        regex = r"(" + ident + r")\.(" + ident + r")\((.*)\)"
        match = re.fullmatch(regex, line.strip())
        if match:
            cls, cmd, args = match.groups()
            if cmd == "update" and "," in args:
                inst, args = [s.strip() for s in args.split(",", maxsplit=1)]
                entry = r"[^ \t:][^:]*:\s*[^ \t,][^,]*"
                regex = r"\{(\s*" + entry + r"(\s*,\s*" + entry + r")*)?\s*}"
                if re.fullmatch(regex, args):
                    args = args[1:-1].split(",")
                    args = [s.split(":", maxsplit=1) for s in args]
                    if all(len(ls) == 2 for ls in args):
                        args = [[s.strip() for s in ls] for ls in args]
                        for key, value in args:
                            command = " ".join([cmd, cls, inst, key, value])
                            self.cmdqueue.append(command)
                    return ""
                return " ".join([cmd, cls, inst] + args.split(","))
            return " ".join([cmd, cls] + args.split(","))
        return line


if __name__ == "__main__":
    try:
        HBNBCommand().cmdloop()
    except KeyboardInterrupt:
        print()
        sys.exit(130)
