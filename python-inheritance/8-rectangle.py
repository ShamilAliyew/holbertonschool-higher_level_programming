#!/usr/bin/python3
"""a class BaseGeometry"""


class BaseGeometry:
    """a class BaseGeometry"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("%s must be an integer" % name)
        if value <= 0:
            raise ValueError("%s must be greater than 0" % name)


class Rectangle(BaseGeometry):
    """a class Rectangle"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def integer_validator(self, width, height):
        if type(width) is not int and type(height) is not int:
            raise TypeError("%d and %d must be an integer" % width, height)
        if width <= 0 and height <=0:
            raise ValueError("%d and %d must be greater than 0" % width, height)
