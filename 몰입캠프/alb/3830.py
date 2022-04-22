from sys import *
from collections import defaultdict,deque
setrecursionlimit(100000)
input=stdin.readline

inf=float('inf')

def bfs(x):
    queue=deque([(x,0)])
    vi[x]=now
    while queue:
        nowat,dist=queue.popleft()
        w[x][nowat]=dist
        w[nowat][x]=-dist
        if nowat==n2:
            return dist
        for i in w[nowat]:
            if vi[i]<now:
                vi[i]=now
                queue.append((i,dist+w[nowat][i]))

def find(x):
    global dist
    if par[x]==x:
        return x

    p=find(par[x])

    dist[x]+=dist[par[x]]

    par[x]=p

    return par[x]

def union(a,b,c):

    aa=find(a)
    bb=find(b)
    
    if aa!=bb:
        dist[bb]=dist[a]-dist[b]+c
        par[bb]=aa
    
    


while True:
    n,m=map(int,input().split())
    
    if n==m==0:
        break
    now=0
    par=[i for i in range(n+1)]
    w=[{} for i in range(n+1)]
    dist=[0]*(n+1)
    for i in range(m):
        a,*b=input().split()
        if a=='!':
            union(int(b[0]),int(b[1]),int(b[2]))
        else:
            n1=int(b[0])
            n2=int(b[1])
            p1=find(n1)
            p2=find(n2)
            if p1==p2:
                print(dist[n2]-dist[n1])
            else:
                print('UNKNOWN')
        
