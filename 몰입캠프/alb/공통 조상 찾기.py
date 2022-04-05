from sys import stdin
from collections import deque,defaultdict
input=stdin.readline

n,x,y=map(int,input().split())
tree=defaultdict(int)
for i in range(n-1):
    a,b=map(int,input().split())
    tree[b]=a
tree[0]=-1


def bfs(x):
    vi=[10000]*n
    queue=deque([(x,0)])
    while queue:
        now,depth=queue.popleft()
        vi[now]=depth
        if tree[now]!=-1:
            queue.append((tree[now],depth+1))
    return vi

xAnc=bfs(x)
yAnc=bfs(y)
mn=1001
mnidx=0
for i in range(n):
    val=xAnc[i]+yAnc[i]
    if val<mn:
        mnidx=i
        mn=val

print(mnidx)
