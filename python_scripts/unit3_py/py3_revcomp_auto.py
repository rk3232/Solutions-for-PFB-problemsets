#!/usr/bin/env python3

#input seq on command line, fetch reverse complement

import sys

input_seq = sys.argv[1]

seq_og = input_seq.upper()

#complement
seq_Aa = seq_og.replace('A', 'a')
seq_TA = seq_Aa.replace('T', 'A')
seq_aT = seq_TA.replace('a', 'T')
seq_Gg = seq_aT.replace('G', 'g')
seq_CG = seq_Gg.replace('C', 'G')
seq_gC = seq_CG.replace('g', 'C')

#reverse complement
seq_revcomp = seq_gC[::-1]

print(f'Sequence: {seq_og:>20} \nComplement: {seq_gC:>18} \nReverse complement: {seq_revcomp:>10}')
