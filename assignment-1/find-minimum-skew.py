#!/usr/bin/python

"""
Define the skew of a DNA string Genome, denoted Skew(Genome), as the difference between the total number of occurrences of 'G' and 'C' in Genome. Let Prefixi (Genome) denote the prefix (i.e., initial substring) of Genome of length i. For example, the values of Skew(Prefixi ("CATGGGCATCGGCCATACGCC")) are:

0 -1 -1 -1 0 1 2 1 1 1 0 1 2 1 0 0 0 0 -1 0 -1 -2

Minimum Skew Problem
Find a position in a genome minimizing the skew.

Given: A DNA string Genome.

Return: All integer(s) i minimizing Skew(Prefixi (Text)) over all values of i (from 0 to |Genome|).
"""
import sys

def check_sequence(seq):
    nucleotides = ['A', 'T', 'C', 'G']
    for s in seq:
        assert s in nucleotides, "invalid nucleotide " + s + " in the genome sequence"
    return (True)

def minimize_genome_skew(dna_string):
    reward = 1
    penality = -1
    skew_list = [0]
    min_skew = skew_list[0]
    output_indexes = []
    for idx,nuc in enumerate(dna_string):
        if nuc == 'C': # find c, penality
            skew_list.append(skew_list[-1] + penality)
        elif nuc == 'G': # find G, reward
            skew_list.append(skew_list[-1] + reward)
        else:
            skew_list.append(skew_list[-1])

        # genome skew(g-c) = abs(skew_list[-1])

        if skew_list[-1] < min_skew:
            output_indexes = []
            output_indexes.append(idx + 1) 
            min_skew = skew_list[-1]
        elif skew_list[-1] == min_skew:   
            output_indexes.append(idx + 1)
            min_skew = skew_list[-1]
    
    return (output_indexes)

if __name__ == "__main__":
    fh = open(sys.argv[1], 'r') 
    #input_string = fh.readline().strip() 
    dna_string = fh.readline().strip()
    assert len(dna_string) >= 0,"empty dna string pattern"
    assert str(input_string) == 'Input',"this has to be 'Input' - check dataset"
    assert check_sequence(dna_string) == True

    print(minimize_genome_skew(dna_string))
