n=int(input())
if str(n)==str(n)[::-1]:
    print("Palindrome")
else:
    while True:
        n+=1
        if str(n)==str(n)[::-1]:
            print(n)
            break