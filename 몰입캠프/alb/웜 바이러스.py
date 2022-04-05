from sys import stdin
input=stdin.readline

n=int(input())
m=int(input())
graph=[[] for i in range(n+1)]
v=[0]*(n+1)
cnt=0

for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x):
    global cnt
    cnt+=1
    v[x]=1
    for i in graph[x]:
        if v[i]==0:
            dfs(i)
dfs(1)

print(cnt-1)
