#!/usr/bin/python
import sys

def reverse_complement(sequence):
    reverse_complement = []
    complement = {'A': 'T', 'G': 'C', 'C':'G', 'T': 'A'}
    sequence = sequence.upper()
    seqbases = list(sequence)
    reverse_seqbases = seqbases[::-1]
    for s in reverse_seqbases:
        reverse_complement.append(complement.get(s))
    return "".join(reverse_complement)

def dice_string(string):
    return (string, string[:len(string)-1], string[1:])
    
def build_debruijn_graph(graph, line):
    forward_kmers = dice_string(line)
    prefix = forward_kmers[1]
    suffix = forward_kmers[2]
    if prefix in graph:
        graph[prefix].append(suffix)
    else:
        graph[prefix]=[suffix]
    return graph

# read the file
graph = {}
filepath = sys.argv[1]
f_kmers = set()
r_kmers = set()
for line in open(filepath):
    line = line.strip()
    rline = reverse_complement(line)
    f_kmers.add(line)
    r_kmers.add(rline)

# build graph
kmers = f_kmers.union(r_kmers)
for k in kmers:
    graph = build_debruijn_graph(graph, k)

#print(graph)
# get adjacency matrix
for key in graph:
#    print (key+" ->",",".join(graph[key]))
    for value in graph[key]:
        print("("+key+",",value+")")

