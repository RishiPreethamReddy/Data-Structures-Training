class node:
    def __init__(self,x):
        self.data=x
        self.left=None
        self.right=None
class tree:
    def __init__(self):
        self.root=None
    def add_element(self,curr,x):
        if curr is None:
            return node(x)
        else:
            if x>=curr.data:
                curr.right=self.add_element(curr.right,x)
            else:
                curr.left=self.add_element(curr.left,x)
        return curr
    def display_in(self,root):
        if root:
            self.display_in(root.left)
            print(root.data,end=" ")
            self.display_in(root.right)
    def display_pre(self,root):
        if root:
            print(root.data,end=" ")
            self.display_pre(root.left)
            self.display_pre(root.right)
    def display_post(self,root):
        if root: 
            self.display_post(root.left)
            self.display_post(root.right)
            print(root.data,end=" ")
    def top_view(self,root,count,l=[]):
        if(root==None):
            return
        if count not in l:
            print(root.data,end=" ")
            l.append(count)
        return(self.top_view(root.left,count-1,l))
        return(self.top_view(root.right,count+1,l))
    def right_view(self,root,count,l=[]):
        if(root==None):
            return
        if count not in l:
            print(root.data)

    def search(self,curr,x): 
        if curr is None:
            return False
        if curr.data==x:
            return True
        elif x<curr.data:
            return self.search(curr.left,x)
        else:
            return self.search(curr.right,x)
    def sumofnode(self,curr):
        if curr is None:
            return 0
        return curr.data + self.sumofnode(curr.left)+self.sumofnode(curr.right)
    def even_sum(self,curr):
        if curr is None:
            return 0
        if(curr.data%2==0):
            return curr.data + self.even_sum(curr.left)+self.even_sum(curr.right)
        else:
            return self.even_sum(curr.left)+self.even_sum(curr.right)
    def odd_sum(self,curr):
        if curr is None:
            return 0
        if(curr.data%2!=0):
            return curr.data + self.odd_sum(curr.left)+self.odd_sum(curr.right)
        else:
            return self.odd_sum(curr.left)+self.odd_sum(curr.right)
    '''def diff_sum(self,curr):
        if curr is None:
            return 0
        if(curr.data%2==0):
            evensum=curr.data + self.diff_sum(curr.left)+self.diff_sum(curr.right)
        if(curr.data%2!=0):
            oddsum=curr.data + self.diff_sum(curr.left)+self.diff_sum(curr.right)
        return self.diff_sum(evensum-oddsum)'''
    def height(self,curr):
        if curr is None:
            return -1
        return max(self.height(curr.left),self.height(curr.right))+1   
    def balanced(self,curr):
        if curr is None:
            return 
        return abs(self.balanced(curr.left) - self.balanced(curr.right)) <=1    
a=tree()
a.root=a.add_element(a.root,10)
a.root=a.add_element(a.root,40)
a.root=a.add_element(a.root,35)
a.display_in(a.root)
print()
a.display_pre(a.root)
print()
a.display_post(a.root)
print(a.search(a.root,10))
print(a.sumofnode(a.root))
print(a.even_sum(a.root))
print(a.odd_sum(a.root))
#print(a.diff_sum(a.root))
print(a.height(a.root))
if(a.balanced(a.root)):
    print("balanced")
else:
    print("Not balanced")

'''
inorder=1 5 6 7 8 10 20 25
pre order=10 5 1 7 6 8 20 25
post order=1 6 8 7 5 25 20 10 
'''