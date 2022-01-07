from sys import stdin
from collections import deque
input=stdin.readline

n,m=map(int,input().split())
matrix=[[0 for i in range(n+1)] for i in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    matrix[a][b]=matrix[b][a]=1

q=int(input())
for _ in range(q):
    a,i,j=map(int,input().split())
    if a==1:
        matrix[i][j]=matrix[j][i]=1
    else:
        matrix[i][j]=matrix[j][i]=0
    v=[-1]*(n)
    left=n
    queue=deque([[1,0]])
    while queue:
        now,vi=queue.popleft()
        if v[now-1]!=-1:
            continue
        v[now-1]=vi
        left-=1
        if left==0:
            break
        for k in range(1,n+1):
            if matrix[now][k]==1 and v[k-1]==-1:
                queue.append([k,vi+1])
    print(*v)
