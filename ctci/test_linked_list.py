import unittest
from linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    def test_add(self):
        ll = LinkedList()
        ll.add(1)
        self.assertEqual(1, ll.get(0))
        ll.add(4)
        self.assertEqual(1, ll.get(0))
        self.assertEqual(4, ll.get(1))

    def test_update(self):
        ll = LinkedList()
        ll.add(1)
        ll.update(4, 0)
        self.assertEqual(4, ll.get(0))
        ll.add(2)
        ll.add(3)
        ll.update(5, 1)
        self.assertEqual(5, ll.get(1))
        self.assertEqual(3, ll.get(2))
        ll.update(5, 2)
        self.assertEqual(5, ll.get(2))

    def test_insert(self):
        ll = LinkedList()
        ll.add(1)
        ll.insert(4, 0)
        self.assertEqual(4, ll.get(0))
        self.assertEqual(1, ll.get(1))
        ll.insert(5, 1)
        self.assertEqual(5, ll.get(1))
        self.assertEqual(1, ll.get(2))
        ll.insert(6, 1)
        self.assertEqual(6, ll.get(1))
        self.assertEqual(5, ll.get(2))
        self.assertEqual(1, ll.get(3))
        ll.insert(7, 0)
        self.assertEqual(7, ll.get(0))
        self.assertEqual(4, ll.get(1))
        self.assertEqual(6, ll.get(2))
        self.assertEqual(5, ll.get(3))
        self.assertEqual(1, ll.get(4))

    def test_remove(self):
        ll = LinkedList()
        ll.add(1)
        ll.add(2)
        ll.add(3)
        ll.remove(1)
        self.assertEqual(3, ll.get(1))
        self.assertEqual(None, ll.get(2))
        ll.remove(0)
        self.assertEqual(3, ll.get(0))
        self.assertEqual(None, ll.get(1))
        ll.remove(0)
        self.assertEqual(None, ll.get(0))

    def test_iteration(self):
        ll = LinkedList()
        test_vals = [1, 2, 3]
        for v in test_vals:
            ll.add(v)
        for test_val, val in zip(test_vals, ll):
            self.assertEqual(test_val, val)

        ll.insert(0, 0)
        for test_val, val in zip([0] + test_vals, ll):
            self.assertEqual(test_val, val)

    def test_add_to_start(self):
        ll: LinkedList = LinkedList()
        vals = [0, 1, 2]
        for val in vals[::-1]:
            ll.add_to_start(val)
        for val in vals:
            self.assertEqual(val, ll.get(val))

    def test_remove_from_start(self):
        ll: LinkedList = LinkedList()
        vals = [0, 1, 2]
        for val in vals[::-1]:
            ll.add_to_start(val)
        for val in vals:
            self.assertEqual(val, ll.first())
            ll.remove_start()

    def test_len(self):
        ll: LinkedList = LinkedList()
        self.assertEqual(0, len(ll))
        vals = [0, 1, 2]
        for val in vals[::-1]:
            ll.add_to_start(val)
        self.assertEqual(len(vals), len(ll))


if __name__ == '__main__':
    unittest.main()
