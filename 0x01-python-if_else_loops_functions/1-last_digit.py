#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number >= 0:
    remainder = number % 10
    if remainder > 5:
        print("Last digit of {} is {} and is greater \
than 5".format(number, remainder))
    elif remainder == 0:
        print("Last digit of {} is {} and is 0".format(number, remainder))
    elif remainder < 6:
        print("Last digit of {} is {} and is less than 6 and \
not 0".format(number, remainder))

elif number < 0:
    abs_number = abs(number)
    remainder = abs_number % 10
    remainder *= -1
    print("Last digit of {} is {} and is less than 6 and \
not 0".format(number, remainder))
