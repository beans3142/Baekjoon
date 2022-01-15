from sys import stdin
from bisect import bisect_left
from collections import defaultdict
input=stdin.readline

n=int(input())
crane=sorted(list(map(int,input().split())),reverse=True)
mx=max(crane)
m=int(input())
box=sorted(list(map(int,input().split())))

minute=0

if mx<box[-1]:
    print(-1)
    exit()

items=defaultdict(int)
for i in box:
    items[i]+=1

while items:
    for i in crane:
        li=list(items)
        idx=bisect_left(li,i)
        items[li[idx-1]]-=1
        if items[li[idx-1]]==0 :
            del items[li[idx-1]]
            if not items:
                break
    minute+=1

print(minute)
