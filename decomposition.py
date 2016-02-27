#! /usr/bin/env python


from __future__ import division, print_function


"""
This module decompose given number on maximum number of different summands
"""

decomp_result = []


def decompose(n):
    """
    :type n: int
    :param n: Eny integer number
    :return: Sorted list of maximum number of different
    summands of the given number
    """
    if n == 4:
        decomp_result.append(1)
        decomp_result.append(3)
        return decomp_result
    if n == 2:
        decomp_result.append(2)
        return decomp_result
    if n == 1:
        decomp_result.append(1)
        return decomp_result
    if n % 2:
        decomp_result.append((n//2+1))
    else:
        decomp_result.append(n//2)
    decompose(n//2)
    return sorted(decomp_result)


def main():
    input_number = raw_input("Input: ")
    if not input_number.isdigit():
        raise ValueError("Not integer given")
    if (input_number < 1) and (input_number > 10**9):
        raise ValueError("Given number out of expected range")
    decompose(int(input_number))
    print("Output:", *decomp_result)


if __name__ == "__main__":
    main()
