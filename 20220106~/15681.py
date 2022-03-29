from sys import stdin,setrecursionlimit
from collections import defaultdict
input=stdin.readline
setrecursionlimit(1000000)

n,r,q=map(int,input().split())
tree=[[] for i in range(n+1)] #트리
dp=[1]*(n+1) # 정답
vi=[0]*(n+1) # 방문처리

for i in range(n-1):
    u,v=map(int,input().split())
    tree[u].append(v)
    tree[v].append(u)

# 루트 노드는 방문처리

def dfs(node):
    global dp
    vi[node]=1
    for i in tree[node]:
        if vi[i]==0:
            dfs(i)
            dp[node]+=dp[i]
    
    
dfs(r)

for i in range(q):
    print(dp[int(input())])
    
