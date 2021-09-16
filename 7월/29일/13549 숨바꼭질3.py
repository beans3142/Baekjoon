import sys
from collections import deque
input=sys.stdin.readline

n,k=map(int,input().split())

if k<n:
    print(n-k)
elif k==n:
    print(0)
else:
    time=[sys.maxsize]*((k*2)+1)
    time[n]=0
    queue=deque([[n,0]])
    while queue:
        now,v=queue.popleft()
        if now==k:
            break
        if now!=1:
            double=now*2
            while True:
                try:
                    if time[double]>v:
                        time[double]=v
                        queue.append([double,v])
                        double*=2
                    else:
                        break
                except:
                    break
        if now<k and time[now+1]>v:
            queue.append([now+1,v+1])
            time[now+1]=v+1
            double=now*2
            while True:
                try:
                    if time[double]>v:
                        time[double]=v+1
                        queue.append([double,v+1])
                        double*=2
                    else:
                        break
                except:
                    break
        if 0<now<2*k and time[now-1]>v:
            queue.append([now-1,v+1])
            double=now*2
            time[now-1]=v+1
            while True:
                try:
                    if time[double]>v:
                        time[double]=v+1
                        queue.append([double,v+1])
                        double*=2
                    else:
                        break
                except:
                    break
    print(time[k])
    
