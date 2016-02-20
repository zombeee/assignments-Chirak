#! /usr/bin/env python

"""
Homework 3
"""

from __future__ import print_function, division
import sys
import os


def my_fasta_reader(fp):
    """
    This function is fasta reader
    :type fp: str
    :param fp: path to fasta file
    :return: list of pared names and sequences
    """
    with open(fp) as input_file:
        COMMENT_START_SYMBOL = "#"
        NEW_SEQ_NAME_START_SYMBOL = ">"
        stack_for_seq = []
        merging_seq_list = []
        for line in input_file:
            if line.startswith(COMMENT_START_SYMBOL):
                continue
            elif line.startswith(NEW_SEQ_NAME_START_SYMBOL):
                if stack_for_seq:
                    stack_for_seq.append("".join(merging_seq_list))
                    merging_seq_list = []
                    yield tuple(stack_for_seq)
                    stack_for_seq = []
                stack_for_seq.append(line.strip("> \n"))
            else:
                merging_seq_list.append(line.strip())
        stack_for_seq.append("".join(merging_seq_list))
        yield tuple(stack_for_seq)


def main():
    file_path = os.path.abspath(sys.argv[1])
    my_fasta_reader(file_path)
    my_fasta_reader("/home/chirak/test.fasta")


if __name__ == "__main__":
    main()
