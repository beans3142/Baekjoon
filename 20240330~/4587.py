from sys import stdin
from math import gcd
input=stdin.readline

while True:
    p,q=map(int,input().split())
    if p==q==0: break
    n=1
    ans=[]
    while p>0:
        if n*p>=q:
            p=n*p-q
            q=q*n
            div=gcd(p,q)
            p//=div
            q//=div
            ans.append((n,p,q))
        n+=1
    print(*ans)
