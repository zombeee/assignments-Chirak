#! /usr/bin/env python


from __future__ import division, print_function


"""
This module decompose given number on maximum number of different summands
"""


def decompose(n):
    """
    :type n: int
    :param n: Eny integer number
    :return: Sorted list of maximum number of different
    summands of the given number
    """
    decomp_result = []
    num = n
    while num:
        if num == 4:
            decomp_result.append(1)
            decomp_result.append(3)
            return sorted(decomp_result)
        if num == 2:
            decomp_result.append(2)
            return sorted(decomp_result)
        if num == 1:
            decomp_result.append(1)
            return sorted(decomp_result)
        if num % 2:
            decomp_result.append(num//2+1)
            num //= 2
        else:
            decomp_result.append(num//2)
            num //= 2
    return sorted(decomp_result)


def main():
    input_number = raw_input("Input: ")
    if not input_number.isdigit():
        raise ValueError("Not integer given")
    if (int(input_number) < 1) or (int(input_number) > 10**9):
        raise ValueError("Given number out of expected range")
    print("Output:", *decompose(int(input_number)))


if __name__ == "__main__":
    main()
