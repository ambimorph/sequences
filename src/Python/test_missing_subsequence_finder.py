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

    def test_insert_last_letter(self):
        self.msf.d = {'A': {'C', 'G'}}
        self.msf.insert_last_letter('AA')
        self.assertDictEqual(self.msf.d, {'A': {'A', 'C', 'G'}})
        self.msf.insert_last_letter('AT')
        self.assertDictEqual(self.msf.d, {'AA': set([]),
                                          'AC': set([]),
                                          'AG': set([]),
                                          'AT': set([])})

    def test_all_of_length_i(self):
        self.assertTrue(self.msf.all_of_length_i(1))
        self.assertTrue(self.msf.all_of_length_i(2))
        self.assertFalse(self.msf.all_of_length_i(3))
                  
if __name__ == '__main__':
    unittest.main()
