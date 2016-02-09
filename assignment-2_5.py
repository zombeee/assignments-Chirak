#! /usr/bin/env python

"""
Homework 2 (3 and 5 tasks)
"""


from __future__ import division, print_function
import operator



def my_filter(fn, elements, **kwargs):
    """
    This function returns a list from those elements of iterable
     for which function returns true
    :param fn: eny function
    :param elements: eny iterable
    :param kwargs: additional arguments for function
    """
    result = []
    for element in elements:
        if fn(element, **kwargs):
            result.append(fn(element, **kwargs))
    return result

my_filter(bool, [1, 0, [], [1, 3, 5]])


def calculate(string):
    calculator_dict = {
        "+": operator.add,
        "-": operator.sub,
    }
    list_to_ignor = ["(", ")", " "]
    numbers = []
    operations = []
    for things in string:
        if things in list_to_ignor:
            continue
        if things == ".":
            raise ValueError("Supported only integer numbers")
        if not numbers and things == "-":
            numbers.append(0)
        if things.isdigit():
            numbers.append(int(things))
        else:
            operations.append(things)
    numbers_iterator = iter(numbers)
    acc = next(numbers_iterator)
    for num, oper in zip(numbers_iterator, operations):
        oper_funct = calculator_dict.get(oper)
        if not calculator_dict.get(oper):
            raise ValueError("Operation {} is not supported".format(oper))
        acc = oper_funct(acc, num)
    return acc

calculate(" -1- 5+6 (+6) - 7 ")
calculate(" 1- 5+6 (+6) - 7 ")


