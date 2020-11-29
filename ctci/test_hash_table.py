import unittest
from hash_table import HashTable


class TestHashTable(unittest.TestCase):
    def test_put(self):
        hash_table = HashTable()
        hash_table.put('key', 2)
        self.assertEqual(2, hash_table.get('key'))
        self.assertEqual(1, hash_table.size())
        hash_table.put('key2', 3)
        self.assertEqual(3, hash_table.get('key2'))
        self.assertEqual(2, hash_table.size())

    def test_replace(self):
        hash_table = HashTable()
        key = 'key'
        hash_table.put(key, 2)
        hash_table.put(key, 3)
        self.assertEqual(3, hash_table.get(key))
        self.assertEqual(1, hash_table.size())

    def test_remove(self):
        hash_table = HashTable()
        hash_table.put('key', 2)
        hash_table.put('key1', 3)
        hash_table.remove('key')
        self.assertEqual(1, hash_table.size())
        self.assertEqual(None, hash_table.get('key'))


if __name__ == '__main__':
    unittest.main()
