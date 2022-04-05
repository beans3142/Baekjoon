from sys import stdin
input=stdin.readline

s1=input().rstrip()
s2=input().rstrip()

dp=[[0 for i in range(len(s1)+1)] for i in range(len(s2)+1)]

for i in range(len(s1)+1):
    dp[0][i]=i

for i in range(len(s2)+1):
    dp[i][0]=i

for i in range(1,len(s2)+1):
    for j in range(1,len(s1)+1):
        if s2[i-1]==s1[j-1]:
            dp[i][j]=dp[i-1][j-1]
        else:
            dp[i][j]=min(dp[i-1][j],dp[i][j-1])+1

print(dp[-1][-1])
    
