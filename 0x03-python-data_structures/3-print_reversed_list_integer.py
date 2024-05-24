#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Print all integers of a list in reverse.

    Arguments:
    my_list -- the list
    """
    for i in reversed(range(len(my_list))):
        print("{:d}".format(my_list[i]))


if __name__ == "__main__":
    import sys
