#! /usr/bin/env python


from __future__ import division, print_function


def my_max(*args):
    """
    This function find max in given sequence of simple numbers, or in
    given tuple or in list
    """
    def sorter(sequence):
        """
        This function find max in gives sequence of simple numbers
        """
        for numbers in sequence:
            if not isinstance(numbers, int):
                raise ValueError("Can't find max, wrong data format")
        return sorted(sequence)[-1]
    if not args:
        raise ValueError("Can't find max, no data given")
    if len(args) == 1:
        thing = args[0]
        if isinstance(thing, (list, tuple)):
            return sorter(thing)
        if isinstance(thing, int):
            return thing
        raise ValueError("Can't find max, wrong data format")
    return sorter(args)


my_max([1, 3, -8, 9])
my_max((1, 3, -8, 9))
my_max((1, 3, -8, 9.5))
my_max(1, 3, -8, 9)
my_max(1)
my_max(1.1)
my_max()
my_max(1, 3, -8, 9, 9.8)


def my_min(*args):
    """
    This function find min in given sequence of simple numbers, or in
    given tuple or in list
    """
    def sorter(sequence):
        """
        This function find min in gives sequence of simple numbers
        """
        for numbers in sequence:
            if not isinstance(numbers, int):
                raise ValueError("Can't find min, wrong data format")
        return sorted(sequence)[0]
    if not args:
        raise ValueError("Can't find min, no data given")
    if len(args) == 1:
        thing = args[0]
        if isinstance(thing, (list, tuple)):
            return sorter(thing)
        if isinstance(thing, int):
            return thing
        raise ValueError("Can't find min, wrong data format")
    return sorter(args)


my_min([1, 3, -8, 9])
my_min((1, 3, -8, 9))
my_min((1, 3, -8, 9.5))
my_min(1, 3, -8, 9)
my_min(1)
my_min(1.1)
my_min()
my_min(1, 3, -8, 9, 9.8)

