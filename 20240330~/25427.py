n=int(input())
s=input()
fx={"D":0,"K":1,"S":2}
dp=[[0]*3 for i in range(n+1)]
ans=0
for i in range(1,n+1):
    if s[i-1] in "DKS":
        dp[i][fx[s[i-1]]]+=1
    elif s[i-1]=='H':
        ans+=dp[i-1][0]*dp[i-1][1]*dp[i-1][2]
    for j in range(3):
        dp[i][j]+=dp[i-1][j]

print(ans)
            
