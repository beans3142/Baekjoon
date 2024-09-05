from sys import stdin
input=stdin.readline

n,m=map(int,input().split())
arr=[input().rstrip() for i in range(n)]
dp=[[0]*m for i in range(n)]

for i in range(n):
    dp[i][0]=int(arr[i][0]=='1')

for j in range(m):
    dp[0][j]=int(arr[0][j]=='1')

for i in range(1,n):
    for j in range(1,m):
        if arr[i][j]=='1':
            dp[i][j]=min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])+1

print(max(max(i) for i in dp)**2)