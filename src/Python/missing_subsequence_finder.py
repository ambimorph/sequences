import time

class MSF(object):

    def __init__(self, sequence, alphabet):

        self.s = sequence
        self.alphabet = alphabet
        self.d = {'': set([])}

    def insert_last_letter(self, word):
        """
        returns True if the prefix now has all four possible endings
        """
        prefix = word[:-1]
        if self.d.has_key(prefix): # else prefix is already known to be full
            self.d[prefix].add(word[-1])
            if len(self.d[prefix]) == 4:
                return True

    def update_full_key(self, prefix):
        """
        Adds all one character increments of prefix to d, deletes prefix.
        """
        for c in self.d.pop(prefix):
            self.d[prefix+c] = set([])

    def ith_pass(self, i):
        """
        Returns True if all subsequences of length i present, else None
        """
        t = time.time()
        for w, _ in enumerate(self.s[:len(self.s)-i+1]): # all indices to subsequences of length i
            word = self.s[w:w+i]
            full = self.insert_last_letter(word)
            if full:
                self.update_full_key(word[:-1])
                if len(self.d) == 4**i:
                    print "Checked {} words in {} seconds".format(w+1, time.time()-t)
                    return True

    def search(self, n):
        """
        Returns True if there are missing subsequences of length <= n
        """
        for i in xrange(n):
            print "Pass {} of {}".format(i+1, n)
            if not self.ith_pass(i+1):
                return True

if __name__ == '__main__':

    import sys

    chars = 'ACGT'
    with open(sys.argv[1], 'r') as f:
        s = f.readline().strip()
        n = int(sys.argv[2])

        missing_subsequences = []

        msf = MSF(s, chars)
        result = msf.search(n)
        print "Missing of length {}".format(n), result
        for k in msf.d.iterkeys():
            if len(k) < (n):
                for c in chars:
                    if c not in msf.d[k]:
                        missing_subsequences.append(k+c)
                        
        print s
        print missing_subsequences

        for k,v in msf.d.iteritems(): 
            if len(k) < n: print k, v


        
