#!/usr/bin/python
import random
from Bio import SeqIO
import sys

def create_matrix(i,j):
    d = []
    for row in range(0,i):
        temp = []
        for col in range(0,j):
            temp.append(None)
        d.append(temp)
        
    return(d)

def levenshtein_formula(d,i, j, v,w):
    gap1 = d[i-1][j] + 1
    gap2 = d[i][j-1] + 1

    if str(v) == str(w):
        match_mismatch = d[i-1][j-1] 
    else:
        match_mismatch = d[i-1][j-1] + 1
    d[i][j] = min([gap1, gap2, match_mismatch])
    #print([gap1, gap2, match_mismatch])
    #print([d[i-1][j], d[i-1][j-1], d[i][j-1]])
    return d
    
def editDistance(x,y):
    ilen = len(x)
    jlen = len(y)

    d = create_matrix(ilen+1,jlen+1)

    ## initialize
    for i in range(0, len(d)):
        for j in range(0, len(d[i])):
            d[i][0] = i
            d[0][j] = j
    x= '#'+x
    y= '#'+y
    d[0][0]=0

#    print(d)
#    print(d)
#    for i in range(0, len(d)):
#        for j in range(0, len(d[i])):
#            print(i, j, d[i][j],x[i],y[j])
#
#    print('%'*5)

    for i in range(1, len(d)):
        for j in range(1, len(d[i])):
#            print(d,i, j, x[i],y[j])
            d = levenshtein_formula(d,i, j, x[i],y[j])
#            print(d)
    print(d)
    return(d[i][j])


records = list(SeqIO.parse(sys.argv[1], "fasta"))
x= (records[0].seq)  # first record
y = (records[-1].seq)  # last record
print(editDistance(x,y))
