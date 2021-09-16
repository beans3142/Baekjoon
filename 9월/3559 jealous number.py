from sys import stdin
from math import lcm
input=stdin.readline

l,r,p,q=map(int,input().split())

ans=r//p-(l-1)//p
ans-=r//(p*q)-(l-1)//(p*q)

print(ans)
