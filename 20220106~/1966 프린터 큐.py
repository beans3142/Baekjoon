import sys
input=sys.stdin.readline
t=int(input())

for i in range(t):
    n,idx=map(int,input().split())
    pq=list(map(int,input().split()))
    loc=[0]*len(pq)
    loc[idx]=1
    while pq:
        if pq[0] != max(pq):
            pq.append(pq.pop(0))
            loc.append(loc.pop(0))
        else:
            pq.pop(0)
            if loc.pop(0) == 1:
                print(n-len(pq))
                break

            
