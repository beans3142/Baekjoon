from sys import stdin
input=stdin.readline

n,k=map(int,input().split())

arr=list(map(int,input().split()))

dp=[[0 for i in range(k+1)] for j in range(n+1)]

for i in range(1,n+1):
    for j in range(k+1):
        if arr[i-1]%2==0:
            dp[i][j]=dp[i-1][j]+1
        elif j!=0:
            dp[i][j]=dp[i-1][j-1]


print(max([max(dp[i]) for i in range(n+1)]))
