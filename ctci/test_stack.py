import unittest
from stack import Stack


class TestStack(unittest.TestCase):
    def test_push(self):
        stack = Stack()
        stack.push(1)
        self.assertEqual(1, stack.peek())
        self.assertFalse(stack.isEmpty())
        stack.push(2)
        self.assertEqual(2, stack.peek())

    def test_pop(self):
        stack = Stack()
        stack.push(1)
        self.assertEqual(1, stack.pop())
        self.assertTrue(stack.isEmpty())
        stack.push(2)
        stack.push(3)
        self.assertEqual(3, stack.pop())
        self.assertEqual(2, stack.pop())
        self.assertTrue(stack.isEmpty())


if __name__ == '__main__':
    unittest.main()
