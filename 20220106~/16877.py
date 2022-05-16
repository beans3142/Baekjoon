from sys import stdin
input=stdin.readline

fibo=[0,1]
for i in range(37):
    fibo.append(fibo[-1]+fibo[-2])

dp=[0]*(3000001)
for i in range(3):
    dp[i+1]=dp[i]+1
    
for i in range(4,3000001):
    bits=[False]*16
    for j in range(2,36):
        if fibo[j]<=i:
            bits[dp[i-fibo[j]]]=True
        else:
            break
    for j in range(16):
        if not bits[j]:
            dp[i]=j
            break

n=int(input())
arr=list(map(int,input().split()))
ans=0
for i in range(n):
    ans^=dp[arr[i]]

if ans:
    print('koosaga')
else:
    print('cubelover')
