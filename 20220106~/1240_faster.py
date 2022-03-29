from sys import stdin
from collections import deque,defaultdict
from math import inf
input=stdin.readline

n,m=map(int,input().split()) # 값 입력 
tree={i:defaultdict(int) for i in range(1,n+1)}

for i in range(n-1):
    a,b,dist=map(int,input().split())
    tree[a][b]=tree[b][a]=dist

def bfs(start,end):
    queue=deque([(start,0)]) # 시작지와 누적 거리
    v=[0]*(n+1)
    while queue:
        now,totaldist=queue.popleft()
        if now==end:
            return totaldist
        for i in tree[now]:
            if v[i]==0:
                v[i]=1
                queue.append((i,totaldist+tree[now][i]))
                

for j in range(m):
    a,b=map(int,input().split())
    print(bfs(a,b))
