def sum1(l):
    if(len(l)==0):
        return 0
    if(len(l)==1):
        return l[0]
    if(len(l)==2):
        return max(l)
    le=l[0]+sum1(l[2:])
    ri=l[1]+sum1(l[3:])
    return max(le,ri)
arr=[13,9,4,10,5,7]
print(sum1(arr))

