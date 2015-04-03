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

    def test_search_1(self):
        result = self.msf.search(1)
        self.assertEqual(result, None)

    def test_search_2(self):
        result = self.msf.search(2)
        self.assertEqual(result, None)

    def test_search_3(self):
        result = self.msf.search(3)
        self.assertEqual(result, 3)

    def test_search_4(self):
        result = self.msf.search(4)
        self.assertEqual(result, 3)

    def test_missing_subsequences_2(self):
        result = self.msf.missing_subsequences(2)
        self.assertListEqual(result, [])

    def test_missing_subsequences_3(self):
        result = self.msf.missing_subsequences(3)
        self.assertListEqual(result, ['TCG', 'CCT', 'GCT'])

    def test_interleavings(self):
        chars = ''
        chunk = 'AA'
        i = [i for i in self.msf.interleavings(chars, chunk)]
        self.assertListEqual(i, ['AA'])

        chars = 'T'
        i = [i for i in self.msf.interleavings(chars, chunk)]
        self.assertSetEqual(set(i), {'AAT', 'TAA'})

        chars = 'TC'
        i = [i for i in self.msf.interleavings(chars, chunk)]
        self.assertSetEqual(set(i), {'AATC', 'TAAC', 'TCAA'})


if __name__ == '__main__':
    unittest.main()
