'''s=input()
open_braces=['[','{','(']
closed_braces=[']','}',')']
braces={'}':'{',']':'[',')':'('}
stack=[]
for char in s:
    if char in open_braces:
        stack.append(char)
    elif char in closed_braces:
        if not stack or braces[char]!=stack.pop():
            print("False)
print(len(stack)==0)'''
a=input()
s=[]
count=0
f=0
for i in a:
    if(i in '{[('):
        s.append(i)
    elif(not s):
        if(i == '}' and s[-1]=='{' or i == ']' and s[-1]=='[' or i == ')' and s[-1]=='('):
            s.pop()
        else:
            print(count)
            f=1
            break
    else:
        print(count)
        f=1
        break
count=count+1




