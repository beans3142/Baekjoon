from sys import stdin
from collections import deque
input=stdin.readline

div=10**9+7

def bfs():
    vi=[0]*(n+1)
    vi[s]=1
    queue=deque([(s,arr[s])])
    while queue:
        now,num=queue.popleft()
        if now==e:
            return num
        for i in connected[now]:
            if vi[i]==0:
                vi[i]=1
                queue.append((i,merge(num,arr[i])))

def merge(a,b):
    return int(str(a)+str(b))%div

n,q=map(int,input().split())
arr=[0]+list(map(int,input().split()))
connected=[[] for i in range(n+1)]

for i in range(n-1):
    a,b=map(int,input().split())
    connected[a].append(b)
    connected[b].append(a)

for i in range(q):
    s,e=map(int,input().split())
    print(bfs())
