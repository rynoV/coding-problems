from typing import Generic, Iterator, List, NewType, Optional, Tuple, TypeVar
from linked_list import LinkedList

K = TypeVar('K')
V = TypeVar('V')


class KeyValuePair(Generic[K, V]):
    def __init__(self, key: K, value: V):
        self.key = key
        self.value = value


KeyValuePairs = LinkedList[KeyValuePair[K, V]]


class HashTable(Generic[K, V]):
    _capacity: int
    _size: int
    _data: List[KeyValuePairs]

    def __init__(self):
        self._capacity = 100
        self._size = 0
        self._data = [None] * self._capacity

    def put(self, key: K, value: V) -> None:
        kv_pairs = self._get_key_value_pairs(key)
        for kv_pair in kv_pairs:
            if kv_pair.key == key:
                kv_pair.value = value
                return

        kv_pairs.add_to_start(KeyValuePair(key, value))
        self._size += 1

    def remove(self, key: K) -> None:
        kv_pairs = self._get_key_value_pairs(key)
        for i, kv_pair in enumerate(kv_pairs):
            if kv_pair.key == key:
                kv_pairs.remove(i)
                self._size -= 1
                return

    def get(self, key: K) -> Optional[V]:
        kv_pairs = self._get_key_value_pairs(key)
        for kv_pair in kv_pairs:
            if kv_pair.key == key:
                return kv_pair.value

    def size(self):
        return self._size

    def _get_key_value_pairs(self, key: K) -> KeyValuePairs:
        return self._get_at_index(self._compute_index(key))

    def _get_at_index(self, index: int) -> KeyValuePairs:
        kv_pairs = self._data[index]
        if kv_pairs is None:
            self._data[index] = LinkedList()
        return self._data[index]

    def _compute_index(self, key: K) -> int:
        return hash(key) % self._capacity
