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


def calculate(numbers, operations):
    """
    This function use operations from (operations) to numbers from (numbers)
    :param numbers: List of the numbers
    :param operations: List of the operations
    (supported only "+" and "-" operations)
    :return: Result of calculations
    """
    if len(numbers) != len(operations) + 1:
        raise ValueError("Errors in given data")
    operation_dict = {
        "+": operator.add,
        "-": operator.sub
    }
    numbers_iterator = iter(numbers)
    acc = next(numbers_iterator)
    for num, oper in zip(numbers_iterator, operations):
        oper_func = operation_dict.get(oper)
        if not oper_func:
            raise ValueError("Operation {} is not supported".format(oper))
        acc = oper_func(acc, num)
    return acc


def evaluate_string(string):
    """
    This function use operations in string to numbers in string
     ignoring " ", "(" and ")"
    :param string: String with numbers and operations
    ("+" and "-" operations supported)
    :return: Calculation result
    """
    numbers = []
    operations = []
    list_for_string = []
    stack_for_colons = []
    for char in string:
        if char == " ":
            if list_for_string:
                raise ValueError("Missing operation")
            continue
        if char == "(" or char == ")":
            if not stack_for_colons or stack_for_colons[-1] == char:
                stack_for_colons.append(char)
            else:
                stack_for_colons.pop()
            if list_for_string:
                if char == "(":
                    raise ValueError("Unresolved brackets composition")
                numbers.append(int("".join(list_for_string)))
                list_for_string = []
            continue
        if char == ".":
            raise ValueError("Supported only integer numbers")
        if not numbers and not list_for_string and char == "-":
            numbers.append(0)
        if char.isdigit():
                list_for_string.append(char)
        else:
            if list_for_string:
                numbers.append(int("".join(list_for_string)))
                list_for_string = []
            operations.append(char)
    if stack_for_colons:
        raise ValueError("Additional(missed) brackets in given data")
    if list_for_string:
        numbers.append(int("".join(list_for_string)))
    return calculate(numbers, operations)

evaluate_string("1 +2 -2 +2+2 - 1 + 5 5")


