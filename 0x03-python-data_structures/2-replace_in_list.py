#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """Replace an element of a list at a specific position

    Arguments:
    my_list -- the list
    idx -- the index of element to replace
    element -- new element
    """
    if idx > (len(my_list) - 1) or idx < 0:
        return (my_list)
    my_list[idx] = element
    return (my_list)


if __name__ == "__main__":
    import sys
