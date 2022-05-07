from sys import stdin
from copy import deepcopy
input=stdin.readline


n=int(input())
arr=list(map(int,input().split()))
tree=[[] for i in range(n+1)]
tree[0].append(0)
ans=0

def dfs(x,dep):
    global ans
    if dep==n:
        ans+=tree[dep][x]
        return tree[dep][x]
    left=dfs(2*x,dep+1)
    right=dfs(2*x+1,dep+1)
    ans+=abs(left-right)+tree[dep][x]
    return tree[dep][x]+max(left,right)

idx=0
for i in range(1,n+1):
    for j in range(2**i):
        tree[i].append(arr[idx])
        idx+=1

dfs(0,0)

print(ans)
