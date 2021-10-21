from sys import stdin
input=stdin.readline

n,m=map(int,input().split())

arr=[input().rstrip() for i in range(n)]
dp=[[[0]*m for i in range(n)] for i in range(4)]
# [ 우측 하단,  좌측하단]
for i in range(n):
    for j in range(m):
        if arr[i][j]=='1':
            if i>0 and j>0:
                dp[2][i][j]=dp[2][i-1][j-1]+1
            else:
                dp[2][i][j]=1
            if i>0 and j+1<m:
                dp[3][i][j]=dp[3][i-1][j+1]+1
            else:
                dp[3][i][j]=1
        if arr[n-i-1][j]=='1':
            if i>0 and j+1<m:
                dp[1][n-i-1][j]=dp[1][n-i][j+1]+1
            else:
                dp[1][n-i-1][j]=1
            if i>0 and j>0:
                dp[0][n-i-1][j]=dp[0][n-i][j-1]+1
            else:
                dp[0][n-i-1][j]=1

ans=0

for i in range(n):
    for j in range(m):
        if arr[i][j]!='1':
            continue
        if m-j>ans or n-i>ans*2-1 or j>ans:
            mn=min(dp[0][i][j],dp[1][i][j])
            if mn>ans:
                for ii in range(ans,mn):
                    d=ii*2
                    if i+d<n:
                        if dp[2][i+d][j]>ii and dp[3][i+d][j]>ii:
                            ans=ii+1

print(ans)

for i in dp:
    for j in i:
        print(j)
    print()
