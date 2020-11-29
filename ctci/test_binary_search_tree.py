import unittest
from binary_search_tree import BinarySearchTree


class TestBinarySearchTree(unittest.TestCase):
    def test_add(self):
        bst = BinarySearchTree()
        vals = [10, 5, 3, 7, 15, 13, 17]
        for val in vals:
            bst.add(val)
        for i, (actual, expected) in enumerate(zip(bst, sorted(vals))):
            self.assertEqual(actual, expected)
        self.assertEqual(len(vals) - 1, i)

    def test_pre_order(self):
        bst = BinarySearchTree()
        vals = [10, 5, 3, 7, 15, 13, 17]
        for val in vals:
            bst.add(val)
        for i, (actual, expected) in enumerate(zip(bst.pre_order_iterator(), vals)):
            self.assertEqual(actual, expected)
        self.assertEqual(len(vals) - 1, i)

    def test_post_order(self):
        bst = BinarySearchTree()
        vals = [10, 5, 3, 7, 15, 13, 17]
        ordered = [3, 7, 5, 13, 17, 15, 10]
        for val in vals:
            bst.add(val)
        for i, (actual, expected) in enumerate(zip(bst.post_order_iterator(), ordered)):
            self.assertEqual(actual, expected)
        self.assertEqual(len(vals) - 1, i)


if __name__ == '__main__':
    unittest.main()
