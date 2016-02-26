#! /usr/bin/env python


"""

"""


from __future__ import division, print_function
from itertools import ifilter, izip, imap, starmap
import operator


def hamming(seq1, seq2):
    """
    :type seq1: str
    :param seq1:
    :type seq2: str
    :param seq2:
    :return:
    """
    if len(seq1) != len(seq2):
        raise ValueError("Different length of the sequences")
    return sum(a != b for a, b in izip(seq1, seq2))


def p_distance(seq1, seq2):
    """
    :type seq1: str
    :param seq1:
    :type seq2: str
    :param seq2:
    :return:
    """
    if len(seq1) != len(seq2):
        raise ValueError("Different length of the sequences")
    return (sum(a != b for a, b in izip(seq1, seq2) if (a != "-" and b != "-"))
/ sum(bool(a) for a, b in izip(seq1, seq2) if (a != "-" and b != "-")))


def matrix_product(a, b):
    """
    :type a: list
    :param a:
    :type b: list
    :param b:
    :return:
    """
    if not a or not b:
        raise ValueError("Empty matrix given")
    n_row_1, n_col_1 = len(a), len(a[0])
    n_row_2, n_col_2 = len(b), len(b[0])
    if n_row_2 != n_col_1:
        raise ValueError("Numbers of rows in first matrix must be equal"
                         " to numbers of colons in second matrix")
    result_matrix = []
    for row in a:
        result_matrix.append([sum(starmap(operator.mul, zip(row, column)))
                              for column in zip(*b)])
    return result_matrix


matrix_1 = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
matrix_2 = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

matrix_product(matrix_1, matrix_2)


GAP = "-"

def new_p_dist(seq1, seq2):
    """

    :param seq1:
    :param seq2:
    :return:
    """
    if len(seq1) != len(seq2):
        raise ValueError("Different size of given sequences")
    if not seq1:
        raise ValueError("Empty sequence given")
    def no_gap(a, b):
        return a != GAP and b != GAP
    mismatches = sum(a != b for a, b in izip(seq1, seq2) if no_gap(a, b))
    gapless_length = sum(no_gap(a, b) for a, b in izip(seq1, seq2)
    return mismatches/gapless_length


def main():
    p_distance("aaaggggtttt", "aaaggcctt-t")
if __name__ == "__main__":
    pass
