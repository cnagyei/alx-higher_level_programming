#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    if len(argv) == 1:
        print("0")
    elif len(argv) == 2:
        print("{}".format(argv[1]))
    elif len(argv) > 2:
        sum = 0
        for i in range(1, len(argv)):
            sum += int(argv[i])
        print("{}".format(sum))
