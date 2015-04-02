from missing_subsequence_finder import *
import sys, random

"""
$ python example.py l n s

l = length of random sequence to generate
n = length of subsequence to find
s = random seed

Example usage:

$ python example.py 200 3 1

ATTCCCGTAATCTACGATTAAGTCACAACCAAACCATGGATTACGGTCTGCGTTGGAATCAGGGCCGTGCCAAGTGCAGTTGTAGTGCCGTATTTGTGGCATGAGCCCGGGCAAAGTTTTCTGAAATAAGCAAGACGCCCACCAATGAGTAAAGAGGGATTGAGCGCGACTTCTCTGCCATATTGATTGGCCAGCAAGCC
Missing of length 3 True
['TCG', 'CCT', 'GCT']

"""

length, n, randseed = map(int, sys.argv[1:])

chars = 'ACGT'
s = ""
random.seed(randseed)
for i in xrange(length):
    s+= random.sample(chars, 1)[0]
print s
    
missing_subsequences = []

msf = MSF(s, chars)
print "Missing of length {}".format(n), msf.search(n)
for k in msf.d.iterkeys():
    if len(k) < (n):
        for c in chars:
            if c not in msf.d[k]:
                missing_subsequences.append(k+c)

print missing_subsequences
        

        
