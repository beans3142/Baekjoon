from sys import stdin
input=stdin.readline

n,k=map(int,input().split())

dp=[[0]*(n+1) for i in range(k)]

for i in range(n+1):
    dp[0][i]=1

for i in range(1,k):
    for j in range(n+1):
        for l in range(j+1):
            dp[i][j]+=dp[i-1][l]
            dp[i][j]%=1000000000
        

print(dp[-1][-1])
