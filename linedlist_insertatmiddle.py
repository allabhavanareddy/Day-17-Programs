# linkedlist to insert element at middle

class node:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class sll:
    def __init__(self):
        self.head = None

    def insertatbeg(self, data):
        if self.head is None:
            self.head = node(data)
        else:
            new = node(data)
            new.next = self.head
            self.head = new

    def insertatmid(self, data, position):
        if position < 0:
            print("Invalid position")
            return
        if position == 0:
            self.insertatbeg(data)
            return
        new_node = node(data)
        current = self.head
        count = 0
        while count < position - 1 and current is not None:
            current = current.next
            count += 1
        if current is None:
            print("Position is out of range")
            return
        new_node.next = current.next
        current.next = new_node

    def printing(self):
        temp = self.head
        while temp:
            print(temp.val)
            temp = temp.next

l = [2, 4, 6, 8, 9]
o = sll()
for i in l:
    o.insertatbeg(i)
# Insert 5 at position 2 (0-based index)
o.insertatmid(5, 4)
o.printing()
