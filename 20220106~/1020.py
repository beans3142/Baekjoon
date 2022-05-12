from sys import stdin
input=stdin.readline

case=[6,2,5,5,4,5,6,3,7,5,6]

n=list(input().rstrip())
num=0
d=0
digit=1
le=0

for i in n:
    num=num*10+int(i)
    d+=case[int(i)]
    digit*=10
    le+=1


n=list(map(int,n))+[0]*(15-len(n))

dp=[[[digit*2 for i in range(106)] for i in range(16)] for i in range(2)]
dp[0][le][0]=0

p=1

for i in range(le-1,-1,-1):
    for j in range(10):
        for k in range(case[j],106):
            dp[0][i][k]=min(dp[0][i][k],dp[0][i+1][k-case[j]]+j*p)
            if j>n[i]:
                dp[1][i][k]=min(dp[1][i][k],dp[0][i+1][k-case[j]]+j*p)
    for j in range(case[n[i]],106):
        dp[1][i][j]=min(dp[1][i][j],dp[1][i+1][j-case[n[i]]]+n[i]*p)
    p*=10

print(min(dp[0][0][d]+digit,dp[1][0][d])-num)
