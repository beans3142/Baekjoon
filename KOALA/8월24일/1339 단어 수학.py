from sys import stdin
from collections import defaultdict
input=stdin.readline

n=int(input())
dic=defaultdict(int)

for i in range(n):
    atn=input().rstrip()
    for w in range(len(atn)):
        dic[atn[~w]]+=10**w

mx=9
ans=0
for i in sorted([(i[1],i[0]) for i in dic.items()],reverse=True):
    ans+=dic[i[1]]*mx
    mx-=1

print(ans)
