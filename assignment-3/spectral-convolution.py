import sys

# read experimental spectra
fh = open(sys.argv[1], 'r')
spectrum = list(map(int, fh.readline().strip().split(' ')))


cv_dict = {}
for i in spectrum:
    for j in spectrum:
        val = i-j
        if val <= 0:
            continue
        if val in cv_dict:
            cv_dict[val] = cv_dict[val] + 1
        else:
            cv_dict[val] = 1

cv_list = []
for w in sorted(cv_dict, key=cv_dict.get, reverse=True):
    for l in range(0, cv_dict[w]):
        cv_list.append(w)

print(" ".join(map(str,cv_list)))
