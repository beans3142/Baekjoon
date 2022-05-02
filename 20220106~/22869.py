from sys import stdin
from collections import deque
input=stdin.readline

n,k=map(int,input().split())
arr=list(map(int,input().split()))
vi=[0]*(n)

queue=deque([0])

while queue:
    now=queue.popleft()
    for i in range(1,k+1):
        if now+i<n:
            if vi[now+i]==0:
                if (i)*(1+abs(arr[now]-arr[now+i]))<=k:
                    vi[now+i]=1
                    queue.append(now+i)
        else:
            break

if vi[-1]:
    print("YES")
else:
    print("NO")
