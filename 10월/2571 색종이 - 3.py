from sys import stdin
input=stdin.readline

n=int(input())
arr=[[0 for i in range(100)] for i in range(100)]
dp=[[0 for i in range(100)] for i in range(100)]

for i in range(n):
    x,y=map(int,input().split())
    for j in range(10):
        for k in range(10):
            arr[~y-j][~x-k]=1
            dp[~y-j][~x-k]=1

for i in range(1,100):
    for j in range(100):
        if arr[i][j]==1:
            dp[i][j]=dp[i-1][j]+1
            

ans=0
for i in range(100):
    for j in range(100):
        if dp[i][j]!=0:
            idx=0
            h=dp[i][j]
            while dp[i][j+idx]:
                h=min(h,dp[i][j+idx])
                ans=max(ans,h*(idx+1))
                idx+=1

print(ans)
