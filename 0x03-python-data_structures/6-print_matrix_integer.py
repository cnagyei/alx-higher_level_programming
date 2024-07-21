#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers.

    Arguments:
    matrix -- Matrix of integers
    """
    for row in matrix:
        for element in row:
            print("{:d}".format(element), end=" ")
        print("")

if __name__ == "__main__":
    import sys
