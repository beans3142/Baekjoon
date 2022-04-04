from sys import stdin
import heapq

input=stdin.readline

t=int(input())

for i in range(t):
    heap1=[]
    heap2=[]
    visited=[0]*1000001
    k=int(input())
    for key in range(k):
        order,n=input().rstrip().split()
        n=int(n)
        if order=='I':
            heapq.heappush(heap1,(-n,key))
            heapq.heappush(heap2,(n,key))
            visited[key]=1
        elif order=='D':
            if n==1:
                while heap1 and not visited[heap1[0][1]]:
                    heapq.heappop(heap1)
                if heap1:
                    visited[heap1[0][1]]=0
                    heapq.heappop(heap1)
            else:
                while heap2 and not visited[heap2[0][1]]:
                    heapq.heappop(heap2)
                if heap2:
                    visited[heap2[0][1]]=0
                    heapq.heappop(heap2)
    while heap2 and not visited[heap2[0][1]]:
        heapq.heappop(heap2)
    while heap1 and not visited[heap1[0][1]]:
        heapq.heappop(heap1)
        
    if len(heap1)!=0 and len(heap2)!=0:
        print(-heap1[0][0],heap2[0][0])
    else:
        print('EMPTY')
