from sys import stdin
from heapq import heappop,heappush
input=stdin.readline

n=int(input())
hq=[]
len_n_hq=[]

for i in range(n):
    for j in map(int,input().split()):
        heappush(hq,j)
    while len(hq)>n:
        heappop(hq)
            
print(sorted(hq)[0])
