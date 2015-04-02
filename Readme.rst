=========================
 Missing Sequence Finder
=========================

Finds subsequences of up to length n not present in a sequence (s) made from an alphabet

Gist
====

We pass through the sequence s up to n times, where n is the length
of subsequence we want to find that is not in s.

invariant:

At the beginning of the ith pass, the dictionary d holds all
|alphabet|^(i-1) keys, mapped to empty sets.  E.g. if the alphabet is
{A,C,G,T}, then at the beginning of the third pass, d holds the 16
keys AA, AC, AG,... TT.

During the ith pass, we look at all subsequences w in s of length i.
We insert the ith character of w in d[w[:-1]] (the prefix).  If w[:-1]
has size |alphabet|, we insert the |alphabet| new keys, e.g. w[:-1]A,
w[:-1]C, w[:-1]G, w[:-1]T into d, and delete the key w[:-1].

If we get to the end of the ith pass and the size of d is less than
|alphabet|^i, we now have at least one prefix of a subsequence not
in s.


Usage:

$ python missing_subsequence_finder.py filename n

