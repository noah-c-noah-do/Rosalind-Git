seq = []
fasta_name = []
test = ""
gc_content = []

with open('rosalind_gc.txt', 'r') as readfile:
    for line in readfile:
        if line[0] == '>':
            line = line.rstrip()
            fasta_name.append(line[1:])
            seq.append(test)
            test = ""
        else:
            line = line.rstrip()
            test += line
    seq.append(test)
    readfile.close()
seq.pop(0)
print(f'sequences are:\n{seq}')
print(f'fasta names are:\n{fasta_name}')


def calc_GC_content(X):
    nuc_list = []
    for i in X:
        nuc_list += i
    ggg = nuc_list.count('G')
    ccc = nuc_list.count('C')
    gggccc = round(100 * (ggg + ccc) / (len(nuc_list)), 5)
    return gggccc


for element in seq:
    gc_content.append(calc_GC_content(element))
print(gc_content)

print(fasta_name[(gc_content.index(max(gc_content)))])
print(max(gc_content))
