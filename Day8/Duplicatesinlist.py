'''input [2,3,1,3,4,3,2,3]
output [[2,3,1,4],[3,2],[3]]'''
l=list(map(int,input().split()))
a=[]
c=0
while(c!=len(l)):
    r=[]
    for i in range(len(l)):
        if(not str(l[i]).isalpha()):
            if (l[i] not in r):
                c=c+1
                r.append(l[i])
                l[i]='a'
    a.append(r)
print(a)


