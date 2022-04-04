from sys import stdin
from collections import defaultdict
input=stdin.readline
n,m=map(int,input().split())
sub=defaultdict(list)
nxt=defaultdict(list)
cem=[1]*n
for i in range(m):
    a,b=map(int,input().split())
    sub[b]+=[a]
    sub[a]
    nxt[a]+=[b]
    nxt[b]

while sub:
    queue=[]
    for i in sub:
        if not sub[i]:
            queue.append(i)
    for i in queue:
        del sub[i]
    for i in queue:
        for j in nxt[i]:
            sub[j].remove(i)
            if not sub[j]:
                cem[j-1]=cem[i-1]+1

print(*cem)
