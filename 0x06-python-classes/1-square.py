#!/usr/bin/python3

class Square:
    """class definition."""

    def __init__(self, size):
        """constructor.

        Args:
            size: of the square.
        """
        self.__size = size
        """The double underscore before size indicates it is a private variable."""
