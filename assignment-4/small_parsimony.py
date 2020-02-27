import sys
import pprint

#SmallParsimony(T, Character)
# for each node v in tree T
#        Tag(v) ← 0
#  if v is a leaf
#   Tag(v) ← 1
#   for each symbol k in the alphabet
#    if Character(v) = k
#     sk(v) ← 0
#    else
#     sk(v) ← ∞
# while there exist ripe nodes in T
#  v ← a ripe node in T
#  Tag(v) ← 1
#  for each symbol k in the alphabet
#      sk(v) ← minimum over all symbols i {si(Daughter(v))+δi,k} + minimum over all symbols j {sj(Son(v))+δj,k}
#   return minimum over all symbols k {sk(v)}

bases = ['A', 'T', 'G', 'C']

def calculate_hamming(str1, str2):
    dist = 0
    for a, b in zip(str1, str2):
        if a != b:
            dist = dist + 1
    return dist


def initialize_scores(seq):
    char_array = {}
    for i, nuc in enumerate(seq):
        char_array[i] = {}
        for base in bases:
            if str(base) == str(nuc):
                char_array[i][str(base)] = 0
            else:
                char_array[i][str(base)] = float('inf')

    return char_array

def is_leaf(node):
    flag = []
    for s in node:
        if s not in bases:
            flag.append(False)
        else:
            flag.append(True)
    return any(flag)

def get_score(nuc, index, score_dict):
    scores = []
    for n, s in score_dict[index].items():
        if str(base) == str(n):
            delta = 0
        else:
            delta = 1
        scores.append(s + delta)
    return min(scores)

def get_seq_from_scores(score_dict):
    seq = ''
    for index in range(len(score_dict)):
        s = min([(b, s) for b, s in score_dict[index].items()], key=lambda se: se[1])
        seq += s[0]
    return seq

# read input
fh = open(sys.argv[1], 'r')
num_leaves = int(fh.readline().strip())
adjacency_list = []
for al in fh.readlines():
    adjacency_list.append(al.strip())

# create a tree to traverse
tree = {}
score_dict = {}
for e in adjacency_list:
    edge = e.split("->")
    node = edge[0]
    child = edge[1]
    tree.setdefault(node,[]).append(child)

processed = {}
for node in tree:
    daughter = tree[node][0]
    son = tree[node][1]
    if is_leaf(daughter) or is_leaf(son):
        score_dict[daughter] = initialize_scores(daughter)
        score_dict[son]= initialize_scores(son)
        seq_len = len(son)
        processed[daughter] = True
        processed[son] = True

for node in tree:
    son, daughter = tree[node]
    score_dict[node] = {}
    for char_index in range(seq_len):
        score_dict[node][char_index] = {}
        for base in bases:
#            print("te", char_index, base, son, daughter, best_neighbour_score(base, char_index, score_dict[str(daughter)]))
            d_score = get_score(base, char_index, score_dict[str(daughter)])
            s_score = get_score(base, char_index, score_dict[str(son)])
            score_dict[node][char_index][base] = (d_score + s_score)
        processed[str(node)] = True


seq_nodes = {}
total_dist = []
for node in tree:
    daughter = tree[node][0]
    son = tree[node][1]
    ancestor = get_seq_from_scores(score_dict[node])
    if is_leaf(daughter) or is_leaf(son):
        d_dist = calculate_hamming(ancestor,daughter)
        s_dist = calculate_hamming(ancestor,son)
        total_dist.append(d_dist)
        total_dist.append(s_dist)
        print("".join(map(str, (ancestor, "->", daughter, ":", d_dist))))
        print("".join(map(str, (ancestor, "->", son, ":", s_dist))))

        seq_nodes[str(node)] = ancestor
    else:
        d_dist = calculate_hamming(ancestor,seq_nodes[str(daughter)])
        s_dist = calculate_hamming(ancestor,seq_nodes[str(son)])
        total_dist.append(d_dist)
        total_dist.append(s_dist)
        print("".join(map(str, (ancestor, "->", seq_nodes[str(daughter)], ":", d_dist))))
        print("".join(map(str, (ancestor, "->", seq_nodes[str(son)], ":", s_dist))))

print(sum(total_dist))

