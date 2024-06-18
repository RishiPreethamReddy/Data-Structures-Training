a=list(map(int,input().split()))
for i in range(len(a)-2):
    s=a[i] + a[i+1] + a[i+2]
    a[i]=min(a[i],a[i+1],a[i+2])
    a[i+2]=max(a[i],a[i+1],a[i+2]) 
    a[i+1]=s-a[i]-a[i+2]
print(a)

''' Input: 4 9 8 2 14 3 5 6
    Output [4,2,8,3,5,6,9,14]'''