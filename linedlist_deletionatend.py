#deletion at end
class node:
    def __init__(self,val=0): #constructor
        self.val=val
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def insertatend(self,data):
        if self.head==None:#creating 1st node
            self.head=node(data)
        else:
           curr=self.head
           while(curr.next):
               curr=curr.next
           new=node(data)
           curr.next=new

    def deleteatend(self):
        if self.head==None:
            return
        temp=self.head
        while(temp.next.next):
            temp=temp.next
        temp1=temp.next.val
        temp.next=None
        return temp1
        
        
    def printing(self):
        temp=self.head
        while(temp):
            print(temp.val,end="->")
            temp=temp.next
l=[2,4,6,8,9]
o=sll()
for i in l:
    o.insertatend(i)
o.printing()
print()

print(o.deleteatend())
print()






