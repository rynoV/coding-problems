import unittest
from queue import Queue


class TestQueue(unittest.TestCase):
    def test_add(self):
        queue = Queue()
        queue.add(1)
        self.assertEqual(1, queue.peek())
        self.assertFalse(queue.isEmpty())
        queue.add(2)
        queue.add(3)
        self.assertEqual(1, queue.peek())

    def test_remove(self):
        queue = Queue()
        queue.add(1)
        self.assertEqual(1, queue.remove())
        self.assertTrue(queue.isEmpty())
        queue.add(2)
        queue.add(3)
        self.assertEqual(2, queue.remove())
        self.assertEqual(3, queue.remove())
        self.assertTrue(queue.isEmpty())


if __name__ == '__main__':
    unittest.main()
