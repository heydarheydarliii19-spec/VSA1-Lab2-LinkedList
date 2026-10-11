class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
#Tapşırıq 1:
print("Tapşırıq 1:")
node = Node(15)
print(node.data)
print(node.next)
        
#Tapşırıq 2: test
print("Tapşırıq 2:")
my_list = SinglyLinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.display()

#Tapşırıq 3:
print("Tapşırıq 3:")
list3 = SinglyLinkedList()
for x in [20, 30, 40]:
    list3.append(x)
list3.prepend(10)
list3.display()
