from sys import stdin
input=stdin.readline

n,m=map(int,input().split())
visited=[False]*2001

friend=[[] for i in range(n)]

for i in range(m):
    a,b=map(int,input().split())
    friend[a].append(b)
    friend[b].append(a)

def dfs(x,depth):
    visited[x]=True
    if depth==4:
        print(1)
        exit()
    for i in friend[x]:
        if visited[i]==False:
            dfs(i,depth+1)
            visited[i]=False
            

for i in range(n):
    dfs(i,0)
    visited[i]=False

print(0)
