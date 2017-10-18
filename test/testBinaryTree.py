import binarytree
import unittest

class MyTestCase(unittest.TestCase):

    def test_LCA(self):

        tree = binarytree.Tree()
        tree.put(2)
        tree.put(5)
        tree.put(3)
        self.assertEqual(tree.find_common(5,3),2)


if __name__ == '__main__':
    unittest.main()
