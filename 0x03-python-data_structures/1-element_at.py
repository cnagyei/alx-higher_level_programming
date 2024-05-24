#!/usr/bin/python3
def element_at(my_list, idx):
    """Retrieve an element from a list like in C

    Arguments:
    my_list -- the list
    idx -- the index of element to retrieve
    """
    if idx > (len(my_list) - 1) or idx < 0:
        return (None)
    return (my_list[idx])


if __name__ == "__main__":
    import sys
