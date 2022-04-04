from sys import stdin,maxsize
from heapq import heappop,heappush
input=stdin.readline
inf=maxsize

n=int(input())

arr=[list(map(int,input().split())) for i in range(n)]
val=[[inf]*n for i in range(n)]
val[0][0]=0

for i in range(n):
    for j in range(n):
        if i==n-1 and j==n-1:
            break
        if i!=n-1:
            if arr[i+1][j]>=arr[i][j]:
                cost=arr[i+1][j]-arr[i][j]+1
                val[i+1][j]=min(val[i+1][j],cost+val[i][j])
            else:
                val[i+1][j]=min(val[i+1][j],val[i][j])
        if j!=n-1:
            if arr[i][j+1] >= arr[i][j]:
                cost=arr[i][j+1]-arr[i][j]+1
                val[i][j+1]=min(val[i][j+1],val[i][j]+cost)
            else:
                val[i][j+1]=min(val[i][j+1],val[i][j])

print(val[-1][-1])
