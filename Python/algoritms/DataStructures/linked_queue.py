from typing import Any
from typing_extensions import Iterator


class Node:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.next: Node | None = None

        def __repr__(self):
            return f"{self.data}"


class LinkedQueue:
    def __init__(self) -> None:
        self.front: None | Node = None
        self.rear: None | Node = None
        self.length: int = 0

    def __iter__(self) -> Iterator[Any]:
        node = self.front
        while node:
            yield node.data
            node = node.next

    def __len__(self) -> int:
        return self.length

    def __str__(self) -> str:
        return "<-".join(str(item) for item in self)

    def is_empty(self) -> bool:
        return len(self) == 0

    def put(self, item: Any) -> None:
        node = Node(item)
        if self.is_empty():
            self.length += 1
            self.front = self.rear = node
        else:
            assert isinstance(self.rear, Node)
            self.rear.next = node
            self.rear = node
            self.length += 1

    def get(self) -> Any:
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        assert isinstance(self.front, Node)
        node = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.length -= 1
        return node.data

    def clear(self) -> None:
        self.front = self.rear = None


if __name__ == "__main__":
    queue = LinkedQueue()
    queue.put("hola")
    queue.put("prueba")
    print(queue)
    queue.get()
    print(queue)
    queue.clear()
    print(queue)
