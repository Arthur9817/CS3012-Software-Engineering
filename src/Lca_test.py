import unittest
import Lca

class TestLCA(unittest.TestCase):

    # def test_empty(self):
    #     expected = None
    #     result = Lca.findLCA(None, None, None)
    #     self.assertEqual(expected, result)

    # def test_lca_1_3(self):
    #     expected = 1
    #     result = Lca.findLCA(Lca.root, Lca.root, Lca.r3)
    #     self.assertEqual(expected, result)

     def test_node1_3(self):
        self.assertEqual(Lca.findLCA(Lca.root, Lca.root.key, Lca.r3.key).key, 1)

if __name__ == '__main__':
    unittest.main()
