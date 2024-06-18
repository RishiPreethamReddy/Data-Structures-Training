#If number is prime then print prime else print next prime
'''a=int(input())
while(1):
    count=0
    for i in range(2,(a//2)+1):
        if (a % i== 0):
            count+=1
            break
    if(count==0):
        print(a)
        break
    else:
        a=a+1'''
#number of digits are prime
n=7854
count=0
while(n):
    if(n%10 in [2,3,5,7]):
        count=count+1
    n=n//10
print(count)