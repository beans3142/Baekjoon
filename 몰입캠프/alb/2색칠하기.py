from sys import stdin,setrecursionlimit
from collections import defaultdict
setrecursionlimit(10**6)
input=stdin.readline

n,m=map(int,input().split())
tree={i:defaultdict(int) for i in range(n)}
colors=[0]*n
vi=[0]*n
able=True

for i in range(m):
    a,b=map(int,input().split())
    tree[a][b]=0
    tree[b][a]=0
    
def dfs(x,color):
    global colors,able
    colors[x]=color
    vi[x]=1
    for i in tree[x]:
        if colors[x]==colors[i]:
            able=False
            return
        if vi[i]==0:
            dfs(i,1 if color==2 else 2)

dfs(0,1)

if able:
    print("YES")
else:
    print("NO")
