from typing import TypeVar, Generic, Iterator

T = TypeVar('T')


class BSTNode(Generic[T]):
    data: T

    def __init__(self, data: T, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        leaf = self.left is None and self.right is None
        children = "(Leaf)" if leaf else f"\nLeft: {self.left}\nRight: {self.right}"
        return f'\n\tData: {self.data} {children}'


class BinarySearchTree(Generic[T]):
    _root: BSTNode[T]

    def __init__(self):
        self._root = None

    def __str__(self):
        return f'Root: {self._root}'

    def add(self, data: T) -> None:
        if self._root is None:
            self._root = BSTNode(data)
        else:
            self._add(data, self._root)

    def _add(self, data: T, node: BSTNode[T]):
        if data <= node.data:
            if node.left is None:
                node.left = BSTNode(data)
            else:
                self._add(data, node.left)
        else:
            if node.right is None:
                node.right = BSTNode(data)
            else:
                self._add(data, node.right)

    def __iter__(self) -> Iterator[T]:
        """In order traversal"""
        return self.in_order_iterator()

    def in_order_iterator(self) -> Iterator[T]:
        """
        In order traversal
        """
        return self._in_order_iterator(self._root)

    def _in_order_iterator(self, node: BSTNode[T]) -> Iterator[T]:
        if node is not None:
            yield from self._in_order_iterator(node.left)
            yield node.data
            yield from self._in_order_iterator(node.right)

    def pre_order_iterator(self) -> Iterator[T]:
        """
        Pre order traversal
        """
        return self._pre_order_iterator(self._root)

    def _pre_order_iterator(self, node: BSTNode[T]) -> Iterator[T]:
        if node is not None:
            yield node.data
            yield from self._pre_order_iterator(node.left)
            yield from self._pre_order_iterator(node.right)

    def post_order_iterator(self) -> Iterator[T]:
        """
        Post order traversal
        """
        return self._post_order_iterator(self._root)

    def _post_order_iterator(self, node: BSTNode[T]) -> Iterator[T]:
        if node is not None:
            yield from self._post_order_iterator(node.left)
            yield from self._post_order_iterator(node.right)
            yield node.data
