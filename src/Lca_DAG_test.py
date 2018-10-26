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

if __name__ == '__main__':
    unittest.main()
