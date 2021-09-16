# 1차 존나 안좋은 풀이, 100

'''
s=list(input())

n=0
r=0
j=0

for i in range(len(s)):
    if n<=0:
        if s[i]==')':
            r+=1
        else:
            n+=1
            j=1
    elif n>0:
        if s[i]=='(':
            j+=1
            n+=j
        else:
            j-=1
            n-=j+1

print(r+j)
'''
# 개선 100->64 m/s

'''
l=input()
n=0
o=0

for i in range(len(l)):
    if l[i]=='(':
        n+=1
        o+=1
        continue
    if o>0:
        if l[i]==')':
            n-=1
            o-=1
            continue
    n+=1

print(n)
'''

l=input()
arr=[]
n=0

for i in range(len(l)):
    if l[i]=='(':
        arr.append(l[i])
    elif arr and l[i]==')':
        arr.pop()
    else:
        n+=1

print(n+len(arr))
        
