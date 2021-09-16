import sys
from heapq import heappop,heappush
from math import inf
input=sys.stdin.readline

n,k=map(int,input().split())

if k<n:
    print(n-k)
    for i in range(n,k-1,-1):
        print(i,end=' ')
elif k==n:
    print(0)
    print(k)
else:
    queue=[(0,n,[n])]
    mx=(2*k)+1
    time=[inf]*(mx)
    while queue:
        val,now,vi=heappop(queue)
        if now==k:
            print(val)
            print(*vi)
            break
        if now<k and time[now+1]>val+1:
            time[now+1]=val+1
            heappush(queue,(val+1,now+1,vi+[now+1]))
        if 0<now<mx and time[now-1]>val+1:
            time[now-1]=val+1
            heappush(queue,(val+1,now-1,vi+[now-1]))
        if 0<now<k and time[now*2]>val+1:
            time[now*2]=val+1
            heappush(queue,(val+1,now*2,vi+[now*2]))
        
            

        
