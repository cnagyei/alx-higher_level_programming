#!/usr/bin/python3
def remove_char_at(str, n):
    """
    Create a string copy, remove character at position

    Args:
        @str: input string
        @n: position
    """
    if n < 0:
        return (str)
    return (str[:n] + str[n+1:])
