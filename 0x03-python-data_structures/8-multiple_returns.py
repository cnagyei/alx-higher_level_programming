#!/usr/bin/python3
def multiple_returns(sentence):
    """Return tuple with length of string and first character.

    Arguments:
    sentence -- string
    """
    strlen = len(sentence)
    if strlen == 0:
        return ((0, None))
        exit(1)

    first_char = sentence[0]

    return ((strlen, first_char))


if __name__ == "__main__":
    import sys
