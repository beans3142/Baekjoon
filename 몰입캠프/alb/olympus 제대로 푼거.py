from sys import stdin,setrecursionlimit
from collections import *
input=stdin.readline
setrecursionlimit(1000000)

def dfs(x,a):
    rel[x]=a
    for i in graph[x]:
        dfs(i,a|(1<<(i-1)))

n,q=map(int,input().split())

par=[[0 for i in range(21)] for i in range(n+1)]
rel=[[] for i in range(n+1)]
graph=[[] for i in range(n+1)]
mygod=defaultdict(int)

for i in range(n):
    line=map(int,input().split())
    nowgod=next(line)
    eldergod=next(line)
    par[nowgod][0]=eldergod
    graph[eldergod].append(nowgod)
    for j in range(next(line)):
        mygod[next(line)]=nowgod


dfs(1,1)

for i in range(q):
    god,human=map(int,input().split())
    nowgod=mygod[human]
    if god!=nowgod:
        if not rel[nowgod]&(1<<(god-1)):
            print("Fail")
            continue
    print("Get")
    
