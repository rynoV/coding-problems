from typing import TypeVar, Generic, Optional, Iterator, Iterable
from copy import copy

T = TypeVar('T')


class Node(Generic[T]):
    value: T

    def __init__(self, value: T = None):
        self.value = value
        self.next_node: self = None

    def __str__(self):
        return f'Value: {self.value}, Next Node: {self.next_node}'


class LinkedList(Generic[T], Iterable[T]):
    _head: Node[T]

    def __init__(self):
        self._head = None

    def last(self) -> Optional[T]:
        return self._last().value

    def first(self) -> Optional[T]:
        return None if self._head is None else self._head.value

    def add(self, value: T) -> None:
        if self._head is None:
            self._head = Node(value)
        else:
            node = self._last()
            node.next_node = Node(value)

    def add_to_start(self, value: T) -> None:
        new_node = Node(value)
        new_node.next_node = self._head
        self._head = new_node

    def remove_start(self) -> None:
        self._head = self._head.next_node

    def remove(self, index: int) -> None:
        if index < 0:
            raise IndexError()

        if index == 0:
            if self._head is not None:
                self._head = self._head.next_node
                return
            else:
                raise IndexError()

        for i, node in enumerate(self._node_iterator()):
            if i + 1 == index:
                to_remove = node.next_node
                if to_remove is None:
                    raise IndexError()
                else:
                    node.next_node = to_remove.next_node
                    return
            elif i > index:
                raise IndexError()

    def insert(self, value: T, index: int) -> None:
        if index < 0:
            raise IndexError()

        for i, node in enumerate(self._node_iterator()):
            if i == index:
                copied = copy(node)
                node.value = value
                node.next_node = copied
                return
            elif i > index:
                raise IndexError()

    def update(self, value: T, index: int) -> None:
        if index < 0:
            raise IndexError()

        for i, node in enumerate(self._node_iterator()):
            if i == index:
                node.value = value
                return
            elif i > index:
                raise IndexError()

    def get(self, index: int) -> Optional[T]:
        for i, value in enumerate(self._value_iterator()):
            if i == index:
                return value
            elif i > index:
                return None

    def __str__(self):
        s = []
        for value in self:
            s.append(str(value))

        return ', '.join(s)

    def __iter__(self) -> Iterator[T]:
        return self._value_iterator()

    def __len__(self) -> int:
        i = 0
        for _ in self:
            i += 1
        return i

    def _value_iterator(self) -> Iterator[T]:
        return (node.value for node in self._node_iterator())

    def _node_iterator(self) -> Iterator[Node[T]]:
        node = self._head
        while node is not None:
            yield node
            node = node.next_node

    def _last(self) -> Optional[Node[T]]:
        for n in self._node_iterator():
            ...
        return n
