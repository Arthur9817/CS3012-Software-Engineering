import unittest
import Lca

class TestLCA(unittest.TestCase):

    def test_empty(self):
        expected = None
        result = Lca.findLCA(None, None, None)
        self.assertEqual(expected, result)

    def test_lca_1_3(self):
        expected = 1
        result = Lca.findLCA(Lca.root, 1, 3)
        self.assertEqual(expected, result)

    def test_lca_4_5(self):
        expected = 2
        result = Lca.findLCA(Lca.root, 4, 5)
        self.assertEqual(expected, result)

    def test_lca_6_7(self):
        expected = 3
        result = Lca.findLCA(Lca.root, 6, 7)
        self.assertEqual(expected, result)

    def test_lca_2_6(self):
        expected = 1
        result = Lca.findLCA(Lca.root, 2, 6)
        self.assertEqual(expected, result)

    def test_lca_3_4(self):
        expected = 1
        result = Lca.findLCA(Lca.root, 3, 4)
        self.assertEqual(expected, result)

    def test_lca_8_2(self):
        expected = None
        result = Lca.findLCA(Lca.root, 8, 2)
        self.assertEqual(expected, result)

    def test_lca_0_4(self):
        expected = None
        result = Lca.findLCA(Lca.root, 0, 4)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
