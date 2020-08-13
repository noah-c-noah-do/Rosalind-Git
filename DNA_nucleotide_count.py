dna_nucleotide = 'GTGATCCAGGGTTTATATCTTTAGCGCGGAAGTATATAAAAGGTCCTTGTAATGTGCCAGGATAAGTCGACCTCGCTGACACATCATTTGAACAAGATTATCATGCAAATTCCGTTTCCACCGTGTCTCACAGGTATGTCCGACCCCTGACTGCAGTGTCGTCAGTTCCTCCCCTCCGAACGACGAGGTCATCTGGCGGCCGCCACGCAGCAAAAATATATCGCCATTAAGTTATTGTGAAACTTAGACACCGGATGATGTCGCTGTGTAATCACGCACACAGGTTAAACCTAATCATCCCCGCCTCGAACCTAGCGTGTGCTTGCACACACGTGCGGTGACTTTGTGCGCGTTGGTGCAATAACAGATCGCCCCGCTATTCTCGGTTGCAGCCGTCTCGAACGTTTAACGGTTGATTGCGAGAAACTCGATGAGCTCTGCGGACAACTGAGCAATGGAAAGTGCCCAGGGCTTACCGGATCCGATCCGAGAGTGAGGAAGTCTAAATGCCTGGTGCATCCGCGTTACTGACCCACAGCGTCACCGGTGTTCTGCATATTTCAGGCCAACGACTTATAACATCTCTCCGTAGTAAGTCGCGAGGTATATCTGCATTGCGGCTCATTGACATGCCCCTTTATGTGGCCATATGTTGCGCCTAGAGGACGATTACACCCGAAACAGTGGAAACTAATCGGTCTCTCACATTCAAGGTCTCTGCCAGAGCCGTGCTCGTTGTGCTTTGGTTATCTCCAGGACTGCGCACCACACGCCAATGCTATAATGAGCTTCCCGTTGTCCAGGGTATACGCAGCTTATTGGTTTGGCTTCTCCAAATATGTTAGGTGATTCGTTTAGTTACCTTGCTCCTGGTCCGAACCGTGCTGGAACTCGACCCGTATTGTCGCTCATAATAGTAGTGACTCTTTAACTGCTCCGCGTAGATAGCGT'
adenine_count = dna_nucleotide.count('A')
cytosine_count = dna_nucleotide.count('C')
guanine_count = dna_nucleotide.count('G')
thymine_count = dna_nucleotide.count('T')

print(f'{adenine_count} {cytosine_count} {guanine_count} {thymine_count} ')
