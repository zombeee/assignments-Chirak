#! /usr/bin/env python


from __future__ import print_function, division


def longest_nonincreasing_subseq_len_sqr(sequence):
    """
    This script search longest non increasing sub sequence in sequence
    :type sequence: collections.Sequence[int]
    :param sequence: sequence of integer numbers
    :return: list with sub sequence insight
    :rtype list
    """
    best_subtask = [1] * len(sequence)
    solution_reversed = []
    solution = []  # Necessary because first solution applied in reverse order
    for i in xrange(1, len(sequence)):
        for j in xrange(0, i):
            if sequence[i] <= sequence[j]:
                best_subtask[i] = max(best_subtask[j]+1, best_subtask[i])
    last_member = max(best_subtask)

    for numbers in reversed(zip(sequence, best_subtask)):  # numbers
        # is tuple where first element is element of input sequence
        # and the second element is length of best subtask for this element
        if numbers[1] == last_member:
            if not solution_reversed:
                solution_reversed.append(numbers[0])
            if numbers[0] >= solution_reversed[-1]:
                solution_reversed.append(numbers[0])
                last_member -= 1
                if last_member == 0:  # we find best subseq
                    break  # and we need to stop iteration
    solution.extend(reversed(solution_reversed))  # reversing of solution
    return solution


def test_sqr_subseq():
    x = [10, 8, 9, 9, 8, 7, 15, 14, 12, 5, 4, 3, 8, 7, 6, 3, 2, 1, 25, 35]
    longest_nonincreasing_subseq_len_sqr(x)


def longest_common_subsequence(seq1, seq2):
    """
    This function search longest common sub sequence in two sequences
    :type seq1: collections.Sequence
    :param seq1: eny sequence
    :type seq2: collections.Sequence
    :param seq2: eny sequence
    :return: List with elements of longest common sub sequence insight
    :rtype: list
    """
    #  note: Subtask matrix has one extra row and column for empty subsequences
    subtasks_matrix = [[0] * (len(seq1)+1) for _ in xrange(0, len(seq2)+1)]
    solution_backward = []
    solution = []
    for i in xrange(1, len(seq2)+1):
        for j in xrange(1, len(seq1)+1):
            subtasks_matrix[i][j] = (subtasks_matrix[i-1][j-1] + 1
                                     if seq2[i-1] == seq1[j-1] else
                                     max(subtasks_matrix[i-1][j],
                                         subtasks_matrix[i][j-1]))
    while i and j:
        if subtasks_matrix[i-1][j] == subtasks_matrix[i][j]:
            i -= 1
        elif subtasks_matrix[i][j-1] == subtasks_matrix[i][j]:
            j -= 1
        else:  # If we can't go to left or up we go diagonal
            i -= 1
            j -= 1
            solution_backward.append(seq2[i])
    solution.extend(reversed(solution_backward))  # reversing of solution
    return solution


def test_common_subseq():
    first_seq = "agatacaca"
    second_seq = "cacaagata"
    longest_common_subsequence(first_seq, second_seq)

    # while i and j:
    #     i, j = (next((i_, j_) for i_, j_ in ((i-1, j), (i, j-1))) if
    #             subtasks_matrix[i][j] == subtasks_matrix[i_][j_] else (i-1,
    #                                                                    j-1))
    #   solution_backward.append(seq2[i-1])
    # This is my best Idea


def main():
    test_sqr_subseq()
    test_common_subseq()


if __name__ == '__main__':
    main()



