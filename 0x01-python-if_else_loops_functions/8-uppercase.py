#!/usr/bin/python3
def uppercase(str):
    """Prints a string in uppercase followed by a new line"""

    for c in range(len(str)):
        ascii_pt = ord(str[c])
        if ascii_pt >= 97 and ascii_pt <= 122:
            print("{}".format(chr(ascii_pt - 32)), end="")
        else:
            print("{}".format(str[c]), end="")
