from sys import stdin
from collections import deque
input=stdin.readline

n,k=map(int,input().split())
villages=[0]*(n+1)
villages[k]=1
queue=deque([k])

while queue:
    now=queue.popleft()
    if now//3>0:
        if villages[now//3]==0:
            villages[now//3]=1
            queue.append(now//3)
    if now*2<=n:
        if villages[now*2]==0:
            villages[now*2]=1
            queue.append(now*2)

print(n-sum(villages))
