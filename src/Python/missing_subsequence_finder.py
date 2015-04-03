import time, itertools

class MSF(object):

    def __init__(self, sequence, alphabet):

        self.s = sequence
        self.alphabet = alphabet
        self.d = {'': set([])}

    def update_full_key(self, prefix):
        """
        Adds all one character increments of prefix to d, deletes prefix.
        """
        for c in self.d.pop(prefix):
            self.d[prefix+c] = set([])

    def insert_last_letter(self, word):
        """
        returns True if the prefix now has all four possible endings
        """
        prefix = word[:-1]
        if self.d.has_key(prefix): # else prefix is already known to be full
            self.d[prefix].add(word[-1])
            if len(self.d[prefix]) == 4:
                self.update_full_key(prefix)
                return True

    def all_of_length_i(self, i):
        """
        Returns True if all subsequences of length i present, else None
        """
        t = time.time()
        for w, _ in enumerate(self.s[:len(self.s)-i+1]): # all indices to subsequences of length i
            word = self.s[w:w+i]
            full = self.insert_last_letter(word)
            if full and len(self.d) == 4**i:
                print "Checked {} words in {} seconds".format(w+1, time.time()-t)
                return True

    def search(self, n):
        """
        Returns True if there are missing subsequences of length <= n
        """
        for i in [i+1 for i in xrange(n)]:
            print "Pass {} of {}".format(i, n)
            if not self.all_of_length_i(i):
                return i

    def missing_subsequences(self, n):

        pass_in_which_found = msf.search(n)
        missing_subsequences = []
        for k in msf.d.iterkeys():
            if len(k) < (pass_in_which_found):
                for c in chars:
                    if c not in msf.d[k]:
                        missing_subsequences.append(k+c)
        return missing_subsequences

    def interleavings(self, chars, chunk):
        """
        slides chunk across windows of chars
        """
        for i, _ in enumerate(chars):
            yield chars + chunk
            yield chars[:i] + chunk + chars[i:]

    def generate_candidates(self, n):

        subsequences = self.missing_subsequences(n)
        print "Missing subsequences:", subsequences
        if len(subsequences) == 0:
            return
        length = len(subsequences[0])
        if length == n:
            for s in subsequences:
                yield s
        else:
            filler_generator = (''.join(i) for i in
                                itertools.product(self.alphabet, repeat = n - length))
            for f in filler_generator:
                for s in subsequences:
                    for word in self.interleavings(f,s):
                        yield word


if __name__ == '__main__':

    import sys

    chars = 'ACGT'
    with open(sys.argv[1], 'r') as f:
        s = f.readline().strip()
    n = int(sys.argv[2])
    msf = MSF(s, chars)
    for c in msf.generate_candidates(n):
        print c
