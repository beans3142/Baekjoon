from sys import stdin
input=stdin.readline

n,k=map(int,input().split())
arr=[int(input()) for i in range(n)]
dp=[0]*(k+1)
dp[0]=1
for i in range(n):
    for j in range(arr[i],k+1):
        dp[j]+=dp[j-arr[i]]
        
print(dp[k])
