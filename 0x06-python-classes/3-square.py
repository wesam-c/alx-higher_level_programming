#!/usr/bin/python3
"""Square module."""

class Square:
    """Defines a square."""
    def __init__(self, size=0):
        """Constructor.

        Args:
            size: length of a side of the square.

        Raise:
            TypeError: If size is not an integar.
            ValueError: If size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integar')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Area of the square.
        
        Returns:
            the size of square    
        """
        return self.__size ** 2
