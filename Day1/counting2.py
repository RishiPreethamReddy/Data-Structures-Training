a=[3,5,4,3,6,7,1,2,4,3,3,7,6,8,8]
b={}
for i in a:
    if i not in b:
        b[i]=1
    else:
        b[i]+=1
print(b)