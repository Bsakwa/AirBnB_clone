#!/usr/bin/python3

# Author: Brian Sakwa
"""Defines the AirBnB command line interpreter"""
import cmd
import sys
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.user import User
from models.state import State


def parse_line(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """ Represents our AirBnB interpreter

    Attributes:
        prompt (str): Command line prompt
    """

    prompt = "(hbnb)"
    __classes = {
            "User",
            "State",
            "Amenity",
            "Place",
            "Review",
            "City",
            "BaseModel"
    }

    def emptyline(self):
        """Does nothing when it receives an empty line"""
        self.non_interactive_check()
        pass

    def do_quit(self, arg):
        """Quit command to exit the interpreter"""
        return True

    def do_EOF(self, arg):
        """EOF signal to quit the program"""
        print("")
        return True

    @staticmethod
    def non_interactive_check():
        if sys.stdin.isatty() is False:
            print("")

    def do_create(self, arg):
        """
        Usage: create <class>
        Creates a new instance of BaseModel
        Saves it to the JSON file
        """
        self.non_interactive_check()
        argl = parse_line(arg)
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(argl[0]).id)
            storage.save()

    def do_show(self, arg):
        """
        Usage: show <class> <id>
        Prints the string representation of an instance
        """
        self.non_interactive_check()
        argl = parse_line(arg)
        objedict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objedict:
            print("** no instance found **")
        else:
            print(objedict["{}.{}".format(argl[0], argl[1])])

    def do_destroy(self, arg):
        """
        Usage: destroy <class> <id>
        Deletes an instance based on class name and id
        Saves the change into the JSON file
        """
        argsl = parse_line(arg)
        objedict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objedict.keys():
            print("** no instance found **")
        else:
            del objedict["{}.{}".format(argl[0], argl[1])]
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
