from sys import stdin
input=stdin.readline

n=int(input())
arr=[list(map(int,input().split())) for i in range(n)]
dp=[arr[0][2]]
if n>1:
    dp.append(arr[1][2])

for i in range(2,n):
    dp.append(max(arr[i][2]+dp[i-2],dp[-1]))
    dp[i-1]=max(dp[i-1],dp[i-2])

print(max(dp))
