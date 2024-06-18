#Using Loops
'''l=list(map(int,input().split()))
for i in range(len(l)):
    for j in range(i+1,len(l)):
        for k in range(j+1,len(l)):
            print((l[i], l[j], l[k]))'''
#Using Recursion
def combination(l,k):
    def fun(curr,start):
        if len(curr)==k:
            print(curr)
            return
        for i in range(start,len(l)):
            fun(curr+[l[i]],i+1)
        return
    fun([],0)
a=list(map(int,input().split()))
k=3
combination(a,k)


