from sys import stdin
input=stdin.readline
n=int(input())
arr=list(map(int,input().split()))
dp=[0 for i in range(n)]
dp[0]=arr[0]
for i in range(1,n):
    dp[i]=max(arr[i],arr[i]+dp[i-1])

print(max(dp))
