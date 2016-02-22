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


def p_dist(seq1, seq2):
    """
    :type seq1: str
    :param seq1:
    :type seq2: str
    :param seq2:
    :return:
    """
    if len(seq1) != len(seq2):
        raise ValueError("Different length of the sequences")
    return (sum(a != b for a, b in izip(seq1, seq2) if (a != "-" or b != "-"))
/ sum(a for a, b in izip(seq1, seq2) if (a != "-" or b != "-")))


def matrix_dot_product(matrix1, matrix2):
    """
    :type matrix1: list
    :param matrix1:
    :type matrix2: list
    :param matrix2:
    :return:
    """
    if not matrix1 or not matrix2:
        raise ValueError("Empty matrix given")
    n_row_1, n_col_1 = len(matrix1), len(matrix1[0])
    n_row_2, n_col_2 = len(matrix2), len(matrix2[0])
    if n_row_2 != n_col_1:
        raise ValueError("Numbers of rows in first matrix must be equal"
                         " to numbers of colons in second matrix")
    result_matrix = []
    for row in matrix1:
        result_matrix.append([sum(starmap(operator.mul, zip(row, column)))
                              for column in zip(*matrix2)])
    return result_matrix


matrix_1 = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
matrix_2 = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

matrix_dot_product(matrix_1, matrix_2)





