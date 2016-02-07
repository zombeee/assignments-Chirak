#! /usr/bin/env python


from __future__ import division, print_function


def my_max(*args):
    """
    This function find max in given sequence of simple numbers, or in
    given tuple or in list
    """

    if len(args) == 1:
        numbers = args[0]
        if isinstance(numbers, (list, tuple)):
            return sorted(numbers)[-1]
    elif not args:
        raise ValueError("Can't find max, no data given")
    else:
        for num in args:
            test_val = 0
            if not isinstance(num, int) > test_val:
                test_val = not isinstance(num, int)
                if test_val == 1:
                    raise ValueError("Can't find max, wrong data format")
                else:
                    return sorted(args)[-1]




my_max([1, 3, -8, 9])
my_max((1, 3, -8, 9))
my_max(1, 3, -8, 9)
my_max(1)
my_max()
# this don't work
my_max(1, 3, -8, 9, 9.8)
# this works
my_max(0.95, 1, 3, -8, 9, 9.8)
