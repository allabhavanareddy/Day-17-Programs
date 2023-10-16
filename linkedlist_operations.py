class node:
    def _init_(self,z):
        self.data=z;
        self.next=None
class list:
    def _init_(self):
        self.head=None
    def creat(self,x):
        if(self.head==None):
            self.head=node(x)
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=node(x)
    def add_front(self,x):
        if(self.head==None):
            self.head=node(x)
        else:
            temp=node(x)
            temp.next=self.head
            self.head=temp
    def add_end(self,x):
        if(self.head==None):
            self.head=node(x)
        else:
            curr=self.head
            while(curr.next):
                curr=curr.next
            temp=node(x)
            curr.next=temp
    def delete_beg(self):
        if self.head==None:
            return
        temp=self.head
        self.head=self.head.next
        temp.next=None
        return temp.data
    def delete_end(self):
        if self.head==None:
            return
        temp=self.head
        while(temp.next.next):
            temp=temp.next
        temp.next=None
        return temp.data
    def traversal(self):
        temp=self.head
        while(temp):
            print(temp.data,end="-->")
            temp=temp.next
a=list()
a.creat(10)
a.creat(20)
a.creat(30)
a.add_front(70)
a.add_end(25)
a.delete_end()
a.delete_beg()
a.traversal()
class node:
    def _init_(self,z):
        self.data=z;
        self.next=None
class list:
    def _init_(self):
        self.head=None
    def creat(self,x):
        if(self.head==None):
            self.head=node(x)
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=node(x)
    def add_front(self,x):
        if(self.head==None):
            self.head=node(x)
        else:
            temp=node(x)
            temp.next=self.head
            self.head=temp
    def add_end(self,x):
        if(self.head==None):
            self.head=node(x)
        else:
            curr=self.head
            while(curr.next):
                curr=curr.next
            temp=node(x)
            curr.next=temp
    def delete_beg(self):
        if self.head==None:
            return
        temp=self.head
        self.head=self.head.next
        temp.next=None
        return temp.data
    def delete_end(self):
        if self.head==None:
            return
        temp=self.head
        while(temp.next.next):
            temp=temp.next
        temp.next=None
        return temp.data
    def traversal(self):
        temp=self.head
        while(temp):
            print(temp.data,end="-->")
            temp=temp.next
a=list()
a.creat(10)
a.creat(20)
a.creat(30)
a.add_front(70)
a.add_end(25)
a.delete_end()
a.delete_beg()
a.traversal()
class node:
    def _init_(self,z):
        self.data=z;
        self.next=None
class list:
    def _init_(self):
        self.head=None
    def creat(self,x):
        if(self.head==None):
            self.head=node(x)
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=node(x)
    def add_front(self,x):
        if(self.head==None):
            self.head=node(x)
        else:
            temp=node(x)
            temp.next=self.head
            self.head=temp
    def add_end(self,x):
        if(self.head==None):
            self.head=node(x)
        else:
            curr=self.head
            while(curr.next):
                curr=curr.next
            temp=node(x)
            curr.next=temp
    def delete_beg(self):
        if self.head==None:
            return
        temp=self.head
        self.head=self.head.next
        temp.next=None
        return temp.data
    def delete_end(self):
        if self.head==None:
            return
        temp=self.head
        while(temp.next.next):
            temp=temp.next
        temp.next=None
        return temp.data
    def traversal(self):
        temp=self.head
        while(temp):
            print(temp.data,end="-->")
            temp=temp.next
a=list()
a.creat(10)
a.creat(20)
a.creat(30)
a.add_front(70)
a.add_end(25)
a.delete_end()
a.delete_beg()
a.traversal()