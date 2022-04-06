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

now=0

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
    time=[]
    nowtime=0

group={}
for idx,i in enumerate(ans):
    for j in i:
        group[j]=idx+1
reach=[set() for i in range(len(ans)+1)]
for i in range(len(ans)):
    for j in ans[i]:
        for k in graph[j]:
            if group[k]!=group[j]:
                reach[i+1].add(group[k])

vi=[1]*(len(ans)+1)
vi[0]=0
for i in reach:
    for j in i:
        vi[j]=0
print(sum(vi))
