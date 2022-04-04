from sys import stdin
input=stdin.readline
n,m=map(int,input().split())
arr=[list(map(int,input().split())) for i in range(n)]
dp=[[0 for i in range(m)] for i in range(n)]
for i in range(m):
    dp[0][i]=arr[0][i]
    
for i in range(1,n):
    dp[i][0]=arr[i][0]+dp[i-1][1]
    dp[i][1]=arr[i][1]+min(dp[i-1][0],dp[i-1][2])
    dp[i][2]=arr[i][2]+min(dp[i-1][1],dp[i-1][3])
    dp[i][3]=arr[i][3]+dp[i-1][2]
