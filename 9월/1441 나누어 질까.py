from sys import stdin
from heapq import heappush,heappop
from collections import defaultdict
input=stdin.readline
n,l,r=map(int,input().split())
a=sorted(set(map(int,input().split())))
#print(a)
unable=[]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[j]%a[i]==0:
            unable.append(a[j])

a=[i for i in a if i not in unable]

arr=[]
vi=[0]*n
ans=0

def bt(idx,nums,depth):
    for i in range(idx,len(a)):
        if vi[i]==0:
            vi[i]=1
            bt(i,nums*a[i],depth+1)
            heappush(arr,(nums*a[i],-(depth+1)))
            vi[i]=0

bt(0,1,0)
used=defaultdict(int)
while arr:
    num,depth=heappop(arr)
    if used[num]==0:
        used[num]=1
        val=(r)//num-(l-1)//num
        if depth%2==0:
            val=-val
        ans+=val
print(ans)
