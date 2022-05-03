from sys import stdin
input=stdin.readline

def dfs(x):
    global cost
    isEnd=True
    for i in graph[x]:
        if vi[i]==0:
            vi[i]=1
            isEnd=False
            cost[x]+=dfs(i)
    if isEnd:
        cost[x]=1
        return 1
    return cost[x]
    

n,m=map(int,input().split())
vi=[0]*(n+1)
cost=[0]*(n+1)
graph=[[] for i in range(n+1)]

for i in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

vi[1]=1
dfs(1)

s=sum(cost)

if m%s:
    print(-1)
else:
    print(m//s)
