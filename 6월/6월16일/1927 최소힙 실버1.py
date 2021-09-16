from collections import deque
from sys import stdin
input=stdin.readline

n=int(input())

heap={}

for i in range(n):
    x=int(input())
    if x==0 and heap:
        pass#dfs(x)
    elif x!=0 and not heap:
        head=x
        heap={x:[0,0]}
    elif x!=0 and heap:
        now=int(head)
        newhead=int(head)
        while x!=0 and now!=0:
            if now<x:
                heap[x]=[heap[now][0],now]
                x=now
            else:
                if heap[now][0]==0:
                    heap[now][0]=x
                    heap[x]=[0,0]
                elif heap[now][1]==0:
                    if heap[now][0]>x:
                        heap[now]=[x,heap[now][0]]
                    else:
                        heap[now]=[heap[now][0],x]
                    heap[x]=[0,0]
                else:
                    now=heap[now][0]
    print(heap)
