#!/usr/bin/python
import random
from Bio import SeqIO
import sys
import numpy 
from operator import itemgetter 
import operator

def create_matrix(i,j):
    d = []
    for row in range(0,i):
        temp = []
        for col in range(0,j):
            temp.append(None)
        d.append(temp)

    return(d)


def semiglobal(d, bt_d, i, j, v,w):
    """
    d - the main matrix
    bt_d - the backtracking matrix
    i - the position to compute (x)
    j - the position to compute (y)
    v - the x sequence
    w- the y sequence
    """
    deletion = (d[i-1][j] - 2, 'D')
    insertion = (d[i][j-1] - 2, 'I') 

    if str(v) == str(w):
        match_mismatch = (d[i-1][j-1] + 1, 'M')
    else:
        match_mismatch = (d[i-1][j-1] - 1, 'S')
    
    decision_list = [insertion, deletion, match_mismatch]

    bt_d[i][j] = max(decision_list, key = itemgetter(0))[1] 
    d[i][j] = max(decision_list, key = itemgetter(0))[0]
    return (d,bt_d)

def get_indexes_maxvalue(d):
    max_values = []
    for i in range(1, len(d)):
        for j in range(1, len(d[i])):
            if not max_values:
                max_values = [(i,j)]
            if d[i][j] > d[max_values[0][0]][max_values[0][1]]:
                max_values = []
                max_values.append((i,j))
            elif d[i][j] == d[max_values[0][0]][max_values[0][1]]:
                max_values.append((i,j))
    return max_values

def dynamic_programming(x,y):
    ilen = len(x)
    jlen = len(y)

    d = create_matrix(ilen+1,jlen+1)
    bt_d = create_matrix(ilen+1,jlen+1) # backtracking matrix

    ## initialize
    for i in range(0, len(d)):
        for j in range(0, len(d[i])):
            d[i][0] = 0
            d[0][j] = 0
            bt_d[i][0] = 0
            bt_d[0][j] = 0
    x= '#'+x
    y= '#'+y
    d[0][0]=0
    bt_d[0][0]=0

    for i in range(1, len(d)):
        for j in range(1, len(d[i])):
            (d, bt_d) = semiglobal(d, bt_d, i, j, x[i],y[j])
    return(d, bt_d)

# backtrace
def backtrace(d, bt_d, x, y, max_values):
    x= '#'+x
    y= '#'+y
    for (i,j) in max_values:
        print(d[i][j]) # print max length
        new_x = ''
        new_y = ''
        while j >0 and i >0:
            if str(bt_d[i][j]) == 'M':
                new_x = new_x + x[i]
                new_y = new_y + y[j]
                i = i-1
                j = j-1
                continue
            if str(bt_d[i][j]) == 'I':
                new_x = new_x + '-'
                new_y = new_y + y[j]
                j = j-1
                continue
            if str(bt_d[i][j]) == 'D':
                new_x = new_x + x[i]
                new_y = new_y + '-'
                i = i-1
                continue
            if str(bt_d[i][j]) == 'S':
                new_x = new_x + x[i]
                new_y = new_y + y[j]
                i = i-1
                j = j-1
                
                continue

        new_x = new_x[::-1]
        new_y = new_y[::-1]
        print(new_x + "\n" + new_y)

if __name__ == '__main__':
    records = list(SeqIO.parse(sys.argv[1], "fasta"))
    x = (records[0].seq)  # first record
    y = (records[-1].seq)  # last record

    matrix, backtracking_matrix  = (dynamic_programming(x,y))

    # for just semi-global
    # get max of last row or last col
    # max of max(last row/col) 
    lastrow = (matrix[len(x)])
    lastcol = ([item[-1] for item in matrix])
    maxval_row = max(lastrow)
    maxval_col = max(lastcol)
    
    if maxval_row > maxval_col:
        maxval_indexes = [(len(x),i) for i, v in enumerate(lastrow) if v == maxval_row]
    else:
        maxval_indexes = [(i,len(y)) for i, v in enumerate(lastcol) if v == maxval_col]

    backtrace(matrix, backtracking_matrix, x, y, maxval_indexes)

