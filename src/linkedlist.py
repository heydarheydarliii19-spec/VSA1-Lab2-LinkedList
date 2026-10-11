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
    def insert_after(self, target, data):
        current = self.head
        while current is not None:
            if current.data == target:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        print("Element tapılmadı.")
    def delete(self, value):
        if self.head is None:
            return
        if self.head.data == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next is not None:
            if current.next.data == value:
                current.next = current.next.next
                return
            current = current.next
        print("Element tapılmadı.")
    def search(self, value):
        current = self.head
        while current is not None:
            if current.data == value:
                print("Element tapıldı.")
                return True
            current = current.next
        print("Element tapılmadı.")
        return False
    def length(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count
    def max_min(self):
        if self.head is None:  # siyahı boşdursa
            return None, None
        maximum = self.head.data
        minimum = self.head.data
        current = self.head.next
        while current is not None:
            if current.data > maximum:
                maximum = current.data
            if current.data < minimum:
                minimum = current.data
            current = current.next
        return maximum, minimum
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

# Tapşırıq 4: test
print("Tapşırıq 4:")
list4 = SinglyLinkedList()
for x in [10, 20, 40]:
    list4.append(x)
list4.insert_after(20, 30)
list4.display()

# Tapşırıq 5: test
print("Tapşırıq 5:")
list5 = SinglyLinkedList()
for x in [10, 20, 30, 40, 50]:
    list5.append(x)
list5.delete(30)
list5.display()

# Tapşırıq 6: test
print("Tapşırıq 6:")
list6 = SinglyLinkedList()
for x in [10, 20, 30, 40]:
    list6.append(x)
list6.search(30)
list6.search(99)

# Tapşırıq 7: test
print("Tapşırıq 7:")
list7 = SinglyLinkedList()
for x in [11, 22, 33, 44, 55]:
    list7.append(x)
print("List length =", list7.length())

# Tapşırıq 8: test
print("Tapşırıq 8:")
list8 = SinglyLinkedList()
for x in [23, 8, 91, 15, 42]:
    list8.append(x)
maximum, minimum = list8.max_min()
print("Maksimum element =", maximum)
print("Minimum element =", minimum)
