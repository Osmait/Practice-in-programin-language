class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"


class LinkedList:

    def __init__(self):
        self.head: Node | None = None
        self.length = 0

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __len__(self):
        return self.length

    def __repr__(self):
        return "->".join(str(node) for node in self)

    def __getitem__(self, index):

        if not 0 <= index < len(self):
            raise IndexError("Index out of range")

        for i, node in enumerate(self):
            if i == index:
                return node
        return None

    def __setitem__(self, index, data):
        if not 0 <= index < len(self):
            raise IndexError("Index out of range")
        current: Node | None = self.head
        for _ in range(index):
            current = current.next
        current.data = data

    def insert_head(self, data):
        self.insert_nth(0, data)

    def insert_nth(self, index, data):
        if not 0 <= index <= len(self):
            raise IndexError("Index out of range")
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node

    def print_list(self):
        print(self)

    def delete_head(self):
        return self.delete_nth(0)

    def delete_tail(self):
        return self.delete_nth(len(self) - 1)

    def delete_nth(self, index):
        if not 0 <= index < len(self):
            raise IndexError("Index out of range")
        deleted_node = self.head
        if index == 0:
            self.head = self.head.next
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            deleted_node = temp.next
            temp.next = temp.next.next

        return deleted_node

    def is_empty(self):
        return self.head is None

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev


if __name__ == "__main__":
    linkedList = LinkedList()
    linkedList.insert_head(1)
    linkedList.insert_head(2)

    print(len(linkedList))
    print(linkedList)
    print(linkedList.insert_head(5))

    print(linkedList)
