import unittest
import LCA


class test_node(unittest.TestCase):

    # 1. Test LCA scenarios
    def testLCA(self):
        root = LCA.Node(1)
        root.left = LCA.Node(2)
        root.right = LCA.Node(3)
        root.left.left = LCA.Node(4)
        root.left.right = LCA.Node(5)
        root.right.left = LCA.Node(6)
        root.right.right = LCA.Node(7)
        self.assertEqual(1, LCA.lowestCommonAncestor(root, 4, 3))
        self.assertEqual(1, LCA.lowestCommonAncestor(root, 2, 7))
        self.assertEqual(3, LCA.lowestCommonAncestor(root, 6, 7))

    # 2.  Test if null
    def testNull(self):
        root = None
        self.assertEqual(-1, LCA.lowestCommonAncestor(root, 4, 5), 'Empty tree returns -1')

    # 3. Invalid Node
    def testInvalidNode(self):
        root = LCA.Node(1)
        root.left = LCA.Node(2)
        root.right = LCA.Node(3)
        root.left.left = LCA.Node(4)
        root.left.right = LCA.Node(5)
        root.right.left = LCA.Node(6)
        root.right.right = LCA.Node(7)
        self.assertEqual(-1, LCA.lowestCommonAncestor(root, 4, 9), "Unfound node returns -1")

    # 4. Root is only node
    def test_rootIsNodeOnly(self):
        root = LCA.Node(1)
        self.assertEqual(1, LCA.lowestCommonAncestor(root, 1, 1))

    # 5. Duplicated Nodes
    def test_duplicatedNodes(self):
        root = LCA.Node(1)
        root.left = LCA.Node(2)
        root.right = LCA.Node(3)
        root.left.left = LCA.Node(4)
        root.left.right = LCA.Node(6)
        root.right.left = LCA.Node(6)
        root.right.right = LCA.Node(7)
        self.assertEqual(1, LCA.lowestCommonAncestor(root, 6, 7))
        # 1 is the common root of both 6's


if __name__ == '__main__':
    unittest.main()

