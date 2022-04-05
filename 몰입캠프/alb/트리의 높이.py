# 어떤 방식이든 그래프 탐색 알고리즘을 이용하면 된다.

from sys import stdin
from collections import deque,defaultdict
input=stdin.readline

n,r=map(int,input().split())
visited=[0]*n
tree=defaultdict(list)

for i in range(n-1):
    a,b=map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)


queue=deque([(r,0)])
while queue:
    now,depth=queue.popleft()
    visited[now]=1
    for i in tree[now]:
        if visited[i]==1:
            continue
        queue.append((i,depth+1))

print(depth)
