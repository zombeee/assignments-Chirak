#! /usr/bin/env python


from __future__ import division, print_function


def my_max(*args):
    """
    This function try to find max, but still can't do it
    """
    if len(args) == 1:
        for seq in args:
            if isinstance(seq, (list, tuple)):
                return (sorted(seq))[-1]
        else:
            for nums in args:
                if isinstance(nums, int):
                    return (sorted(args))[-1]
                else:
                    raise ValueError("Can't find max, wrong data format")


my_max([1, 3, -8, 9])
my_max((1, 3, -8, 9))
my_max(1, 3, -8, 9)
my_max(1)
my_max()
my_max(1, 3, -8, 9, True)
