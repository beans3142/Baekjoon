from collections import defaultdict
from sys import stdin
from copy import deepcopy
input=stdin.readline

n=int(input())
arr=[[0]*(n+1)]+[[0]+list(map(int,input().split())) for i in range(n)]
dp=[[[0 for i in range(11)] for i in range(n+1)] for i in range(n+1)]
q=int(input())


# 첫 줄 채워넣기
dp[1][1][arr[1][1]]+=1
for i in range(2,n+1):
    dp[i][1][arr[i][1]]+=1
    dp[1][i][arr[1][i]]+=1
    for j in range(1,11):
        dp[i][1][j]+=dp[i-1][1][j]
        dp[1][i][j]+=dp[1][i-1][j]

for j in range(2,n+1):
    for i in range(2,n+1):
        for k in range(1,11):
            dp[j][i][k]+=dp[j-1][i][k]+dp[j][i-1][k]-dp[j-1][i-1][k]
        dp[j][i][arr[j][i]]+=1
        
ans=0
for i in range(q):
    a,b,c,d=map(int,input().split())
    a-=1
    b-=1
    ans=0
    for j in range(1,11):
        cnt=dp[c][d][j]+dp[a][b][j]-dp[a][d][j]-dp[c][b][j]
        ans+=bool(cnt>0)
    print(ans)
