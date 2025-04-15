n,k=map(int,input().split())
arr=list(map(int,input().split()))
dp=[0]*(n+1)
for i in arr:
    dp[i]=-1
for i in range(1,k+1):
    
