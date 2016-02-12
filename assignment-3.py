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
        names_list = []
        seqs_list = []
        mergin_seq_list = []
        for line in input_file:
            if line.startswith("#"):
                continue
            if line.startswith(">"):
                names_list.append(line.strip(">, \n"))
                if mergin_seq_list:
                    seqs_list.append("".join(mergin_seq_list))
                    mergin_seq_list = []
            else:
                mergin_seq_list.append(line.strip())
        if mergin_seq_list:
            seqs_list.append("".join(mergin_seq_list))
    return zip(names_list, seqs_list)


def main():
    file_path = os.path.abspath(sys.argv[1])
    my_fasta_reader(file_path)


if __name__ == "__main__":
    main()
