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
    # operand1 = float(user_input[1])
    # #check the len of list
    # if len(user_input) >= 3:
    #     operand2 = float(user_input[2])
    #     if len(user_input) == 4:
    #         operand3 = float(user_input[3])
    operands = user_input[1:]
    float_operands = []
    #change all integer to float
    for operand in operands:
        operand = float(operand)
        float_operands.append(operand)


    if operator == "+":
        print add(float_operands)
    elif operator == "-":
        print subtract(operands)
    elif operator == "*":
        print multiply(operands)
    elif operator == "/":
        print divide(operands)
    elif operator == "square":
        print square(operands)
    elif operator == "cube":
        print cube(operands)
    elif operator == "pow":
        print power(operands)
    elif operator == "mod":
        print mod(operands)
    elif operator == "cubes+":
        print add_cubes(operands)
    elif operator == "x+":
        print add_mult(operands)
