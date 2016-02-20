#! /usr/bin/env python


"""

"""


from __future__ import division, print_function
from itertools import ifilter, izip, imap

def hamming(seq1, seq2):
    """
    :type seq1: str
    :param seq1:
    :type seq2: str
    :param seq2:
    :return:
    """
    if len(seq1) != len(seq2):
        raise ValueError("Different lenght of the sequences")
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
        raise ValueError("Different lenght of the sequences")
    return ((sum(a != b for a, b in izip(seq1, seq2) if a != "-" or b != "-"))
/(sum(a for a, b in izip(seq1, seq2) if a != "-" or b != "-")))


def matrix_dot_prodact(matrix1, matrix2):
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
        raise ValueError("Errors in given data")
    mult_matrix_result = [[None for j in xrange(n_col_2)]
                          for i in xrange(n_row_1)]
    for i in mult_matrix_result:
        i.append(sum((j for numbers in lines for i in matrix1)*
                     (num for row[j] in matrix2)))





