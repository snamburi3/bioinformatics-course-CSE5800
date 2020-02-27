import sys
from itertools import combinations

# read experimental spectra
fh = open(sys.argv[1], 'r')
#input_string = fh.readline().strip()
spectrum = list(map(int, fh.readline().strip().split(' ')))
exp_spectrum = {}
for l in spectrum:
    exp_spectrum[l] = 1   

# integer Masses
integer_masses = {}
amino_acids = "G A S P V T C I L N D K Q E M N F R Y W"
masses = "57 71 87 97 99 101 103 113 113 114 115 128 128 129 131 137 147 156 163 186"

aa_masses = list(map(int, masses.split(" ")))
for idx, aa in enumerate(amino_acids.split(" ")):
    integer_masses[aa] = aa_masses[idx]

# check if the aa masses are in the spectrum
def spectrum_single_aa(masses, exp_spectrum):
    masses = list(map(int, masses.split(' ')))
    aa = {}
    for mass in masses:
        if mass in exp_spectrum:
            aa[mass] = 1
    return aa

def get_all_substrings(peptide, sep='-'):
    all_pieces = list(peptide.split(sep))
    output = []
    for cut in range(1, len(all_pieces)):  
        for i in range(len(all_pieces) - cut):
            output.append(all_pieces[i:i + cut])
    output.append(all_pieces)
    return output


## check if the constituent masses in the spectrum
def bound(peptide, exp_spectrum):
    for ele in get_all_substrings(peptide, sep='-'):
        if not ele:
            continue
        masses = sum(map(int,ele))
        if int(masses) not  in exp_spectrum:
            return False
    return True

def extend(peptides, single_peptides, exp_spectrum):
    ext_peptides = {}
    for peptide in peptides:
        for single_mass in single_peptides:
            temp_peptide = str(peptide) + "-" + str(single_mass)
            peptide_mass = sum(map(int,temp_peptide.split('-')))
            if bound(temp_peptide, exp_spectrum):
            #if peptide_mass in exp_spectrum:
                ext_peptides[temp_peptide] = 1
    return(ext_peptides)

#################
single_peptides = spectrum_single_aa(masses, exp_spectrum)
peptides = {}
for aa in single_peptides:
    peptides[aa] = 1


while(peptides):
    temp_peptides = extend(peptides, single_peptides, exp_spectrum)
    if temp_peptides:
        peptides = temp_peptides
    else:
        break

final_peptides = {}
for peptide in peptides:
    final_peptides[peptide] = 1

print(" ".join(map(str,final_peptides.keys())))
