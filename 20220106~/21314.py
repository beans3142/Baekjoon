from sys import stdin
input=stdin.readline

stack=[]

s=input().rstrip()

mx=[]
mn=[]

for i in range(len(s)):
    if s[i]=='K':
        mx.append(5*10**len(stack))
        stack=[]
    else:
        stack.append('M')
if stack:
    for i in range(len(stack)):
        mx.append(1)

stack=[]

for i in range(len(s)):
    if s[i]=='K':
        if stack:
            mn.append(10**(len(stack)-1))
        mn.append(5)
        stack=[]
    else:
        stack.append('M')

if stack:
    mn.append(1*10**(len(stack)-1))

print(*mx,sep='')
print(*mn,sep='')
