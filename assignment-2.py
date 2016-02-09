#! /usr/bin/env python


"""
Homework 1
"""

from __future__ import division, print_function


def my_max(*args):
    """
    This function find max in given sequence of simple numbers, or in
    given tuple or in list
    """
    def sorter(sequence):
        """
        This function find max in given sequence of simple numbers
        """
        def bubble_sort(a):
            """
            This function sort the list
            """
            for i in reversed(range(len(a))):
                for j in range(1, i + 1):
                    if a[j-1] > a[j]:
                        a[j], a[j-1] = a[j-1], a[j]
            return a

        listed_seq = list(sequence)
        for number in listed_seq:
            if not isinstance(number, int):
                raise ValueError("Can't find max, wrong data format")
        return bubble_sort(listed_seq)[-1]

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


my_max([1, 3, -11, -8, 9, 1])
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
        This function find max in given sequence of simple numbers
        """
        def bubble_sort(a):
            """
            This function sort the list
            """
            for i in reversed(range(len(a))):
                for j in range(1, i + 1):
                    if a[j-1] > a[j]:
                        a[j], a[j-1] = a[j-1], a[j]
            return a

        listed_seq = list(sequence)
        for number in listed_seq:
            if not isinstance(number, int):
                raise ValueError("Can't find max, wrong data format")
            return bubble_sort(listed_seq)[0]

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
my_min(7, 3, -8, 9, 9.8)

