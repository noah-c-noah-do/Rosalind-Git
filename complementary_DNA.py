dna_strand = 'TAACCTAATCCTGAGGGTTCATTTAGGCGGACTCACCTGCAAATTGCATTGCTCGTTCTCCCGGCAAACCCTCTGGCCTTGGAGTCTAAGTCTCGGTCCGGTGCGCGATGAATGGCGATAAGACTAATACTAAAAAGCGCAGAAGAATCCTACGGGGAGAATAGGCGGTCAATCCCAACTTGGTATCCCACTGCCGAAAGGATCTCAAGCAACCCACCCTCACGAACGGCGAAGTGTCCACACACCCCTTTAAGTAGCCGCTAGATGCGTTGGCGTATACCGATGGCTACGAACGAATGGTGAGGAATCCTGTATCTCCGGGAGAGAAGCGGCGCCCACTGGTACCGGTAGGAGAGCGGCAGTGGCGGACAGCCGACCCGGTATTCCCCCTTGTTTGATTTGAAGCGTGCAGACAACGCATCTGTTGGATCACAAGGTAGCCATCGCAGACCTGAAACTTATAGCCTCACTTAACTGTGGTAGAGTAGGGCTGCGGTACCTATCAAAGGTAATTAGCTCACTCAAAACAATTTCCTAGATGCATTGAACGGTCATCCGGCTGGCTTCGTCATAACCCGCCGACGTCAGTTAGTCCGTGTCAGCGAAACAAGTAAATCGATCCGCAAGTAACCAAACACTGCGGACCGAATGCGTGTACGCCAGATAACGACCGTGGGAGTTCATCAACACTCGTTCGTACGCACGCCATAGACTTGTCTTATTGTACCAGGCCATGCCGCAAAAGCACCATCAAATTATCAGTAGCGAAATGTAAACTGAGCCTGCAGACGGATTACAACAATAATCGTTGAGATAGCTCTGCGATGAAGTAATGTATGAGCAATCGTGTAACATTATTGCTCAGTCTTGC'
dna_complement = ''
for letter in dna_strand:
    if letter == 'T':
        letter = 'A'
        dna_complement += letter
    elif letter == 'A':
        letter = 'T'
        dna_complement += letter
    elif letter == 'C':
        letter = 'G'
        dna_complement += letter
    elif letter == 'G':
        letter = 'C'
        dna_complement += letter

dna_complement = dna_complement[::-1]
print(dna_complement)