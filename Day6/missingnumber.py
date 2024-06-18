n=int(input())
l=list(map(int,input().split()))
res=sum(l)
print((n*(n+1))//2-res)