"""
UMass ECE 241   -   Advanced Programming
Homework #3     -   Fall 2019
hw3_q1_2019.py      -   Double-linked list
Complete the following methods in the code below!
search()
add()
size()
remove()
"""

class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None
        self.prev = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def getPrev(self):
        return self.prev

    def setData(self,newdata):
        self.data = newdata

    def setPrev(self, newprev):
        self.prev = newprev

    def setNext(self,newnext):
        self.next = newnext


class OrderedDLList:
    def __init__(self):
        self.head = None
        self.tail = None

    def search(self, item):
        current = self.head
        index = 1
        while current != None:
            if current.data == item:
                return index #return index once current is equal to the desired item
            current = current.next
            index += 1 #search the one with the index one greater if conditional statement not met
        return None

    def add(self, item):
        new = Node(item)
        if self.head == None:
            self.head = new #sets item as head if it is the only item
        elif self.head.data > new.data:
            new.setNext(self.head)
            self.head.setPrev(new)
            self.head = new # new item becomes head if smallest
        else: #occurs if somewhere else in list
            previous = self.head
            current = self.head.next
            while current != None: #as pointer stays in the list...
                if current.data > new.data: #switches places if new item is greater than the compared number
                    previous.setNext(new)
                    new.setPrev(previous)
                    new.setNext(current)
                    current.setPrev(new)
                    self.tail = current.next
                    return new
                previous = current
                current = current.next
            previous.setNext(new)
            new.setPrev(previous)
            return new

    def isEmpty(self):
        return self.head == None

    def size(self):
        size = 0 # initialize size variable
        current = self.head.next_node
        while current != None and current != self.tail:
            size += 1 #adds 1 to size variable if current is not at the end of list
            current = current.next_node
        return size

    def remove(self, item):
        if self.head.data == item: #if removed item is first in list
            self.head = self.head.next
            self.head.prev = None # removes prior link
        else:
            previous = self.head
            current = previous.next
            while current != None: #continues as long as the current value is inthe list
                if current.data == item:
                    if current.next == None:
                        previous.setNext(None)
                        if self.tail.data == item: #reassigns tail value if it was deleted
                            self.tail = self.tail.prev

                    else:
                        previous.setNext(current.next)
                        current.next.setPrev(previous)
                    return True
                previous = current # checks next number in list
                current = current.next
            return False

    def printList(self):
        current = self.head
        while current != None:
            print(current.getData())
            current = current.getNext()

    def printRevList(self):
        current = self.tail
        while current != None:
            print(current.getData())
            current = current.getPrev()

mylist = OrderedDLList()
mylist.add(10)
mylist.add(15)
mylist.add(20)
mylist.add(11)

print(mylist.search(11))

mylist.printList()
print()
mylist.printRevList()

mylist.remove(20)
print()
mylist.printList()
print()
mylist.printRevList()