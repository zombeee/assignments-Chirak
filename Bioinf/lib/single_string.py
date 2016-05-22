
"""
Contains:
- `acgt_content` - counter of atcg bases in sequence
- `dna_to_rna` - Converts DNA genetic code to RNA genetic code
- `revers_compliment` - Converts DNA string to revers complimented string
- `revers_compliment` - Converts DNA string to revers complimented string
- one associated constants
"""


from typing import List


GENETIC_ALPHOBET = {"A": "T",
                    "T": "A",
                    "C": "G",
                    "G": "C"
                    }
GEN_COD_DICT = {
    "UUU": "F",
    "UUC": "F",
    "UUA": "L",
    "UUG": "L",
    "CUU": "L",
    "CUC": "L",
    "CUA": "L",
    "CUG": "L",
    "AUU": "I",
    "AUC": "I",
    "AUA": "I",
    "AUG": "M",
    "GUU": "V",
    "GUC": "V",
    "GUA": "V",
    "GUG": "V",
    "UCU": "S",
    "UCC": "S",
    "UCA": "S",
    "UCG": "S",
    "CCU": "P",
    "CCC": "P",
    "CCA": "P",
    "CCG": "P",
    "ACU": "U",
    "ACC": "U",
    "ACA": "U",
    "ACG": "U",
    "GCU": "A",
    "GCC": "A",
    "GCA": "A",
    "GCG": "A",
    "UAU": "Y",
    "UAC": "Y",
    "CAU": "H",
    "CAC": "H",
    "CAA": "Q",
    "CAG": "Q",
    "AAU": "N",
    "AAC": "N",
    "AAA": "K",
    "AAG": "K",
    "GAU": "D",
    "GAC": "D",
    "GAA": "E",
    "GAG": "E",
    "UGU": "C",
    "UGC": "C",
    "UGG": "W",
    "CGU": "R",
    "CGC": "R",
    "CGA": "R",
    "CGG": "R",
    "AGU": "S",
    "AGC": "S",
    "AGA": "R",
    "AGG": "R",
    "GGU": "G",
    "GGC": "G",
    "GGA": "G",
    "GGG": "G",
    "UAA": None,
    "UAG": None,
    "UGA": None

}


def acgt_content(seq: str) -> List[int]:
    """
    Counts number of "A", "C", "G", "T", in string uppercase string
    :param seq: Uppercase string with DNA genetic code inside
    :return: List with number of "A", "C", "G", "T" letters respectively
    """
    return [seq.count("A"), seq.count("C"), seq.count("G"), seq.count("T")]


def dna_to_rna(dna_seq: str) -> str:
    """
    Converts DNA genetic code to RNA genetic code by replacing all "T" letters
    on "U" letters
    :param dna_seq: Uppercase string with DNA genetic code inside
    :return: Uppercase string with RNA genetic code inside
    """
    return "".join(list(base if base != "T" else "U" for base in dna_seq))


def revers_compliment(seq: str) -> str:
    """
    Converts DNA genetic code string to revers complimented string
    :param seq: Uppercase string with DNA genetic code inside
    :return: Revers complimented uppercase string with DNA genetic code inside
    """
    return "".join(list(GENETIC_ALPHOBET[base] for base in reversed(seq)))


def translator(sequence: str) -> str:
    """
    Translate RNA sequence to protein sequence
    :param sequence: Uppercase string with RNA genetic code inside
    :return: Uppercase string with protein amino acid code inside
    """
    triplet = []
    protein_seq = []
    for char in sequence:
        triplet.append(char)
        if len(triplet) == 3:
            protein_seq.append(GEN_COD_DICT["".join(triplet)])
            triplet = []
    return "".join(protein_seq)


def dna_motif(seq: str, subseq: str) -> List[int]:
    """

    :param seq:
    :param subseq:
    :return:
    """
    result = [0]
    for n in range(len(seq)):
        if seq.find(subseq) + 1:
            result.append(seq.find(subseq)+1)
        else:
            return result
    return result

dna_motif("atatatatat", "ata")