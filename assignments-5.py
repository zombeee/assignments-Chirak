#! /usr/bin/env python


from __future__ import division, print_function
from itertools import imap

"""
Homework 5
"""


GAP_SYMBOL = "-"
DNA_ALPHABET = ("A", "T", "G", "C")
GEN_COD_DICT = {
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
    "TAA": None,
    "TAG": None,
    "TGA": None

}


def reconstruct_protein_alignment(*args):
    """
    'Greedy' translate aligned DNA sequence to aligned protein sequence
    :type args: str
    :param args: Aligned DNA sequences
    :return: Tuple of aligned protein sequences
    :raise ValueError: If given sequences have different length
    :raise ValueError: If length of the given sequences is not a multiple of
    three
    :raise ValueError If unexpected chars in DNA code founded
    :raise ValueError: If numbers of gaps is not a multiple of three
    """
    if len(set(imap(len, args))) != 1:
        raise ValueError("Given sequences have different length")
    if len(args[0]) % 3:
        raise ValueError("Length of the given sequences"
                         " is not a multiple of three")

    def translator(sequence):
        triplet = []
        gaps_stack = []
        protein_seq = []
        for char in sequence:
            if char in DNA_ALPHABET:
                triplet.append(char)
                if len(triplet) == 3:
                    if GEN_COD_DICT["".join(triplet)]:
                        protein_seq.append(GEN_COD_DICT["".join(triplet)])
                        triplet = []
                    else:
                        protein_seq.append(GAP_SYMBOL * ((len(sequence)//3) -
                                           len(protein_seq)))
                        break
            elif char == GAP_SYMBOL:
                gaps_stack.append(char)
                if len(gaps_stack) == 3:
                    protein_seq.append(GAP_SYMBOL)
                    gaps_stack = []
            else:
                raise ValueError("Unexpected chars in DNA code")
        if gaps_stack:
            raise ValueError("Numbers of gaps is not a multiple of three")
        return "".join(protein_seq)

    return tuple(translator(sequence) for sequence in args)


def main():
    reconstruct_protein_alignment("AAAGGGTTT", "AA-GGGT--",
                                  "TAAGGGTTT", "A-AGGGT--")


if __name__ == "__main__":
    main()



