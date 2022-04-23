from sys import stdin
from collections import deque
input=stdin.readline

inf=float('inf')

f,s,g,u,d=map(int,input().split())

building=[inf]*(f+1)

queue=deque([s])
building[s]=0

while queue:
    now=queue.popleft()
    if now==g:
        print(building[g])
        exit()
    if now+u<=f and building[now+u]==inf:
        building[now+u]=building[now]+1
        queue.append(now+u)
    if now-d>0 and building[now-d]==inf:
        building[now-d]=building[now]+1
        queue.append(now-d)

print('use the stairs')
