#!/usr/bin/env python3

# reverse complement

#forward input
og_seq = 'GATGGGATTggggttttccccTCCCATGTGCTCAAGACTGGCGCTaaaaGttttGAGCTTCTCaaaaGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCggggACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGccccCTCTGAGTCAGGAAACAttttCAGACCTATGGAAACTACTTCCTGaaaaCAACGTTCTGTccccCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTccccGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTccccCCGTGGccccTGCACCAGCAGCTCCTACACCGGCGGccccTGCACCAGccccCTCCTGGccccTGTCATCTTCTGTCCCTTCCCAGaaaaCCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTccccTGCCCTCAACAAGATGttttGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACAccccCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGccccCACCATGAGCGCT'

#test
test_seq = og_seq[0:20]
test_seq = test_seq.upper()
test_rev = test_seq[::-1]

test_revCc = test_rev.replace('C','c')
test_revGC = test_revCc.replace('G', 'C')
test_revcG = test_revGC.replace('c', 'G')
test_revAa = test_revcG.replace('A', 'a')
test_revTA = test_revAa.replace('T', 'A')
test_revcomp = test_revTA.replace('a', 'T')

print(f'This is test sequence: {test_seq:>5} and \nthis is the reverse: {test_rev:>5} and \nthis is the reverse complement: {test_revcomp:>5}')

#og seq
og_seq = og_seq.upper()

#complement
seq_Aa = og_seq.replace('A', 'a')
seq_TA = seq_Aa.replace('T', 'A')
seq_aT = seq_TA.replace('a', 'T')
seq_Gg = seq_aT.replace('G', 'g')
seq_CG = seq_Gg.replace('C', 'G')
seq_gC = seq_CG.replace('g', 'C')

#complement
seq_comp = seq_gC

#reverse complement
seq_revcomp = seq_comp[::-1]

#print
print(f'Sequence: {og_seq:>5}')
print(f'Complement: {seq_comp:>5}')
print(f'Reverse complement: {seq_revcomp:>5}')

#print readable subset
print(f'Sequence: {og_seq[1:10]:>20} \nComplement: {seq_comp[1:10]:>18} \nReverse complement: {seq_revcomp[1:10]:>10}')
