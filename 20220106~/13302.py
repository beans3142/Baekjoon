from sys import stdin
input=stdin.readline

inf=float('inf')

def bt(day,price,coupon):
    if day>n:
        return price
    if dp[coupon][day]:
        return price+dp[coupon][day]
    if date[day]==0:
        return bt(day+1,price,coupon)
    ans=inf
    a1=bt(day+1,price+10000,coupon)
    a2=bt(day+3,price+25000,coupon+1)
    a3=bt(day+5,price+37000,coupon+2)
    ans=min(ans,a1,a2,a3)
    if coupon>2:
        ans=min(ans,bt(day+1,price,coupon-3))
    dp[coupon][day]=ans-price
    return ans

n,m=map(int,input().split())
date=[1]*(n+1)
unable=map(int,input().split())
for i in unable:
    date[i]=0

dp=[[0 for i in range(n+1)] for j in range(41)]

ans=bt(1,0,0)
print(ans)
