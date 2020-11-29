from typing import TypeVar, Generic
from linked_list import LinkedList

T = TypeVar('T')


class Queue(Generic[T]):
    _queue: LinkedList[T]

    def __init__(self):
        self._queue = LinkedList()

    def remove(self) -> T:
        """
        Remove and return the first item from the queue.
        """
        top = self._queue.first()
        self._queue.remove_start()
        return top

    def add(self, data: T):
        """
        Add an item to the end of the queue.
        """
        self._queue.add(data)

    def peek(self) -> T:
        """
        Return the first item of the queue.
        """
        return self._queue.first()

    def isEmpty(self):
        """
        Return true if and only if the queue is empty.
        """
        return len(self._queue) == 0
