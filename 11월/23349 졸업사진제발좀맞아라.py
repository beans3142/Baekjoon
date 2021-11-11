from sys import stdin
from collections import defaultdict
input=stdin.readline

n=int(input())

name=defaultdict(int)
place=defaultdict(list)
p={}

for i in range(n):
    n,l,s,e=input().rstrip().split()
    if name[n]:
        continue
    name[n]=1
    s=int(s)
    e=int(e)
    place[l].append((s,e))

mx=max([len(place[i]) for i in place])
able=[]

for i in place:
    if len(place[i])==mx:
        able.append(i)
    

for i in able:
    p[i]=defaultdict(int)
    for s,e in place[i]:
        for t in range(s,e):
            p[i][t]+=1

mx_dist=0

for i in sorted(able):
    idx=1
    while idx<50001:
        if mx_dist<p[i][idx]:
            s=idx
            mx_dist=p[i][idx]
            ansp=i
            while mx_dist==p[i][idx]:
                idx+=1
            e=idx
        else:
            idx+=1
    
    
print(ansp,s,e)
