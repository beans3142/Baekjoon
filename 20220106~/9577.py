from sys import stdin
input=stdin.readline

def dfs(a):
    if vi[a]:
        return False
    vi[a]=True
    for b in graph[a]:
        if rev[b]==-1 or dfs(rev[b]):
            rev[b]=a
            return True
    return False

for _ in range(int(input())):
    n,m=map(int,input().split())
    graph=[[] for i in range(101)]
    for i in range(1,m+1):
        t1,t2,a,*qi=map(int,input().split())
        for k in range(t1,t2):
            for q in qi:
                graph[k].append(q)

    cnt=0
    rev=[-1]*(101)
    for i in range(101):
        vi=[False]*(101)
        if dfs(i):
            cnt+=1
            if cnt==n:
                break
    if cnt<n:
        print(-1)
    else:
        print(i+1)
