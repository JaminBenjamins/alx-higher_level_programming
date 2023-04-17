#!/usr/bin/python3
"""Defines a base model class."""
import json
import csv
import turtle


class Base:
    """Represent the base model.

    Represents the "base" for all other classes in the project.

    Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
            id (int): The identity of the new class.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dicts):
        """Return the JSON serialization of a list of dictionaries.

        Args:
            list_dicts (list): A list of dictionaries.
        """
        if list_dicts is None or list_dicts == []:
            return "[]"
        return json.dumps(list_dicts)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        fname = cls.__name__ + ".json"
        with open(fname, "w") as jsonfil:
            if list_objs is None:
                jsonfil.write("[]")
            else:
                is_dict = [i.to_dictionary() for i in list_objs]
                jsonfil.write(Base.to_json_string(is_dict))

    @staticmethod
    def from_json_string(json_string):
        """Return the deserialization of a JSON string.

        Args:
            json_string (str): A JSON string representation of a list of dicts.
        Return:
            If json_string is None or empty - an empty list.
            Otherwise - the Python list represented by json_string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a class instantiated from a dictionary of attributes.

        Args:
            **dict: Key/value pairs of attributes to initialize.
        """
        if dict and dict != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON strings.

        Reads from .json file.

        Return:
            An empty list - if the .json file is empty
            Otherwise - a list of instantiated objects.
        """
        fname = str(cls.__name__) + ".json"
        try:
            with open(fname, "r") as jsonfil:
                is_dict = Base.from_json_string(jsonfil.read())
                return [cls.create(**d) for d in is_dict]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        fname = cls.__name__ + ".csv"
        with open(fname, "w", newline="") as csvfil:
            if list_objs is None or list_objs == []:
                csvfil.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldname = ["id", "width", "height", "x", "y"]
                else:
                    fieldname = ["id", "size", "x", "y"]
                riter = csv.DictWriter(csvfil, fieldname=fieldname)
                for objec in list_objs:
                    riter.writerow(objec.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a dictionary object instantiated from a CSV file.

        Reads from `<cls.__name__>.csv`.

        Returns:
            An empty list if the file does not exist.
            Otherwise - a list of instantiated objects.
        """
        fname = cls.__name__ + ".csv"
        try:
            with open(fname, "r", newline="") as csvfil:
                if cls.__name__ == "Rectangle":
                    fieldname = ["id", "width", "height", "x", "y"]
                else:
                    fieldname = ["id", "size", "x", "y"]
                is_dict = csv.DictReader(csvfil, fieldname=fieldname)
                is_dict = [dict([k, int(v)] for k, v in d.items())
                              for d in is_dict]
                return [cls.create(**d) for d in is_dict]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw objects using the turtle module.

        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        urt = turtle.Turtle()
        urt.screen.bgcolor("#bf2e28")
        urt.pensize(3)
        urt.shape("turtle")

        urt.color("#ffffff")
        for rect in list_rectangles:
            urt.showturtle()
            urt.up()
            urt.goto(rect.x, rect.y)
            urt.down()
            for i in range(2):
                urt.forward(rect.width)
                urt.left(90)
                urt.forward(rect.height)
                urt.left(90)
            urt.hideturtle()

        urt.color("#b5e3d8")
        for sq in list_squares:
            urt.showturtle()
            urt.up()
            urt.goto(sq.x, sq.y)
            urt.down()
            for i in range(2):
                urt.forward(sq.width)
                urt.left(90)
                urt.forward(sq.height)
                urt.left(90)
            urt.hideturtle()

        turtle.exitonclick()
