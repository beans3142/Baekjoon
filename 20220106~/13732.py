from sys import stdin
from collections import deque
input=stdin.readline

n,m=map(int,input().split())
arr=[input().rstrip() for i in range(n)]
line=deque([])
ans=[['' for i in range(m)] for i in range(n)]

for i in range(m):
    for j in range(n):
        if arr[~j][i]=='#':
            ans[~j][i]='#'
            for k in range(len(line)):
                ans[~j+k+1][i]=line[~k]
            line=deque([])
        else:
            if arr[~j][i]=='.':
                line.append('.')
            else:
                line.appendleft('a')
    for k in range(len(line)):
        ans[~j+k][i]=line[~k]
    line=deque([])

for i in ans:
    print(*i,sep='')
