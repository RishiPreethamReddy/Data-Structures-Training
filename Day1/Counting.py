a="aaabbaaaaddd"
c=1
b=''
for i in range(len(a)-1):
    if(a[i]==a[i+1]):
        c=c+1
    else:
        b=b+a[i]+str(c)
        c=1
b=b+a[i]+str(c)
print(b)