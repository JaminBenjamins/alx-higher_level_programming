#!/usr/bin/python3
""" Defining a square function printing a special character """


def print_square(size):
    """
        Args:
            size(int) - the size of a square

        Raises:
            TypeError - if size is not integer
            ValueError - if size < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size ust be >= 0")

    for i in range(size):
        [print('#', end="") for j in range(size)]
        print("")
