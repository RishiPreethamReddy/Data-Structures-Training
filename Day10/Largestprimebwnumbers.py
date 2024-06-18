def isprime(x):
    for i in range(2,(x//2)+1):
        if(x%i==0):
            return 0
    return 1

def lprime(n,m):
    for i in range(m-1,n,-1):
        if(isprime(i)):
            return i
    return  0

a=list(map(int,input().split()))
s=0
for i in range(len(a)-1):
    s=s+lprime(a[i],a[i+1])
print(s)

#Input: 4 9 8 2 14 3 5 6
#output 20