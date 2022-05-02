from sys import stdin,setrecursionlimit
from collections import defaultdict
setrecursionlimit(500000)
input=stdin.readline

def dfs(x):
    global time
    inout[x][0]=time
    time+=1
    for i in graph[x]:
        dfs(i)
    inout[x][1]=time
    time+=1

n,q=map(int,input().split())

time=1
inout=[[0]*2 for i in range(n+1)]
graph=[[] for i in range(n+1)]
mygod=defaultdict(int)

for i in range(n):
    line=map(int,input().split())
    nowgod=next(line)
    eldergod=next(line)
    graph[eldergod].append(nowgod)
    for j in range(next(line)):
        mygod[next(line)]=nowgod

dfs(1)

for i in range(q):
    god,human=map(int,input().split())
    eldergod=mygod[human]
    if inout[god][0]<=inout[eldergod][0] and inout[god][1]>=inout[eldergod][1]:
        print("Get")
    else:
        print("Fail")
