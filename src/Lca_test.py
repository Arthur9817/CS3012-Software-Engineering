import unittest
import Lca

class TestLCA(unittest.TestCase):

    def test_node_1_and_3(self):
        result = Lca.findLCA(Lca.Node(1), 1, 3).key
        expected = 1
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
