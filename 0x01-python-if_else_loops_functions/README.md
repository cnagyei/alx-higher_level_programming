# 0x01. Python - if/else, loops, functions

## Resources

- [More Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html) (_Read until "4.6. Defining Functions" included_)
- [IndentationError](https://www.youtube.com/watch?v=1QXOd2ZQs-Q)
- [How To Use String Formatters in Python 3](https://www.digitalocean.com/community/tutorials/how-to-use-string-formatters-in-python-3)
- [Learn to Program](https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt)
- [Learn to Program 2 : Looping](https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt)
- [Pycodestyle – Style Guide for Python Code](https://pypi.org/project/pycodestyle/)

### man or help:

- `python3`

## Tasks

### 0. Positive anything is better than negative nothing

This program will assign a random signed number to the variable `number` each time it is executed. Complete the source code in order to print whether the number stored in the variable `number` is positive or negative.

- You can find the source code [here](https://github.com/alx-tools/0x01.py/blob/master/0-positive_or_negative_py)
- The variable `number` will store a different value every time you will run this program
- You don't have to understand what `import`, `random. randint` do. Please do not touch this code
- The output of the program should be:
	- The number, followed by
		- if the number is greater than 0: is positive
		- if the number is 0: is zero
		- if the number is less than 0: is negative
	- followed by a new line

```sh
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
-4 is negative
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
0 is zero
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
-3 is negative
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
-10 is negative
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
10 is positive
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
-5 is negative
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
6 is positive
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
7 is positive
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
5 is positive
guillaume@ubuntu:~/0x01$
```

### 1. The last digit

This program will assign a random signed number to the variable `number` each time it is executed. Complete the source code in order to print the last digit of the number stored in the variable `number`

- You can find the source code [here](https://github.com/alx-tools/0x01.py/blob/master/1-last_digit_py)
- The variable `number` will store a different value every time you will run this program
- You don't have to understand what `import`, `random.randint` do. Please do not touch this code. This line should not change: `number = random.randint(-10000, 10000)`
- The output of the program should be:
	- The string `Last digit of`, followed by
	- the number, followed by
	- the string `is`, followed by the last digit of `number`, followed by
		- if the last digit is greater than 5: the string `and is greater than 5`
		- if the last digit is 0: the string `and is 0`
		- if the last digit is less than 6 and not 0: the string `and is less than 6 and not 0`
		- followed by a new line

```sh
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 4205 is 5 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -626 is -6 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 1144 is 4 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -9200 is 0 and is 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 5247 is 7 and is greater than 5
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -9318 is -8 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 3369 is 9 and is greater than 5
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -5224 is -4 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -4485 is -5 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 3850 is 0 and is 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 5169 is 9 and is greater than 5
guillaume@ubuntu:~/0x01$
```