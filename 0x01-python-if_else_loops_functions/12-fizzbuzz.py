#!/usr/bin/python3
def fizzbuzz():
    """Print number, Fizz, Buzz, or FizzBuzz"""
    for i in range(1, 101):
        if (i % 3 == 0) and not (i % 5 == 0):
            print("Fizz", end=" ")
        elif (i % 5 == 0) and not (i % 3 == 0):
            print("Buzz", end=" ")
        elif (i % 3 == 0) and (i % 5 == 0):
            print("FizzBuzz", end=" ")
        else:
            print("{}".format(i), end=" ")
