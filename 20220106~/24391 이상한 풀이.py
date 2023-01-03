from sys import stdin
from collections import defaultdict
input=stdin.readline

n,m=map(int,input().split())

dd=defaultdict(set)

for i in range(m):
    a,b=map(int,input().split())
    dd[a].add(b)
    dd[b].add(a)
    dd[a]|=dd[b]
    dd[b]|=dd[a]
