#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """Add 2 tuples.

    Arguments:
    tuple_a -- first tuple
    tuple_b -- second tuple

    Return: Tuple with 2 integers
    """
    add_two_zeros = (0, 0)
    add_one_zero = (0,)
    # tuple_a is empty
    if len(tuple_a) == 0:
        tuple_a += add_two_zeros

    # if tuple_a contains 1 element
    elif len(tuple_a) == 1:
        tuple_a += add_one_zero

    # tuple_b is empty
    if len(tuple_b) == 0:
        tuple_b += add_two_zeros

    # if tuple_b contains 1 element
    elif len(tuple_b) == 1:
        tuple_b += add_one_zero

    # unpack tuples
    x, y = tuple_a
    q, r = tuple_b

    # add elements
    x += q
    y += r

    # pack tuples
    tuples_added = x, y

    return (tuples_added)


if __name__ == "__main__":
    import sys
