from sys import stdin
from collections import defaultdict
input=stdin.readline

n=int(input())
items=defaultdict(dict)
include=defaultdict(list)
buy=defaultdict(int)
for i in range(n):
    before,after=input().rstrip().split()
    items[after][before]=1
    items[before]
    include[before].append(after)
    include[after]

ans=[]
able=False
idx=0

a=[]

for i in items:
    if not items[i]:
        able=True
        a.append(i)

if able:
    while a:
        ans.append(sorted(a))
        b=[]
        for i in a:
            del items[i]
            for j in include[i]:
                del items[j][i]
                if buy[j]!=0:
                    continue
                if not items[j]:
                    buy[j]=1
                    b.append(j)
        a=b

if items:
    print(-1)
else:
    for i in ans:
        for j in i:
            print(j)
