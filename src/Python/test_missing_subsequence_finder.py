import unittest, missing_subsequence_finder


class MSFTest(unittest.TestCase):

    def setUp(self):
        sequence = ("ATTCCCGTAATCTACGATTAAGTCACAACCAAACCATGGATTACGGTCTGCGTTGGAATCA"
                    "GGGCCGTGCCAAGTGCAGTTGTAGTGCCGTATTTGTGGCATGAGCCCGGGCAAAGTTTTCT"
                    "GAAATAAGCAAGACGCCCACCAATGAGTAAAGAGGGATTGAGCGCGACTTCTCTGCCATAT"
                    "TGATTGGCCAGCAAGCC")
        alphabet = 'ACGT'
        self.msf = missing_subsequence_finder.MSF(sequence, alphabet)

    def test_update_full_key(self):
        self.msf.d = {'A': {'A', 'C', 'T', 'G'}}
        self.msf.update_full_key('A')
        self.assertDictEqual(self.msf.d, {'AA': set([]),
                                          'AC': set([]),
                                          'AG': set([]),
                                          'AT': set([])})
                  
if __name__ == '__main__':
    unittest.main()
