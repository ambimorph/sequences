from missing_subsequence_finder import *
import sys, random

"""
$ python example.py l n s

l = length of random sequence to generate
n = length of subsequence to find
s = random seed

Example usage:

$ python example.py 200 4 99

CAAATCCGGTCCGATCCGAGTCTGTCCCAATGCTGTCATATGTTGAACTACACACGATAACCTCGTATGGGCAAAAAAGTTTATAACGAACTCCCATTGCCCGGCTGATGACTACTCGTTTGTCTCGGCGGTGCCTCGGTAGAGGGTATCCAGACGGATCAGGCGGGTTAAACGTCCGTGCTTTCACAACTGCTACCGTC
Pass 1 of 4
Checked 8 words in 2.59876251221e-05 seconds
Pass 2 of 4
Checked 47 words in 7.00950622559e-05 seconds
Pass 3 of 4
Missing subsequences: ['AGC', 'CGC']
AAGC
AGCA
ACGC
CGCA
CAGC
AGCC
CCGC
CGCC
GAGC
AGCG
GCGC
CGCG
TAGC
AGCT
TCGC
CGCT
"""

length, n, randseed = map(int, sys.argv[1:])

chars = 'ACGT'
s = ""
random.seed(randseed)
for i in xrange(length):
    s+= random.sample(chars, 1)[0]
print s
msf = MSF(s, chars)
for c in msf.generate_candidates(n):
    print c
