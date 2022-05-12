from sys import stdin
from collections import deque
input=stdin.readline

n=int(input())
tree=[[] for i in range(n+1)]

for i in range(n-1):
    a,b=map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

queue=deque([(1,0)])
vi=[0]*(n+1)
vi[1]=1
cnt=0

while queue:
    now,dist=queue.popleft()
    pushed=False
    for i in tree[now]:
        if vi[i]==0:
            pushed=True
            vi[i]=1
            queue.append([i,dist+1])
    if not pushed:
        cnt+=dist

if cnt%2==1:
    print('Yes')
else:
    print('No')
