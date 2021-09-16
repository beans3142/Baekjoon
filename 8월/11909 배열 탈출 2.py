from sys import stdin,maxsize
from heapq import heappop,heappush
input=stdin.readline
inf=maxsize

n=int(input())

arr=[list(map(int,input().split())) for i in range(n)]
val=[[inf]*n for i in range(n)]

queue=[[0,arr[0][0],0,0]]


while queue:
    s,v,x,y=heappop(queue)
    if val[x][y]<s:
        continue
    val[x][y]=s
    if x==n-1 and y==n-1:
        break
    nx=x+1
    ny=y+1
    if x+1<n:
        cost=0 if arr[y][x+1]<v else arr[y][x+1]-v+1
        if val[y][x+1]>s+cost:
            heappush(queue,[s+cost,arr[y][x+1],x+1,y])
    if y+1<n:
        cost=0 if arr[y+1][x]<v else arr[y+1][x]-v+1
        if val[y+1][x]>s+cost:
            heappush(queue,[s+cost,arr[y+1][x],x,y+1])
        
print(val[-1][-1])
