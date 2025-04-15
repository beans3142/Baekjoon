from sys import stdin
input=stdin.readline
from collections import defaultdict


while True:
    n=int(input())
    if n==0:break
    dd=defaultdict(list)
    for i in range(n):
        v,h=input().split()
        h=float(h)
        dd[h].append(v)
    print(*dd[max(dd)])
