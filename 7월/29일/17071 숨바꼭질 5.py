import sys
from heapq import heappop,heappush
from math import inf
input=sys.stdin.readline

n,k=map(int,input().split())
move=[0,1]
for i in range(2,1000):
    move.append(move[-1]+i)
if k<n:
   pass 
if k==n:
    print(0)
else:
    queue=[(0,n)]
    time=[inf]*(500001)
    time[n]=0
    while queue:
        try:
            val,now=heappop(queue)
            dk=k+move[val]
            if now>500000:
                continue
            if now==dk:
                print(val)
                break
            if dk>500000:
                print(-1)
                break
            if 0<now and time[now+1]>val+1:
                time[now+1]=val+1
                heappush(queue,(val+1,now+1))
            if (0<now<dk*2+1 and time[now-1]>val+1) or (now>dk and time[now-1]>val+1):
                time[now-1]=val+1
                heappush(queue,(val+1,now-1))
            if 0<now<250001 and time[now*2]>val+1:
                time[now*2]=val+1
                heappush(queue,(val+1,now*2))
        except:
            continue
