#! /usr/bin/env python


from __future__ import division, print_function


def my_max(*args):
    """
    This function find max in given sequence of simple numbers, or in
    given tuple or in list
    """

    if len(args) == 1:
        for seq in args:
            if isinstance(seq, (list, tuple)):
                return sorted(seq)[-1]
    elif len(args) == 0:
        raise ValueError("Can't find max, no data given")
    else:
        for num in args:
            if isinstance(num, int):
                return sorted(args)[-1]
            else:
                raise ValueError("Can't find max, wrong data format")


my_max([1, 3, -8, 9])
my_max((1, 3, -8, 9))
my_max(1, 3, -8, 9)
my_max(1)
my_max()
# this don't work
my_max(1, 3, -8, 9, 9.8)
# this works
my_max(0.95, 1, 3, -8, 9, 9.8)
