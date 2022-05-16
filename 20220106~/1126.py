from sys import stdin
from copy import deepcopy
input=stdin.readline

n=int(input())
arr=sorted(map(int,input().split()))
dp=[[-1]*(500001) for i in range(2)]
dp[0][0]=dp[1][0]=0
mx=0
for i in range(n):
    for j in range(mx+1):
        if dp[0][j]==-1:
            continue
        dp[1][j+arr[i]]=max(dp[1][j+arr[i]],dp[0][j]+arr[i])
        if j<arr[i]:
            dp[1][arr[i]-j]=max(dp[1][arr[i]-j],dp[0][j]+arr[i]-j)
        else:
            dp[1][j-arr[i]]=max(dp[0][j],dp[1][j-arr[i]])

    mx+=arr[i]
    dp[0]=deepcopy(dp[1])
    
print(dp[0][0] if dp[0][0]>0 else -1)
