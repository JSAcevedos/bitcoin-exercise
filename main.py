#Implementación de los nodos
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#Implementación de la lista enlazada
class linkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def pushback(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def popback(self):
        if self.tail is None:
            print("ERROR: Empty list")
        else:
            current_node = self.head
            while current_node.next.next:
                current_node = current_node.next
            temp = current_node.data
            current_node.next = None
            self.tail = current_node
            return temp


    def print(self):
        if self.head is None:
            print("ERROR: Empty list")
        else:
            current_node = self.head
            while current_node is not None:
                if current_node.next is None:
                    print(current_node.data, end="")
                else:
                    print(current_node.data, end=" ")
                current_node = current_node.next

inputs = input().split()
values = linkedList()
days = linkedList()

for i in inputs:
    values.pushback(int(i))

while values.head:
    day = 0
    temp = values.head.next
    while temp:
        if values.head.data < temp.data:
            day += 1
            break
        else:
            day += 1
        if temp.next is None:
            day = 0
        temp = temp.next
    days.pushback(day)
    values.head = values.head.next

days.print()