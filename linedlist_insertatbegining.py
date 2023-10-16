'''class node:
    def __init__(self,val=0):
        self.val=val
        self.next=None
def insertatbeg(head,data):
    pass
l=[2,4,6,8,9]
head=node(l[0])'''

# insertion at begining
class node:
    def __init__(self,val=0): #constructor
        self.val=val
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def insertatbeg(self,data):
        if self.head==None:
            self.head=node(data)
        else:
            new=node(data)
            new.next=self.head
            self.head=new
    def printing(self):
        temp=self.head
        while(temp.next):
            print(temp.val)
            temp=temp.next
l=[2,4,6,8,9]
o=sll()
for i in l:
    o.insertatbeg(i)
o.printing()
    