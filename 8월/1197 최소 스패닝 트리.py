from sys import stdin
from heapq import heappop,heappush
input=stdin.readline

n,m=map(int,input().split())

vi=[0]*n
order=[]

for i in range(m):
    a,b,c=map(int,input().split())
    heappush(order,(c,a,b))

for i in
