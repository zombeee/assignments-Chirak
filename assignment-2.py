#! /usr/bin/env python


from __future__ import division, print_function


def my_max(*args):
    """
    This function find max in given sequence of simple numbers, or in
    given tuple or in list
    """
    if not args:
        raise ValueError("Can't find max, no data given")
    if len(args) == 1:
        numbers = args[0]
        if isinstance(numbers, (list, tuple)):
            for thing in numbers:
                if not isinstance(thing, int):
                    raise ValueError("Can't find max, wrong data format")
            return sorted(numbers)[-1]
        if isinstance(numbers, int):
            return numbers
        raise ValueError("Can't find max, wrong data format")
    else:
        for num in args:
            if not isinstance(num, int):
                raise ValueError("Can't find max, wrong data format")
        return sorted(args)[-1]


my_max([1, 3, -8, 9])
my_max((1, 3, -8, 9))
my_max((1, 3, -8, 9.5))
my_max(1, 3, -8, 9)
my_max(1)
my_max(1.1)
my_max()
my_max(1, 3, -8, 9, 9.8)
my_max(0.95, 1, 3, -8, 9, 9.8)


def my_min(*args):
    """
    This function find min in given sequence of simple numbers, or in
    given tuple or in list
    """
    if not args:
        raise ValueError("Can't find max, no data given")
    if len(args) == 1:
        numbers = args[0]
        if isinstance(numbers, (list, tuple)):
            for thing in numbers:
                if not isinstance(thing, int):
                    raise ValueError("Can't find max, wrong data format")
            return sorted(numbers)[0]
        if isinstance(numbers, int):
            return numbers
        raise ValueError("Can't find max, wrong data format")
    else:
        for num in args:
            if not isinstance(num, int):
                raise ValueError("Can't find max, wrong data format")
        return sorted(args)[0]

my_min([1, 3, -8, 9])
my_min((1, 3, -8, 9))
my_min((1, 3, -8, 9.5))
my_min(1, 3, -8, 9)
my_min(1)
my_min(1.1)
my_min()
my_min(1, 3, -8, 9, 9.8)
my_min(0.95, 1, 3, -8, 9, 9.8)
