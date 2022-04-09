from sys import stdin
input=stdin.readline

n,m=map(int,input().split())
arr=list(map(int,input().split()))
dp=[0]*(n+1)
for i in range(n):
    dp[i+1]=dp[i]+arr[i]

for i in range(m):
    l,r=map(int,input().split())
    print(dp[r]-dp[l-1])
