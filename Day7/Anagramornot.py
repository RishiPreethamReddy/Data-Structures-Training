'''
Question:
school
3 queries
q1: L 2 --->hoolsc
q2: R 3 --->oolsch
q3: L 1 --->chools
hoc is the string and we need to check whether it is an anogram of any substring
for school(substrings:sch,cho,hoo,ool)
hoc is the anagram of cho so output is yes
'''
s=input()
sa=list(s)
sub=[]
anag=''.join(sorted([s[2],s[3],s[1]]))
for i in range(len(sa)):
    a=""
    for j in range(i,len(sa)):
        a+=sa[j]
        if len(a)==len(anag):
            sub.append(''.join(sorted(a)))
            a=""
if anag in set(sub):
    print('yes')
else:
    print('no')