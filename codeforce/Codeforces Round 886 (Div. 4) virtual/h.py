from sys import stdin
input=stdin.readline

def dfs(now):
    global flag
    for nxt,dist in graph[now]:
        if vi[nxt]==inf:
            nxtloc=vi[now]+dist
            if nxtloc not in vi:
                vi[nxt]=nxtloc
                dfs(nxt)
            else:
                flag=False
                return
        else:
            if vi[nxt]!=vi[now]+dist:
                flag=False

for _ in range(int(input())):
    n,m=map(int,input().split())
    inf=float('inf')
    vi=[inf]*(n+1)
    graph=[[] for i in range(n+1)]
    for i in range(m):
        a,b,c=map(int,input().split())
        graph[a].append((b,c))
        graph[b].append((a,-c))
    flag=True
    for i in range(1,n+1):
        if vi[i]==inf:
            use={i}
            vi[i]=0
            dfs(i)
    if flag:
        print("YES")
    else:
        print("NO")

