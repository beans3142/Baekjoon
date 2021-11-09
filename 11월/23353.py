from sys import stdin
input=stdin.readline

n=int(input())
arr=[list(map(int,input().split())) for i in range(n)]
dp=[[[0]*(n) for i in range(n)]for i in range(8)] # 상하좌우왼위오위왼아오아
mx=1

# 아래쪽으로 몇개?

for i in range(n):
    dp[0][0][i]=1 if arr[0][i]==1 else 0
for i in range(1,n):
    for j in range(n):
        dp[0][i][j]=dp[0][i-1][j]+1 if arr[i][j]==1 else 0

# 위쪽으로 몇개?

for i in range(n):
    dp[1][-1][i]=1 if arr[-1][i]==1 else 0
for i in range(1,n):
    for j in range(n):
        dp[1][~i][j]=dp[1][~i+1][j]+1 if arr[~i][j]==1 else 0

# 우측으로

for i in range(n):
    dp[2][i][0]=1 if arr[i][0]==1 else 0
for i in range(n):
    for j in range(1,n):
        dp[2][i][j]=dp[2][i][j-1]+1 if arr[i][j]==1 else 0

# 좌측으로

for i in range(n):
    dp[3][i][-1]=1 if arr[i][-1]==1 else 0
for i in range(n):
    for j in range(1,n):
        dp[3][i][~j]=dp[3][i][~j+1]+1 if arr[i][~j]==1 else 0

# 이제 대각선..

for i in range(n):
    dp[4][0][i]=1 if arr[0][i]==1 else 0
for i in range(n):
    dp[4][i][0]=1 if arr[i][0]==1 else 0
for i in range(1,n):
    for j in range(1,n):
        dp[4][i][j]=dp[4][i-1][j-1]+1 if arr[i][j]==1 else 0


for i in range(n):
    dp[5][0][i]=1 if arr[0][i]==1 else 0
for i in range(n):
    dp[5][i][-1]=1 if arr[i][-1]==1 else 0
for i in range(1,n):
    for j in range(1,n):
        dp[5][i][~j]=dp[5][i-1][~j+1]+1 if arr[i][~j]==1 else 0

for i in range(n):
    dp[6][~0][i]=1 if arr[~0][i]==1 else 0
for i in range(n):
    dp[6][i][~0]=1 if arr[i][~0]==1 else 0
for i in range(1,n):
    for j in range(1,n):
        dp[6][~i][~j]=dp[6][~i+1][~j+1]+1 if arr[~i][~j]==1 else 0

for i in range(n):
    dp[7][~0][i]=1 if arr[~0][i]==1 else 0
for i in range(n):
    dp[7][i][0]=1 if arr[i][0]==1 else 0
for i in range(1,n):
    for j in range(1,n):
        dp[7][~i][j]=dp[7][~i+1][j-1]+1 if arr[~i][j]==1 else 0

ans=0

for i in range(n):
    for j in range(n):
        for _ in range(8):
            ans=max(ans,dp[_][i][j])
        if arr[i][j]==2:
            ans=max(ans,(dp[4][i-1][j-1] if i-1>-1 and j-1>-1 else 0) +(dp[6][i+1][j+1] if i+1<n and j+1<n else 0) +1,\
                    (dp[7][i+1][j-1] if i+1<n and j-1>-1 else 0) +(dp[5][i-1][j+1] if i-1>-1 and j+1<n else 0)+1,\
                    (dp[2][i][j-1] if j-1>-1 else 0)+(dp[3][i][j+1] if j+1<n else 0)+1,\
                    (dp[1][i+1][j] if i+1<n else 0)+(dp[0][i-1][j] if i-1>-1 else 0)+1)

print(ans)

'''
for i in range(8):
	for j in dp[i]:
		print(j)
	print()
	print()
	'''
