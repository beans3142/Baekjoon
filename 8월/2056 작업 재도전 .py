from collections import defaultdict, deque
from sys import stdin
input=stdin.readline

n=int(input())

dp=[0]*n
depth=[0]*n
works=defaultdict(list)
time=[0]*n

for i in range(n):
    work=list(map(int,input().split()))
    time[i]=work[0]
    depth[i]=work[1]
    for j in range(work[1]):
        works[work[2+j]-1].append(i)
    
queue=deque([])

for i in range(n):
    if depth[i]==0:
        queue.append(i)
        dp[i]=time[i]

while queue:
    now=queue.popleft()
    for i in works[now]:
        depth[i]-=1
        dp[i]=max(dp[i],dp[now]+time[i])
        if depth[i]==0:
            queue.append(i)

print(max(dp))
