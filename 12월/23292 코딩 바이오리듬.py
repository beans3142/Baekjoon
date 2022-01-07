from sys import stdin
from collections import defaultdict
input=stdin.readline

a=list(map(int,list(input().rstrip())))
n=int(input())
d=defaultdict(list)
for i in range(n):
    bio=0
    y=list(map(int,list(input().rstrip())))
    for j in range(4):
        bio+=(a[j]-y[j])**2
    bio*=((a[4]-y[4])**2+(a[5]-y[5])**2)
    bio*=((a[6]-y[6])**2+(a[7]-y[7])**2)
    d[bio].append(y)

print(*sorted(d[max(d)])[0],sep='')


