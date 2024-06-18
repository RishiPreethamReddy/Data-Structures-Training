a=[1,1,1,2,2,2,1,2]
count=1
present=a[0]
for i in range(1,len(a)):
    if(a[i]==present):
        count=count+1
    else:
        count=count-1
        if(count==0):
            count=count+1
            present=a[i]
print(present)
