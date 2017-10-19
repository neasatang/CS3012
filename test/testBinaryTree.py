import binarytree
import unittest

class MyTestCase(unittest.TestCase):

    #test for node init
    def test_node_init_true(self):
        #test for value in the node
        node = binarytree.Node(4)
        self.assertTrue(node==4)

    #test for node init
    def test_node_init_false(self):
        #test for a value that isn't in the node
        node = binarytree.Node(8)
        self.assertFalse(node == 5)

    #test for less than comparison
    def test_node_lt_true(self):
        #test for actual value that is less than
        node = binarytree.Node(6)
        self.assertTrue(node < 10)

    #test for less than comparison
    def test_node_lt_false(self):
        #test for value that isn't less than
        node = binarytree.Node(3)
        self.assertFalse(node < 2)

    #test for greater than comparison
    def test_node_gt_true(self):
        #test for actual value that is greater than
        node = binarytree.Node(4)
        self.assertTrue(node > 2)

    #test for greater than comparison
    def test_node_gt_false(self):
        #test for value that isn't greater than
        node = binarytree.Node(4)
        self.assertFalse(node > 5)

    #test for node equal comparison
    def test_node_eq_true(self):
        #test for actual value that is equal
        node = binarytree.Node(4)
        self.assertTrue(node == 4)

    #test for node equal comparison
    def test_node_eq_false(self):
        #test for value that isn't equal
        node = binarytree.Node(4)
        self.assertFalse(node == 6)

    #test for convert to string
    def test_node_str(self):
        node = binarytree.Node(4)
        self.assertTrue(str(node) == "[Node val: 4]")

    #test for tree init
    def test_tree_true(self):
        #tests for an empty tree
        tree = binarytree.Tree()
        self.assertTrue(tree.root == None)

    #test for tree init
    def test_tree_false(self):
        #tests for a node that isn't in the tree
        tree = binarytree.Tree()
        self.assertFalse(tree.root == 1)

    #test for tree put
    def test_put_tree(self):
        # test for one node in the tree for put and get
        tree = binarytree.Tree()
        tree.put(3)
        self.assertTrue(tree.get(3), 3)

    #test for tree put
    def test_put_tree2(self):
        # test for one node in the tree for put and get
        tree = binarytree.Tree()
        tree.put(3)
        tree.put(6)
        self.assertTrue(tree.get(6), 6)

    #test for tree put
    def test_put_tree3(self):
        #test for a 3 node filled tree for put and get
        tree = binarytree.Tree()
        tree.put(3)
        tree.put(6)
        tree.put(7)
        self.assertTrue(tree.get(7), 7)

    #test for tree put
    def test_put_tree4(self):
        #test for a node not in the tree
        tree = binarytree.Tree()
        tree.put(3)
        tree.put(6)
        tree.put(7)
        # check for non node on the tree
        self.assertFalse(tree.get(10), 10)

    #test for tree put
    def test_put_tree5(self):
        # test for no node on the tree
        tree = binarytree.Tree()
        self.assertFalse(tree.get(4), 4)

    #test for full tree
    def test_LCA(self):
        tree = binarytree.Tree()
        tree.put(5)
        tree.put(3)
        tree.put(4)
        self.assertTrue(tree.find_common(4,5)==5)

    #test for empty tree
    def test_LCA_2(self):
        tree = binarytree.Tree()
        self.assertFalse(tree.find_common(2,3))

    #test for one node in tree
    def test_LCA_3(self):
        tree = binarytree.Tree()
        tree.put(2)
        self.assertTrue(tree.find_common(2,2)==2)

    #test for one node in tree
    def test_LCA_4(self):
        tree = binarytree.Tree()
        tree.put(2)
        self.assertFalse(tree.find_common(2,5))

    #test for two nodes in a tree
    def test_LCA_5(self):
        tree = binarytree.Tree()
        tree.put(2)
        tree.put(4)
        self.assertTrue(tree.find_common(2, 4),2)

    #test for if node exists in tree
    def test_node_exists(self):
        tree = binarytree.Tree()
        tree.put(5)
        self.assertTrue(tree.node_exists(5))

    #test for if node exists in tree
    def test_node_exists2(self):
        #test for node not existing in tree
        tree = binarytree.Tree()
        tree.put(3)
        self.assertFalse(tree.node_exists(7))

    #test for if node exists in tree
    def test_node_exists3(self):
        # test for node not existing in tree
        tree = binarytree.Tree()
        tree.put(3)
        self.assertFalse(tree.node_exists(6))

    #test for _node_exists
    def test__node_exists(self):
        tree = binarytree.Tree()
        node = binarytree.Node(8)
        tree.put(node)
        self.assertTrue(tree._node_exists(node,8))

    #test for if node exists in tree
    def test__node_exists2(self):
        tree = binarytree.Tree()
        node = binarytree.Node(123)
        tree.put(node)
        self.assertTrue(tree._node_exists(node,123))

    #test for if node exists in tree
    def test__node_exists3(self):
        #check for node not in tree
        tree = binarytree.Tree()
        node = binarytree.Node(123)
        tree.put(node)
        self.assertFalse(tree._node_exists(node, 168))

if __name__ == '__main__':
    unittest.main()
