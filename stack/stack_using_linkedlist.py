class Node:
    def __int__(self, value=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        currnode = self.head
        while currnode:
            yield currnode
            currnode = currnode.next


class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return '\n'.join(values)

    def isEmpty(self):
        if self.LinkedList.head is None:
            return True
        else:
            return False

    def push(self, value):
        node = Node()
        node.value = value
        node.next = self.LinkedList.head
        self.LinkedList.head = node

    def pop(self):
        if self.isEmpty():
            print("Stack underflow")
        else:
            node = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return node

    def peak(self):
        if self.isEmpty():
            print("Stack underflow")
        else:
            node = self.LinkedList.head.value
            return node

    def delete(self):
        self.LinkedList.head = None


customStack = Stack()
print(customStack.isEmpty())
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)
print("_________")
print(customStack.pop())
print("_________")
print(customStack.peak())
