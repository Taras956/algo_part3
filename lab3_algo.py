import unittest
from typing import List

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def pre_order_traversal(root: BinaryTree) -> List[int]:
    if not root:
        return []
    
    result = [root.value]
    result += pre_order_traversal(root.left)
    result += pre_order_traversal(root.right)
    
    return result

class TestPreOrderTraversal(unittest.TestCase):
    def setUp(self):
        self.root = BinaryTree(1)
        self.root.left = BinaryTree(2)
        self.root.right = BinaryTree(3)
        self.root.left.right = BinaryTree(5)
        self.root.right.left = BinaryTree(6)
        self.root.right.right = BinaryTree(7)

    def test_pre_order_traversal(self):
        result = pre_order_traversal(self.root)
        self.assertEqual(result, [1, 2, 5, 3, 6, 7])

    def test_empty_tree(self):
        result = pre_order_traversal(None)
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()