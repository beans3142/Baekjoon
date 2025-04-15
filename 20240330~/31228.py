from math import *
n,k=map(int,input().split())
k=min(k,n-k)
g=gcd(n,k)
print(n//g*(k//g-1) if n%k and n>4 else 0)
