from sys import stdin
from heapq import heappop,heappush
from collections import defaultdict
input=stdin.readline
vi=defaultdict(int)
hq=[]
n,l=map(int,input().split())
arr=list(map(int,input().split()))
idx=0
leng=0
ans=[]

for idx,i in enumerate(arr):
    heappush(hq,i)
    vi[i]+=1
    num=hq[0]
    if idx>l-1:
        vi[arr[idx-l]]-=1
    while vi[num]==0:
        heappop(hq)
        num=hq[0]
    ans.append(hq[0])

print(*ans)
