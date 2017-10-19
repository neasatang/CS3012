import binarytree
import unittest

class MyTestCase(unittest.TestCase):

    #test for node
    def test_node_int(self):
        node = binarytree.Node(4)
        self.assertTrue(node==4)

    #test for less than comparison
    def test_node_lt(self):
        node = binarytree.Node(6)
        self.assertTrue(node < 10)

    #test for greater than comparison
    def test_node_gt(self):
        node = binarytree.Node(4)
        self.assertTrue(node > 2)

    #test for node equal comparison
    def test_node_eq(self):
        node = binarytree.Node(4)
        self.assertTrue(node == 4)

    #test for convert to string
    def test_node_str(self):
        node = binarytree.Node(4)
        self.assertTrue(str(node) == "[Node val: 4]")

    #test for tree init
    def test_tree(self):
        tree = binarytree.Tree()
        self.assertTrue(tree.root == None)

        #tests for a node that isn't in the tree
        self.assertFalse(tree.root == 1)

    #test for tree put
    def test_put_tree(self):
        # test for one node in the tree for put and get
        tree = binarytree.Tree()
        tree.put(3)
        self.assertTrue(tree.get(3), 3)

    def test_put_tree2(self):
        # test for one node in the tree for put and get
        tree = binarytree.Tree()
        tree.put(3)
        tree.put(6)
        self.assertTrue(tree.get(6), 6)

        tree.put(7)
        self.assertTrue(tree.get(7), 7)

        # check for non node on the tree
        self.assertFalse(tree.get(10), 10)

    def test_put_tree3(self):
        # test for no node on the tree
        tree = binarytree.Tree()
        self.assertFalse(tree.get(4), 4)

    #test for full tree - this fails
    def test_LCA(self):
        tree = binarytree.Tree()
        tree.put(5)
        tree.put(3)
        tree.put(4)
        self.assertTrue(tree.find_common(5,3),4)

    #test for empty tree
    def test_LCA_2(self):
        tree = binarytree.Tree()
        self.assertFalse(tree.find_common(2,3))

    # test for one node in tree
    def test_LCA_3(self):
        tree = binarytree.Tree()
        tree.put(2)
        self.assertFalse(tree.find_common(2, None))

    # test for two nodes in binary tree
    def test_LCA_4(self):
        tree = binarytree.Tree()
        tree.put(3)
        tree.put(5)
        self.assertFalse(tree.find_common(3,5))

    def test_node_exists(self):
        tree = binarytree.Tree()
        tree.put(5)
        self.assertTrue(tree.node_exists(5))


    def test_node_exists2(self):
        tree = binarytree.Tree()
        tree.put(3)
        self.assertTrue(tree.node_exists(3))
        self.assertFalse(tree.node_exists(6))

    #test for _node_exists
    def test__node_exists(self):
        tree = binarytree.Tree()
        node = binarytree.Node(8)
        tree.put(node)
        self.assertTrue(tree._node_exists(node,8))

    def test__node_exists2(self):
        tree = binarytree.Tree()
        node = binarytree.Node(123)
        tree.put(node)
        self.assertTrue(tree._node_exists(node,123))

if __name__ == '__main__':
    unittest.main()
