# 유클리드 호제법 이해하기

from random import *

#a,b=randint(1,101),randint(1,101)
a,b=map(int,input().split())

n=max(a,b)
m=min(a,b)
r=1

print(n,m,'의 최대공약수 구하기')



while r!=0:
    r=n%m
    n=m
    m=r

print(n)
