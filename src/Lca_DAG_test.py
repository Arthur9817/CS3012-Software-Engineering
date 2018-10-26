import unittest
import Lca_DAG

class TestDAG(unittest.TestCase):

    def test_lca_empty(self):
        expected = None
        result = Lca_DAG.findLCA(None, None, None)
        self.assertEqual(expected, result)

    def test_lca_1_3(self):
        expected = 1
        result = Lca_DAG.findLCA(Lca_DAG.root, Lca_DAG.root, Lca_DAG.n3)
        self.assertEqual(expected, result)

    def test_lca_2_3(self):
        expected = 1
        result = Lca_DAG.findLCA(Lca_DAG.root, Lca_DAG.n2, Lca_DAG.n3)
        self.assertEqual(expected, result)

    def test_lca_4_6(self):
        expected = 3
        result = Lca_DAG.findLCA(Lca_DAG.root, Lca_DAG.n4, Lca_DAG.n6)
        self.assertEqual(expected, result)

    def test_lca_5_7(self):
        expected = 2
        result = Lca_DAG.findLCA(Lca_DAG.root, Lca_DAG.n5, Lca_DAG.n7)
        self.assertEqual(expected, result)

    def test_lca_6_7(self):
        expected = 1
        result = Lca_DAG.findLCA(Lca_DAG.root, Lca_DAG.n6, Lca_DAG.n7)
        self.assertEqual(expected, result)

    def test_lca_2_6(self):
        expected = 4
        result = Lca_DAG.findLCA(Lca_DAG.root, Lca_DAG.n2, Lca_DAG.n6)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
