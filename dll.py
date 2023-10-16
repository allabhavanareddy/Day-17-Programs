#double linked list
class node :
    def __init__(self,val=0):
        self.val=val
        self.next=None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
        self.tail=None
    def insertb(self,data):
        if self.head==None:
            self.head=node(data)
            self.tail=self.head
        else:
            new=node(data)
            new.next=self.head
            self.head.prev=new
            self.head=new

    def inserte(self,data):
        if self.head==None:
            self.head=node(data)
            self.tail=self.head
        else:
            new=node(data)
            self.tail.next=new
            new.prev=self.tail
            self.tail=new
    def deleteb(self):
        if self.head==None:
            return
        else:
            temp1=self.head
            self.head=self.head.next
            self.head.prev=None
        return temp1.val
    
    def deletee(self):
        if self.head==None:
            return
        else:
            temp1=self.tail
            self.tail=self.tail.prev
            self.tail.next=None
        return temp1.val

    def print(self):
        temp=self.head
        while(temp):
            print(temp.val,end="-->")
            temp=temp.next

ob=dll()
l=[1,2,3,4,5]
for i in l:
    ob.insertb(i)
    
l1=[100,200,300,400,500]
for j in l1:
    ob.inserte(j)
    
ob.print()
print()
print('delete at beginning:',ob.deleteb())
print('delete at end:',ob.deletee())
ob.print()