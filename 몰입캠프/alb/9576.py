from sys import stdin
input=stdin.readline

def dfs(x):
    if vi[x]:
        return False
    vi[x]=True
    for i in range(graph[x][0],graph[x][1]+1):
        if getbook[i]==0 or dfs(getbook[i]):
            getbook[i]=x
            return True
    return False

for _ in range(int(input())):
    n,m=map(int,input().split())
    graph=[[]for i in range(m+1)]
    getbook=[0]*(1001)
    vi=[False]*(1001)
    cnt=0
    for i in range(m):
        a,b=map(int,input().split())
        graph[i+1].append(a)
        graph[i+1].append(b)

    for i in range(1,m+1):
        for j in range(m+1):
            vi[j]=False
        if dfs(i):
            cnt+=1
    print(cnt)
