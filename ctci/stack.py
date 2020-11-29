from typing import TypeVar, Generic
from linked_list import LinkedList

T = TypeVar('T')


class Stack(Generic[T]):
    _stack: LinkedList[T]

    def __init__(self):
        self._stack = LinkedList()

    def pop(self) -> T:
        """
        Remove and return the top item from the stack.
        """
        top = self._stack.first()
        self._stack.remove_start()
        return top

    def push(self, data: T):
        """
        Add an item to the top of the stack.
        """
        self._stack.add_to_start(data)

    def peek(self) -> T:
        """
        Return the top of the stack.
        """
        return self._stack.first()

    def isEmpty(self):
        """
        Return true if and only if the stack is empty.
        """
        return len(self._stack) == 0
