from sys import stdin
input=stdin.readline


def dfs(a):
    if vi[a]:
        return False
    vi[a]=True
    for b in graph[a]:
        if rev[b]==-1 or dfs(rev[b]):
            rev[b]=a
            cor[a]=b
            return True
    return False


def mvcdfs(a):
    via[a]=True
    for b in graph[a]:
        if rev[b]!=-1 and vib[b]==via[rev[b]]==False:
            vib[b]=True
            mvcdfs(rev[b])



        
n,m=map(int,input().split())
graph=[[] for i in range(n+1)]
rgraph=[[] for i in range(m+1)]

for i in range(n):
    ai,*nodes=map(int,input().split())
    for node in nodes:
        graph[i+1].append(node)
        rgraph[node].append(i+1)

cor=[-1]*(n+1) 
rev=[-1]*(m+1)
cnt=0

for i in range(1,n+1):
    vi=[False]*(n+1)
    if dfs(i):
        cnt+=1

via=[False]*(n+1)
vib=[False]*(m+1)

for i in range(1,n+1):
    if cor[i]==-1:
        mvcdfs(i)

ansa=[]
ansb=[]

for i in range(1,n+1):
    if via[i]==False:
        ansa.append(i)

for i in range(1,m+1):
    if vib[i]:
        ansb.append(i)

print(cnt)
print(len(ansa),*ansa)
print(len(ansb),*ansb)
