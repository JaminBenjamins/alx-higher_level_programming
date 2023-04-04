""" Print new lines after chracter """


def text_indentation(text):
    """
        Args:
            text(str) - text to print while adding lines

        Raises:
            TypeError - text must be a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] == "\n" or text[i] in ".?:":
            if text[i] in ".?:":
                print("\n")
            c += 1
        while i < len(text) and text[i] == ' ':
            c += 1
            continue
        c += 1
