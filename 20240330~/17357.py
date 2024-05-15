import sys
input = sys.stdin.readline
n,k = map(int,input().split())
data = list(map(int,input().split()))
dp = [0] * n
dp[0] = data[0]
for i in range(1,n):
	dp[i] = dp[i-1] + data[i]
dp.sort(reverse=True)
print(sum(dp[:k]))
