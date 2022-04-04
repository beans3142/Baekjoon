from sys import stdin
from math import *
input=stdin.readline

for _ in range(int(input())):
    total=0
    n,m,a=map(int,input().split())
    for i in range(n+1):
        for j in range(m+1):
            if gcd(i,j)<=a:
                total+=lcm(i,j)
    print(total)
                
