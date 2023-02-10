#!/usr/bin/python3

# Author: Brian Sakwa
"""Defines the AirBnB command line interpreter"""
import cmd


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
        pass

    def do_quit(self, arg):
        """Quit command to exit the interpreter"""
        return True

    def do_EOF(self, arg):
        """EOF signal to quit the program"""
        print("")
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
