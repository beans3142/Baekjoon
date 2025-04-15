from sys import stdin;input=stdin.readline
from collections import deque
dr=[1,0,-1,0]
dc=[0,1,0,-1]
n=int(input())
arr=[input().rstrip() for i in range(n)]
def check(sr,sc):
    def dfs(r,c):
        for i in range(4):
            nr=r+dr[i]
            nc=c+dc[i]
            if -1<nr<n and -1<nc<n:
                if vi[nr][nc]==0 and arr[nr][nc]=='.':
                    vi[nr][nc]=1
                    dfs(nr,nc)
    vi=[[0]*n for i in range(n)]
    vi[sr][sc]=1
    div=0
    for i in range(4):
        nsr=sr+dr[i]
        nsc=sc+dc[i]
        if -1<nsr<n and -1<nsc<n:
            if vi[nsr][nsc]==0 and arr[nsr][nsc]=='.':
                vi[nsr][nsc]=1
                dfs(nsr,nsc)
                div+=1
    return div>1
ans=0
for r in range(n):
    for c in range(n):
        if arr[r][c]=='.':
            ans+=check(r,c)
print(ans)
