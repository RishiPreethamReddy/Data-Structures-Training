s1="tu5g2kk1h8"
s2="g5g8gd6h3"
s=[]
j=0
minn=9999
for i in s1+s2:
    if i.isdigit():
        if int(i) not in s:
            s.append(int(i))
            j+=1
            if int(i)%2==0 and int(i)<minn:
                minn=int(i)
res=""
s.remove(minn)
s.sort(reverse=True)
for i in s:
    res+=str(i)
print(res+str(minn))