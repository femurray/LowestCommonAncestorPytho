import unittest
import LCA

class LCAPythonTest(unittest.TestCase):

    # 1. Test LCA scenarios
    def test_tree(self):
        self.assertEqual(LCA.findLCA(LCA.root, 2, 3).key, 1)
        self.assertEqual(LCA.findLCA(LCA.root, 4, 5).key, 2)
        self.assertEqual(LCA.findLCA(LCA.root, 6, 7).key, 3)

    # 2. Test empty tree
    def test_emptyTree(self):
        self.assertEqual(LCA.findLCA(None, None, None), None)

    # 3. Test same node
    def test_sameNode(self):
        self.assertEqual(LCA.findLCA(LCA.root, 1, 1).key, 1)

if __name__ == '__main__':
    unittest.main()

