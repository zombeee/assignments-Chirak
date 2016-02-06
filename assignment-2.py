#! /usr/bin/env python


from __future__ import division, print_function


def my_max(*args):
    """
    This function try to find max, but still can't do it
    """
    work_args = list(args)
    if len(work_args) == 1:
        for seq in work_args:
            if isinstance(seq, list) or isinstance(seq, tuple):
                filtering_seq = list(seq)
                return (sorted(filtering_seq))[-1]
            else:
                raise ValueError("Can't find max, got only one value")
    else:
        for nums in work_args:
            if isinstance(nums, int):
                return (sorted(work_args))[-1]
            else:
                raise ValueError("Can't find max, wrong data format")


my_max([1, 3, -8, 9])
my_max((1, 3, -8, 9))
my_max(1, 3, -8, 9)
my_max(1)
my_max(0, 0, 0)
my_max(1, 3, -8, 9, True)
