"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
"""
# No setup
repeat forever:
    read input
    tokenize input
    if the first token is "q":
        quit
    else:
        decide which math function to call based on first token
"""


while True:
    user_input = raw_input("> ")
    if user_input == "q":
        break
    #change the string to a list
    user_input = user_input.strip().split(" ")
    operator = user_input[0]
    operand1 = float(user_input[1])
    #check the len of list
    if len(user_input) >= 3:
        operand2 = float(user_input[2])
        if len(user_input) == 4:
            operand3 = float(user_input[3])

    if operator == "+":
        print add(operand1, operand2)
    elif operator == "-":
        print subtract(operand1, operand2)
    elif operator == "*":
        print multiply(operand1, operand2)
    elif operator == "/":
        print divide(operand1, operand2)
    elif operator == "square":
        print square(operand1)
    elif operator == "cube":
        print cube(operand1)
    elif operator == "pow":
        print power(operand1, operand2)
    elif operator == "mod":
        print mod(operand1, operand2)
    elif operator == "cubes+":
        print add_cubes(operand1, operand2)
    elif operator == "x+":
        print add_mult(operand1, operand2, operand3)
