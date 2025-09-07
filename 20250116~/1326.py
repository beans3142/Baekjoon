from sys import stdin
from collections import deque
input=stdin.readline
n=int(input())
arr=list(map(int,input().split()))
vi=[1e9]*n
a,b=map(int,input().split())
q=deque([a-1])
vi[a-1]=0
while q:
    now=q.popleft()
    for i in range(now+arr[now],n,arr[now]):
        if vi[i]>vi[now]+1:
            vi[i]=vi[now]+1
            q.append(i)
    for i in range(now,-1,-arr[now]):
        if vi[i]>vi[now]+1:
            vi[i]=vi[now]+1
            q.append(i)
print(vi[b-1] if vi[b-1]!=1e9 else -1)
