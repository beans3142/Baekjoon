from sys import stdin,maxsize
input=stdin.readline
inf=maxsize
n = int(input())
p = []
for i in range(n):
    p.append(list(map(int, input().split())))
dp = [[0 for i in range(n)] for i in range(n)]

for d in range(n-1):
    for i in range(n-1-d):
        j = i + 1 + d
        dp[i][j]=maxsize
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + p[i][0]*p[k][1]*p[j][1])
print(dp[0][n-1])
