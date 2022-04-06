from sys import stdin,setrecursionlimit
setrecursionlimit(10000000)
input=stdin.readline
v,e=map(int,input().split())
graph=[[] for i in range(v+1)]
rev=[[] for i in range(v+1)]

for i in range(e):
    a,b=map(int,input().split())
    graph[a].append(b)

for i in range(1,v+1):
    for node in graph[i]:
        rev[node].append(i)

vi=[0]*(len(graph)+1)
time=[]
nowtime=0

def dfs(x,graph,d):
    global nowtime
    if vi[x]==d+1:
        return
    vi[x]=d+1
    if d==1:
        cycle.append(x)
    for i in graph[x]:
        if vi[i]==d:
            dfs(i,graph,d)
    nowtime+=1
    time.append((nowtime,x))

ans=[]
for i in range(1,v+1):
    if vi[i]==2:
        continue
    dfs(i,graph,0)
    for totaltime,v in sorted(time,reverse=True):
        if vi[v]==2:
            continue
        cycle=[]
        dfs(v,rev,1)
        if cycle:
            ans.append(sorted(cycle))
    nowtime=0

print(len(ans))
for i in sorted(ans):
    print(*i,-1)
