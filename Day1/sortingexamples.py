a=[2,5,7,9]
b=[1,3,6,7,10,13]
i=0
j=0
res=[]
while (i<len(a) and j<len(b)):
    if(a[i]<b[j]):
        res.append(a[i])
        i=i+1
    else:
        res.append(b[j])
        j=j+1
while (j<len(b)):
    res.append(b[j])
    j=j+1
while (i<len(a)):
    res.append(a[i])
    i=i+1
print(res)