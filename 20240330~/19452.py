from sys import stdin
input=stdin.readline

def dfs1(now):
    cnt=0
    for nxt in tree[now]:
        if vi[nxt]==0:
            vi[nxt]=1
            cnt=max(dfs1(nxt),cnt)
    left[now]=cnt+1
    return left[now]
    
        
    
def dfs2(now):
    global dist
    for nxt in tree[now]:
        if vi[nxt]==1 and left[nxt]>d:
            dist+=2
            vi[nxt]=2
            dfs2(nxt)



n,s,d=map(int,input().split())

tree=[[] for i in range(n+1)]
left=[0]*(n+1)

vi=[0]*(n+1)

for i in range(n-1):
    a,b=map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)


dist=0
vi[s]=1
dfs1(s)
vi[s]=2
dfs2(s)
print(dist)
