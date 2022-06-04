from sys import stdin
from collections import defaultdict
input=stdin.readline

def dfs(x):
    if vi[x]:
        return False
    vi[x]=True
    for i in graph[x]:
        if rev[i]==-1 or dfs(rev[i]):
            rev[i]=x
            return True
    return False

n=int(input())
graph=[[] for i in range(n)]
rev=defaultdict(int)
sik=[]

for i in range(n):
    a,b=map(int,input().split())
    graph[i].append(a+b)
    graph[i].append(a-b)
    graph[i].append(a*b)
    sik.append([a,b])
    rev[a-b]=-1
    rev[a+b]=-1
    rev[a*b]=-1

cnt=0

for i in range(n):
    vi=[False]*n
    cnt+=dfs(i)

if cnt<n:
    print("impossible")
else:
    now=0
    for j in rev:
        for i in rev:
            if rev[i]==now:
                a,b=sik[rev[i]]
                if a+b==i:
                    print(f'{a} + {b} = {i}')
                elif a-b==i:
                    print(f'{a} - {b} = {i}')
                else:
                    print(f'{a} * {b} = {i}')
                now+=1
        
