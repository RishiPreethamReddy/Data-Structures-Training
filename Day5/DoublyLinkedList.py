class node:
    def __init__(self,u):
        self.data=u
        self.prev=None
        self.nxt=None
class dll:
    def __init__(self):
        self.head=None
        self.tail=None
    def addback(self,x):
        if(self.head==None):
            self.head=node(x)
            self.tail=self.head
        else:
            t=node(x)
            self.tail.nxt=t
            t.prev=self.tail
            self.tail=self.tail.nxt
    def addfront(self,x):
        if(self.head==None):
            self.head=node(x)
            self.tail=self.head
        else:
            t=node(x)
            t.nxt=self.head
            self.head.prev=t
            self.head=t
    def display(self):
        t=self.head
        while(t!=None):
            print(t.data,end="<=>")
            t=t.nxt
        print()
    def rev_display(self):
        t=self.tail
        while(t!=None):
            print(t.data,end="<=>")
            t=t.prev
        print()
    def linear_search(self,target):
        t=self.head
        while t:
            if t.data==target:
                return t
            t=t.nxt
        return None
    def evod(self,t,evensum,oddsum):
        if(t==None):
            return abs(evensum-oddsum)
        if(t.data%2==0):
            evensum=evensum+t.data
        else:
            oddsum=oddsum+t.data
        return self.evod(t.nxt,evensum,oddsum)
l1=dll()
l1.addback(7)
l1.addfront(5)
l1.addback(8)
l1.addback(9)
l1.addfront(3)
l1.addback(10)
l1.addback(12)
l1.addback(15)
l1.display()
l1.rev_display()
result=l1.linear_search(10)
if result:
    print("Found")
else:
    print("Not found")
print(l1.evod(l1.head,0,0))