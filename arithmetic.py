"""Math functions for calculator."""

# def common_function(operands_lst, operator):
#     total = operands_lst[0]
#     operation = operator + "="
#     for i in range(1,len(operands_lst)):
#         total  operands_lst[i]


def add(lst):
    """Return the sum of the two inputs."""
    return reduce(lambda a, b: a + b, lst)


def subtract(lst):
    """Return the second number subtracted from the first."""
    return reduce(lambda a, b: a - b, lst)


def multiply(lst):
    """Multiply the two inputs together."""
    return reduce(lambda a, b: a * b, lst)


def divide(lst):
    """Divide the first input by the second and return the result."""
    return reduce(lambda a, b: a / b, lst)


def square(lst):
    """Return the square of the input."""
    return lst[0] ** 2


def cube(lst):
    """Return the cube of the input."""
    return lst[0] ** 3


def power(num1, num2):
    """Raise num1 to the power of num2 and return the value."""
    return reduce(lambda a, b: a ** b, lst)


def mod(num1, num2):
    """Return the remainder of num1 / num2."""
    return reduce(lambda a, b: a % b, lst)


def add_mult(lst):
    """add first two and multiply sum with third"""
    return (lst[0] + lst[1]) * lst[2]


def add_cubes(num1, num2):
    """cube both numbers and sum them"""
    return reduce(lambda a, b: a + (b ** 3), lst, 0)
