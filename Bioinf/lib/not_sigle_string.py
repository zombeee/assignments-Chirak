

"""
Contains:
- `highest_gc_content` - Find sequence with highest GC content
-
- several associated constants
"""


from typing import Generator, Tuple
import operator as op

ENTRY_START_CHAR = ">"
COMMENT_START_CHAR = "#"
CHAR_STRIP = "> \n"


def highest_gc_content(file: list) -> Tuple[str, float]:
    """
    Find sequence with highest GC content in fasta file
    :param file: List with sequence in fasta format in strings
    :return: Tuple of form (sequence name, GC content)
    """

    def gc_counter(_file: list) -> Generator:
        """
        Counts GC content in sequence
        :param _file:List with sequence in fasta format in strings
        :return: a generator of entries, yielding tuples of form
        (sequence name, GC content)
        """

        def fasta_reader(__file: list) -> Generator:
            """
            Read fasta file from fp and returns tuples with label and sequence
            :param __file: List with sequence in fasta format in strings
            :return: a generator of entries, yielding tuples of form
            (label, sequence)
            """
            # note: `sequence_stack` is meant to contain 2 items:
            #       1. label of a sequence (a string)
            #       2. parts of a sequence (a list of strings)
            sequence_stack = []
            # Iterate over nonempty lines
            for line in (l for l in __file if l.strip()):
                if line.startswith(ENTRY_START_CHAR) and sequence_stack:
                    # we've found a new entry and it's not the first entry,
                    # hence `sequence_stack` is not empty, hence we must
                    # unload the previous record
                    yield sequence_stack[0], "".join(sequence_stack[1])
                    sequence_stack = [line.strip(CHAR_STRIP), []]
                elif line.startswith(ENTRY_START_CHAR):
                    # we reached the first entry, that is `sequence_stack`
                    # is empty at the moment
                    sequence_stack = [line.strip(CHAR_STRIP), []]
                elif not line.startswith(COMMENT_START_CHAR):
                    # the line is not a comment, hence it must contain
                    # a part of a sequence
                    sequence_stack[1].append(line.strip(CHAR_STRIP))
            yield sequence_stack[0], "".join(sequence_stack[1])

        for _pair in  fasta_reader(_file):
            yield (_pair[0], round((((_pair[1].count("C")+_pair[1].count("G"))/
                                     len(_pair[1]))*100), 6))

    return max(list(gc_counter(file)), key=op.itemgetter(1))


def hamming(seq1: str, seq2: str) -> int:
    """
    Counts Hamming distance for two sequences
    :param seq1: DNA sequence
    :param seq2: DNA sequence
    :return: Hamming distance
    """
    if len(seq1) != len(seq2):
        raise ValueError("Different length of the sequences")
    return sum(a != b for a, b in zip(seq1, seq2))


