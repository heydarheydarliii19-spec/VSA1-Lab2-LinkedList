class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None  # siyahı əvvəlcə boşdur

    def append(self, data):
        """Siyahının sonuna yeni element əlavə edir."""
        new_node = Node(data)
        if self.head is None:  # siyahı boşdursa
            self.head = new_node
            return
        current = self.head
        while current.next is not None:  # sonuncu düyünü tap
            current = current.next
        current.next = new_node

    def display(self):
        """Siyahını 10 -> 20 -> None formatında çap edir."""
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
