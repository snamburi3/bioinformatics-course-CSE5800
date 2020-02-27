#!/usr/bin/python
"""
The d-neighborhood Neighbors(Pattern, d) is the set of all k-mers whose Hamming distance from Pattern does not exceed d.

Generate the d-Neighborhood of a String
Find all the neighbors of a pattern.

Given: A DNA string Pattern and an integer d.

Return: The collection of strings Neighbors(Pattern, d).
"""

import sys

def check_sequence(seq):
    nucleotides = ['A', 'T', 'C', 'G']
    for s in seq:
        assert s in nucleotides, "invalid nucleotide " + s + " in the genome sequence"
    return (True)

def single_position_mutation(dna, position):
    nucleotides = ['A', 'T', 'C', 'G']
    dna_patterns = {}
    dna_list = list(dna)
    elem = dna_list[position]

    # remove the nucleotide that is present
    iter_nucleotides = nucleotides.copy()
    iter_nucleotides.remove(elem)

    for nuc in iter_nucleotides:
        dna_list[position] = str(nuc) # replace the nuc 
        changed_dna = dna_list.copy()
        dna_patterns["".join(changed_dna)] = 1
    return (dna_patterns)

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

if __name__ == "__main__":
    fh = open(sys.argv[1], 'r')
    #input_string = fh.readline().strip()
    dna_pattern = fh.readline().strip()
    target_d = int(fh.readline().strip())
    assert len(dna_pattern) >= 0,"empty dna string pattern"
    #assert str(input_string) == 'Input',"this has to be 'Input' - check dataset"
    assert check_sequence(dna_pattern) == True
    assert isinstance(target_d, int) == True, 'D must be integer' 

    for key in generate_d_neighborhood(dna_pattern, target_d):
        print(key)
