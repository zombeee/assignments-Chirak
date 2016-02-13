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
    :param fp: path to fasta file
    :return: list of pared names and sequences
    """
    with open(fp) as input_file:
        comment_start_symbol = "#"
        new_seq_name_symbol = ">"
        stack_for_seq = []
        merging_seq_list = []
        for line in input_file:
            if line.startswith(comment_start_symbol):
                continue
            if line.startswith(new_seq_name_symbol):
                if stack_for_seq:
                    stack_for_seq.append("".join(merging_seq_list))
                    merging_seq_list = []
                    yield tuple(stack_for_seq)
                    stack_for_seq = []
                stack_for_seq.append(line.strip(">, \n"))
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
