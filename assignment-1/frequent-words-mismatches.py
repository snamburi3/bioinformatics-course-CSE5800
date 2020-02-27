#!/usr/bin/python

"""
Frequent Words with Mismatches and Reverse Complements Problem
Find the most frequent k-mers (with mismatches and reverse complements) in a DNA string.

Given: A DNA string Text as well as integers k and d.

Return: All k-mers Pattern maximizing the sum Countd(Text, Pattern) + Countd(Text, Pattern) over all possible k-mers.

"""
import sys

def check_sequence(seq):
    nucleotides = ['A', 'T', 'C', 'G']
    for s in seq:
        assert s in nucleotides, "invalid nucleotide " + s + " in the genome sequence"
    return (True)


def reverse_complement(sequence):
    reverse_complement = []
    complement = {'A': 'T', 'G': 'C', 'C':'G', 'T': 'A'}
    sequence = sequence.upper()
    seqbases = list(sequence)
    reverse_seqbases = seqbases[::-1]
    for s in reverse_seqbases:
        reverse_complement.append(complement.get(s))
    return "".join(reverse_complement)

def single_position_mutation(dna, position):

    nucleotides = ['A', 'T', 'C', 'G']
    dna_strings = {}
    dna_list = list(dna)
    elem = dna_list[position]

    iter_nucleotides = nucleotides.copy()
    iter_nucleotides.remove(elem)

    for nuc in iter_nucleotides:
        dna_list[position] = str(nuc)
        changed_dna = dna_list.copy()
        dna_strings["".join(changed_dna)] = 1
    return (dna_strings)

def generate_one_neighborhood(dna_pattern, position=0):
    all_patterns = {}
    for i in range(position, len(dna_pattern)):
        all_patterns.update(single_position_mutation(dna_pattern, i))
    return(all_patterns)

def generate_d_neighborhood(dna_pattern, target_d):
    patterns = {}
    for d in range(target_d):
        temp_patterns = {}
        if d == 0:
            patterns.update(generate_one_neighborhood(dna_pattern, d))
        else:
            for key, value in patterns.items():
                temp_patterns.update(generate_one_neighborhood(key, d))
        patterns.update(temp_patterns)
    return (patterns)

def get_dict_keys_max_value(myList):
    maxKey = max(myList, key=myList.get)
    myKeys = list()
    # Iterate over all the items in dictionary to find keys with max value
    for key, value in myList.items():
        if value == myList[maxKey]:
            myKeys.append(key)
    return (myKeys)

def get_frequent_words(dna_string, kmers_length, d_mismatches):
    all_substrings = {}
    for i in range(0,len(dna_string)):
        dna_substr = dna_string[i:i+kmers_length]
        if len(dna_substr) < kmers_length:
            continue

        if not dna_substr in all_substrings:
            all_substrings[dna_substr] = 1
        else:
            all_substrings[dna_substr] += 1

        for pattern in generate_d_neighborhood(dna_substr, d_mismatches):
                if not pattern in all_substrings:
                    all_substrings[pattern] = 1 
                else:
                    all_substrings[pattern] += 1


    return (all_substrings)

if __name__ == "__main__":
    fh = open(sys.argv[1], 'r')

#    input_string = fh.readline().strip()
    dna_string = fh.readline().strip()
    input_args = fh.readline().strip().split()
    kmers_length = int(input_args[0])
    d_mismatches = int(input_args[1])
    
    assert len(dna_string) >= 0,"empty dna string pattern"
#    assert str(input_string) == 'Input',"this has to be 'Input' - check dataset"
    assert check_sequence(dna_string) == True
    assert isinstance(kmers_length, int) == True, 'kmer length must be integer'
    assert isinstance(d_mismatches, int) == True, 'D mismatches must be integer'

    # forward strand
    all_forward_kmers = get_frequent_words(dna_string, kmers_length, d_mismatches)

    # reverse strand
    all_reverse_kmers = get_frequent_words(reverse_complement(dna_string), kmers_length, d_mismatches)

    # Sum Countd(Text, Pattern) + Countd(Text, Pattern) 
    for key,val in all_reverse_kmers.items():
        if not key in all_forward_kmers:
            all_forward_kmers[key] = val
        else:
            all_forward_kmers[key] += val

    print(get_dict_keys_max_value(all_forward_kmers))

