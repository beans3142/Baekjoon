from sys import stdin;input=stdin.readline
inf=float('inf')
n,m=map(int,input().split())
graph=[[inf]*(n+1) for i in range(n+1)]

for i in range(m):
    a,b,c=map(int,input().split())
    graph[a][b]=graph[b][a]=min(graph[a][b],c) # 동일간선처리


for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==j: continue
            graph[i][j]=min(graph[i][k]+graph[k][j],graph[i][j])

mx=0
ans=''
for i in range(1,n+1):
    for j in range(i+1,n+1):
        if graph[i][j]>mx:
            mx=graph[i][j]
            ans=(i,j)

print(*ans)
