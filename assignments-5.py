#! /usr/bin/env python


from __future__ import division, print_function
from itertools import izip, imap

"""
Homework 5
"""


CHARS_OF_THE_GENE_CODE = ["A", "T", "G", "C"]
STOP_CODONS = ["TAA", "TAG", "TGA"]
GENETIC_CODE_DICT = {
    "TTT": "F",
    "TTC": "F",
    "TTA": "L",
    "TTG": "L",
    "CTT": "L",
    "CTC": "L",
    "CTA": "L",
    "CTG": "L",
    "ATT": "I",
    "ATC": "I",
    "ATA": "I",
    "ATG": "M",
    "GTT": "V",
    "GTC": "V",
    "GTA": "V",
    "GTG": "V",
    "TCT": "S",
    "TCC": "S",
    "TCA": "S",
    "TCG": "S",
    "CCT": "P",
    "CCC": "P",
    "CCA": "P",
    "CCG": "P",
    "ACT": "U",
    "ACC": "U",
    "ACA": "U",
    "ACG": "U",
    "GCT": "A",
    "GCC": "A",
    "GCA": "A",
    "GCG": "A",
    "TAT": "Y",
    "TAC": "Y",
    "CAT": "H",
    "CAC": "H",
    "CAA": "Q",
    "CAG": "Q",
    "AAT": "N",
    "AAC": "N",
    "AAA": "K",
    "AAG": "K",
    "GAT": "D",
    "GAC": "D",
    "GAA": "E",
    "GAG": "E",
    "TGT": "C",
    "TGC": "C",
    "TGG": "W",
    "CGT": "R",
    "CGC": "R",
    "CGA": "R",
    "CGG": "R",
    "AGT": "S",
    "AGC": "S",
    "AGA": "R",
    "AGG": "R",
    "GGT": "G",
    "GGC": "G",
    "GGA": "G",
    "GGG": "G",

}


def reconstruct_protein_alignment(*args):
    if len(set(imap(len, args))) != 1:
        raise ValueError("Given sequences have different length")
    if len(args[0]) % 3:
        raise ValueError("Length of the given sequences"
                         " is not a multiple of three ")
    triplet = []
    gaps_stack = []
    protein_seq = []
    result_protein_sequences = []
    for sequence in args:
        for char in sequence:
            if char in CHARS_OF_THE_GENE_CODE:
                triplet.append(char)
                if len(triplet) == 3:
                    if "".join(triplet) in STOP_CODONS:
                        protein_seq.append("-" * ((len(sequence)//3) -
                                           len(protein_seq)))
                        triplet = []
                        break
                    protein_seq.append(GENETIC_CODE_DICT["".join(triplet)])
                    triplet = []
            else:
                gaps_stack.append("-")
                if len(gaps_stack) == 3:
                    protein_seq.append("-")
                    gaps_stack = []
        result_protein_sequences.append("".join(protein_seq))
        protein_seq = []
    return tuple(result_protein_sequences)


def main():
    reconstruct_protein_alignment("AAAGGGTTT", "AA-GGGT--", "TAAGGGTTT", "AAAGGGTTT")


if __name__ == "__main__"
    main()



