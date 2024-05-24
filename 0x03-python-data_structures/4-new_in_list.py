#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replace an element of a list at a specific position
    without modifying the orinal list

    Arguments:
    my_list -- the list
    idx -- the index of element to replace
    element -- new element
    """
    new_list = my_list[:]
    if idx > (len(my_list) - 1) or idx < 0:
        return (my_list)
    new_list[idx] = element
    return (new_list)


if __name__ == "__main__":
    import sys
