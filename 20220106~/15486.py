from sys import stdin
input=stdin.readline

inf=float('inf')

n=int(input())
arr=[list(map(int,input().split())) for i in range(n)]
dp=[0 for i in range(n+1)]
for i in range(n):
    try:
        dp[i]=max(dp[i],dp[i-1])
        dp[i+arr[i][0]]=max(dp[i]+arr[i][1],dp[i+arr[i][0]])
    except:
        pass

print(max(dp))
