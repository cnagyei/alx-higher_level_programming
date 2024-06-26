#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    from sys import argv

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    operator = argv[2]

    if operator == "+":
        print("{} {} {} = {}".format(a, operator, b, (a + b)))
    elif operator == "-":
        print("{} {} {} = {}".format(a, operator, b, (a - b)))
    elif operator == "*":
        print("{} {} {} = {}".format(a, operator, b, (a * b)))
    elif operator == "/":
        print("{} {} {} = {}".format(a, operator, b, (a // b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
