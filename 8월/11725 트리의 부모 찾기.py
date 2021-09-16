from sys import *
setrecursionlimit=1000000
from collections import defaultdict,deque
input=stdin.readline
tree=defaultdict(list)

n=int(input())
vi=[0]*(n+1)
vi[1]=1

for i in range(n-1):
    a,b=map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

queue=deque([[1,1]])

while queue:
    nxt,mom=queue.popleft()
    for i in tree[nxt]:
        if vi[i]==0:
            vi[i]=mom
            queue.append([i,i])

for i in range(2,n+1):
    print(vi[i])
