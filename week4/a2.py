def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """

    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return len(dna1) > len(dna2)


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    num_nucleotides = 0
    for char in dna:
	    if char in nucleotide:
		    num_nucleotides = num_nucleotides + 1
    return num_nucleotides


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return dna2 in dna1


def is_valid_sequence(dna):
    """ (str) -> bool

    Return True if and only if the DNA sequence is valid (i.e. contains no characters other than 'A', 'T', 'C', 'G'.

    >>> is_valid_sequence('ATTCG')
    True
    >>> is_valid_sequence('ABCG')
    False
    """
    valid = True
    for char in dna:
        if not char in 'ATCG':
            valid = False
    return valid


def is_valid_sequence(dna):
    """ (str) -> bool

    Return True if and only if the DNA sequence is valid (i.e. contains no characters other than 'A', 'T', 'C', 'G'.

    >>> is_valid_sequence('ATTCG')
    True
    >>> is_valid_sequence('ABCG')
    False
    """
    valid = True
    for char in dna:
        if not char in 'ATCG':
            valid = False
    return valid


def insert_sequence(dna1, dna2, index):
    """ (str, str, int) -> str

    Return the DNA sequence obtained by inserting the second DNA sequence into the first DNA sequence at the given index.

    >>> insert_sequence('ATCG', 'ATCG', 2)
    'ATATCGCG'
    
    >>> insert_sequence('ATCG', 'ATCG', -1)
    'ATCATCGG'
    """
    new_sequence = dna1[:index] + dna2[:] + dna1[index:]
    return new_sequence


def get_complement(nucleotide):
    """ (str) -> str

    Return the nucleotide's complement. (i.e. A complements T, C complements G, and vice versa).

    >>> get_complement('A')
    'T'
    >>> get_complement('G')
    'C'
    """
    if nucleotide in 'A':
        print ('T') 
    elif nucleotide in 'T':
        print ('A')
    elif nucleotide in 'C':
        print ('G')
    elif nucleotide in 'G':
        print ('C')


def get_complementary_sequence(dna):
    """ (str) -> str
    Return the complementary nucleotides for the DNA sequence. (i.e. A complements T, C complements G, and vice versa).
    >>> get_complementary_sequence('ATCG')
    'TAGC'
    >>> get_complementary_sequence('GCTA')
    'CGAT'
    """
    new_sequence = ''
    for char in dna:
        if char in 'A':
            new_sequence = new_sequence + 'T'
        if char in 'T':
            new_sequence = new_sequence + 'A'
        if char in 'C':
            new_sequence = new_sequence + 'G'
        if char in 'G':
            new_sequence = new_sequence + 'C'
        return new_sequence
