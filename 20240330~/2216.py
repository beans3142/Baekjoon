from sys import stdin
input=stdin.readline

a,b,c=map(int,input().split())
s1=input().rstrip()
s2=input().rstrip()

dp=[[0]*(len(s2)+1) for i in range(len(s1)+1)]

for i in range(1,len(s1)+1):
    dp[i][0]=dp[i-1][0]+b

for i in range(1,len(s2)+1):
    dp[0][i]=dp[0][i-1]+b


for i in range(1,len(s1)+1):
    for j in range(1,len(s2)+1):
        if s1[i-1]==s2[j-1]:
            dp[i][j]=dp[i-1][j-1]+a
        else:
            dp[i][j]=dp[i-1][j-1]+c
        dp[i][j]=max(dp[i-1][j]+b,dp[i][j-1]+b,dp[i][j])

print(dp[-1][-1])
