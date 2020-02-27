#!/usr/bin/python

#Distance Between Leaves Problem
#Compute the distances between leaves in a weighted tree.

#Given: An integer n followed by the adjacency list of a weighted tree with n leaves.
#Return: A space-separated n x n (di, j), where di, j is the length of the path between leaves i and j.

import sys

# read experimental spectra
fh = open(sys.argv[1], 'r')
num_leaves = int(fh.readline().strip())
adjacency_list = []
for al in fh.readlines():
    adjacency_list.append(al.strip())


def create_matrix(i,j):
    d = []
    for row in range(0,i):
        temp = []
        for col in range(0,j):
            temp.append(0)
        d.append(temp)

    return(d)

def distance_nodes(node, inner_node, graph, traversed_list, distance, matrix, level):
    for d in inner_node:
        if int(d[0]) in traversed_list:
            continue
        else:
            traversed_list.append(int(d[0]))
        if int(d[0]) == int(node):
            continue
        new_distance = distance + int(d[1])
        if int(d[0]) < len(matrix[0]):
            matrix[int(node)][int(d[0])] = new_distance
        distance_nodes(node, graph[d[0]], graph, traversed_list, new_distance, matrix, level=level+1)
    return  matrix 


graph = {}
for edges in adjacency_list:
    nodes, edge_distance = edges.split(':')
    nodeA, nodeB = nodes.split("->")
    graph.setdefault(nodeA,[]).append((nodeB,edge_distance))


# create matrix and iterate through the graph
i = num_leaves; j = num_leaves
matrix = create_matrix(i, j)
for node in graph:
    if not int(node) < num_leaves:
        continue
    traversed_list = []
    traversed_list.append(int(node))
    distance = 0
    matrix = distance_nodes(node, graph[node], graph,  traversed_list, distance, matrix, level=1)

# print final matrix
for line in matrix:
    print(" ".join(map(str, line)))

