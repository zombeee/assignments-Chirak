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
    if len(numbers) != len(operations) + 1:
        raise ValueError("msg")
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
    list_to_ignor = ["(", ")", " "]
    numbers = []
    operations = []
    string_for_numbers = ""
    for things in string:
        if things in list_to_ignor:
            continue
        if things == ".":
            raise ValueError("Supported only integer numbers")
        if not numbers and things is "-":
            numbers.append(0)
        if things.isdigit():
                string_for_numbers += things
        else:
            if string_for_numbers:
                numbers.append(int(string_for_numbers))
                string_for_numbers = ""
            operations.append(things)
    return calculate(numbers, operations)

evaluate_string(" 1- 5+66 (+6) + 7 ")



