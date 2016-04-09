#! /usr/bin/env python


from __future__ import print_function, division


def alignment(seq1, seq2):
    """
    This function aligns two sequences
    :type seq1: collections.Sequence
    :param seq1: eny sequence
    :type seq2: collections.Sequence
    :param seq2: eny sequence
    :return: Tuple with two aligned sequences
    :rtype: tuple(str)
    """
    #  note: Subtask matrix has one extra row and column for aligning with
    #  empty subsequences
    subtasks_matrix = [[0] * (len(seq1)+1) for _ in xrange(0, len(seq2)+1)]
    subtasks_matrix[0] = range(0, len(seq1)+1)  # initiation of first row
    for i in xrange(0, len(seq2)+1):
        subtasks_matrix[i][0] = i  # initiation of first colon
    solution_seq_1_reversed = []
    solution_seq_2_reversed = []
    for i in xrange(1, len(seq2)+1):
        for j in xrange(1, len(seq1)+1):
            subtasks_matrix[i][j] = min((subtasks_matrix[i-1][j-1] +
                                         (seq2[i-1] != seq1[j-1]),
                                         subtasks_matrix[i-1][j] + 1,
                                         subtasks_matrix[i][j-1] + 1))
    while i or j:
        if subtasks_matrix[i][j] == subtasks_matrix[i-1][j] + 1:
            solution_seq_1_reversed.append("-")
            solution_seq_2_reversed.append(seq2[i-1])
            i -= 1
        elif subtasks_matrix[i][j] == subtasks_matrix[i][j-1] + 1:
            solution_seq_1_reversed.append(seq1[j-1])
            solution_seq_2_reversed.append("-")
            j -= 1
        else:  # If we can't go to left or up we go diagonal
            solution_seq_1_reversed.append(seq1[j-1])
            solution_seq_2_reversed.append(seq2[i-1])
            i -= 1
            j -= 1
    return ("".join(reversed(solution_seq_1_reversed)),
            "".join(reversed(solution_seq_2_reversed)))  # reversing of solution


def alignment_test():
    first_seq = "agatacaca"
    second_seq = "cacaagata"
    alignment(first_seq, second_seq)


def main():
    alignment_test()


if __name__ == '__main__':
    main()