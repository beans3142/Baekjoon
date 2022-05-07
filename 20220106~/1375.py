from sys import stdin
from collections import defaultdict,deque
input=stdin.readline

n,m=map(int,input().split())

graph=defaultdict(list)
group=[{}]
par=defaultdict(int)
groupno=0

for i in range(m):
    a,b=input().rstrip().split()
    graph[b].append(a)
    par[a]+=par[b]+1

for i in list(graph):
    if par[i]==0:
        dfs(i,0)
        groupno+=1
        group.append({})

q=int(input())

for i in range(q):
    a,b=input().rstrip().split()
    able=False
    if a==b:
        print('gg',end=' ')
        continue
    for j in group:
        if a in j and b in j:
            if j[a]>j[b]:
                able=True
                print(a,end=' ')
                break
            else:
                able=True
                print(b,end=' ')
                break
    if not able:
        print('gg',end=' ')

