from sys import stdin
from collections import *
input=stdin.readline

log=21

n,q=map(int,input().split())

par=[[0 for i in range(21)] for i in range(n+1)]
depth=[-1]*(n+1)
mygod=defaultdict(int)
graph=[[] for i in range(n+1)]

for i in range(n):
    line=map(int,input().split())
    nowgod=next(line)
    eldergod=next(line)
    par[nowgod][0]=eldergod
    graph[eldergod].append(nowgod)
    for j in range(next(line)):
        mygod[next(line)]=nowgod

queue=deque([1])
depth[1]=0
while queue:
    now=queue.popleft()
    for i in graph[now]:
        depth[i]=depth[now]+1
        queue.append(i)

for i in range(1,21):
    for j in range(1,n+1):
        par[j][i]=par[par[j][i-1]][i-1]

def lca(a,b):
    if depth[a]>depth[b]:
        return False
    for i in range(log-1,-1,-1):
        if depth[b]-depth[a]>=(1<<i):
            b=par[b][i]
    if a==b:
        return a
    for i in range(log-1,-1,-1):
        if par[a][i]!=par[b][i]:
            a=par[a][i]
            b=par[b][i]
    return par[a][0]


for i in range(q):
    god,human=map(int,input().split())
    nowgod=mygod[human]
    if god!=nowgod:
        able=lca(god,nowgod)
        if able!=god:
            print("Fail")
            continue
    print("Get")
    
