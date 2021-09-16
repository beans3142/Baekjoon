from sys import stdin
from collections import deque
input=stdin.readline
n=int(input())
tree={i:[]for i in range(1,n+1)}

for i in range(n-1):
    a,b,c=map(int,input().split())
    tree[a].append([b,c])
    tree[b].append([a,c])

def bfs(x):
    visited=[0]*(n+1)
    queue=deque([[x,0]])
    mx=-1
    far=1
    while queue:
        now,length=queue.popleft()
        if mx<length:
            far=now
            mx=length
        for i in tree[now]:
            if visited[i[0]]==0:
                visited[i[0]]=1
                queue.append([i[0],length+i[1]])
    return far,mx
if n>2:
    print(bfs(bfs(1)[0])[1])
else:
    if n==2:
        print(tree[1][0][1])
    else:
        print(0)

