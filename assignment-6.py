#! /usr/bin/env python


from __future__ import print_function, division
import itertools
import collections
import random


def merge(a, b):
    """
    :type a: list
    :param a: sorted list
    :type b: list
    :param b: sorted list
    :return: one sorted list
    """
    i, j = 0, 0
    one_sorted_list = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            one_sorted_list.append(a[i])
            i += 1
        else:
            one_sorted_list.append(b[j])
            j += 1
    if i == len(a):
        one_sorted_list.extend(itertools.islice(b, j, len(b)))
    else:
        one_sorted_list.extend(itertools.islice(a, i, len(a)))
    return one_sorted_list


def merge_recursive(sequence):
    first_part = sequence[len(sequence) // 2:]
    second_part = sequence[:len(sequence) // 2]

    def merge_(a, b):
        if len(a) <= 1 and len(b) <= 1:
            return merge(a, b)
        return merge(merge_(a[:len(a) // 2], a[len(a) // 2:]),
                     merge_(b[:len(b) // 2], b[len(b) // 2:]))

    return merge_(first_part, second_part)


def merge_sort_iterative(sequence):
    split = collections.deque([item] for item in sequence)
    while len(split) not in (1, 0):
        split.append(merge(split.popleft(), split.popleft()))
    return split.pop() if split else []


def test_merge_recursive():
    unsorted_list = [random.randint(1, 1000) for _ in xrange(1, 51)]
    return merge_recursive(unsorted_list) == sorted(unsorted_list)


def main():
    if not test_merge_recursive():
        raise RuntimeError("all_bad")


if __name__ == '__main__':
    main()
