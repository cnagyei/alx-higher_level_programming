#!/usr/bin/python3
def no_c(my_string):
    """Remove all characters c and C from a string.

    Arguments:
    my_string -- the string
    """
    new_string = []
    for i in range(len(my_string)):
        if my_string[i] not in "cC":
            new_string.append(my_string[i])
    return ("".join(new_string))


if __name__ == "__main__":
    import sys
