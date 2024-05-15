from sys import stdin
input=stdin.readline

n=int(input())
arr=list(map(int,input().split()))
dp=[0]*(n+1)
for i in range(n,0,-1):
    try:
        dp[i]=dp[i+arr[i-1]+1]+1
    except:
        dp[i]=1
print(*dp[1:])
