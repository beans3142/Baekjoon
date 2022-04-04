from sys import stdin
import heapq

input=stdin.readline

heap=[]
absheap={}
n=int(input())

for i in range(n):
    a=int(input())
    if a==0:
        try:
            if absheap[heap[0]][0]>0:
                print(-heap[0])
                absheap[heap[0]][0]-=1
            elif absheap[heap[0]][1]>0:
                print(heap[0])
                absheap[heap[0]][1]-=1
            if absheap[heap[0]]==[0,0]:
                heapq.heappop(heap)

        except:
            print(0)

    else:
        try:
            if absheap[abs(a)]==[0,0]:
                raise ValueError
            if a < 0:
                absheap[abs(a)][0]+=1
            else:
                absheap[a][1]+=1
        except:
            heapq.heappush(heap,abs(a))
            if a>0:
                absheap[a]=[0,1]
            else:
                absheap[abs(a)]=[1,0]
                
