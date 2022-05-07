from sys import stdin
from collections import deque
input=stdin.readline

n=int(input())
deq=deque([])
for idx,i in enumerate(map(int,input().split())):
    deq.append((i,idx+1))
    
ans=[]
for i in range(n):
    now,idx=deq.popleft()
    ans.append(idx)
    if not deq:
        break
    for j in range(abs(now)-1):
        if now>0:
            deq.append(deq.popleft())
        else:
            deq.appendleft(deq.pop())
    if now<0:
        deq.appendleft(deq.pop())

print(*ans)
