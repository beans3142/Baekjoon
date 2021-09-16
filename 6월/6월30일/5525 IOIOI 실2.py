#50점 짜리 코드
'''
n=int(input())
m=int(input())
p='I'+'OI'*n
s=input()
cnt=0
for i in range(m-len(p)):
    is_true=True
    for _ in range(len(p)):
        if s[i+_]!=p[_]:
            is_true=False
            break
    if is_true:
        cnt+=1
print(cnt)
'''
#여전히 50점..
'''
import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
m=int(input())
s=deque(list(input().rstrip()))
p=deque(list('I'+'OI'*n))
queue=deque([None]*len(p))
cnt=0
for i in range(m):
    queue.popleft()
    queue.append(s.popleft())
    if queue==p:
        cnt+=1

print(cnt)
'''
# 100점짜리 코드
n=int(input())
m=int(input())
p='I'+'OI'*n
s=input()
stack=0
cnt=0
for i in range(m):
    if stack%2:
        if s[i]=='O':
            stack+=1
        else:
            stack=1
    else:
        if s[i]=='I':
            stack+=1
            if stack==len(p):
                cnt+=1
                stack-=2
        else:
            stack=0
print(cnt)
