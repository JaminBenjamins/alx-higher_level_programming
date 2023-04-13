#!/usr/bin/python3
""" a function that append a file """


def append_write(filename="", text=""):
    """ Apend a string tp UTF-8 file
        Args:
            filename = the file where text is appended 
            text - the text to be appended

        Return:
            Number of characters added
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
