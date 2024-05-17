#!/usr/bin/python3
def uppercase(str):
    """Prints a string in uppercase followed by a new line"""

    for c in str:
        ascii_pt = ord(c)
        if ascii_pt >= 97 and ascii_pt <= 122:
            c = chr(ascii_pt - 32)
        print("{}".format(c), end="")
    print("")
