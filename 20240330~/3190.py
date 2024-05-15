from sys import stdin
from collections import *
input=stdin.readline

dx=[1,0,-1,0]
dy=[0,1,0,-1]

n=int(input())
k=int(input())
arr=[[0]*n for i in range(n)]
arr[0][0]=1
q=deque([(0,0)])
cd={}

for i in range(k):
    a,b=map(int,input().split())
    arr[a-1][b-1]=2

l=int(input())
for i in range(l):
    T,D=input().rstrip().split()
    cd[int(T)]=1 if D=="D" else -1
    
t=0
d=1000
while q:
    if t in cd:
        d+=cd[t]
    eatapple=False
    x,y=q[-1]
    nx=x+dx[d%4]
    ny=y+dy[d%4]
    if -1<nx<n and -1<ny<n:
        if arr[ny][nx]==0:
            arr[ny][nx]=1
            q.append((nx,ny))
        elif arr[ny][nx]==2:
            arr[ny][nx]=1
            eatapple=True
            q.append((nx,ny))
        else:
            print(t+1)
            exit()
    else:
        print(t+1)
        exit()
    if not eatapple:
        x,y=q.popleft()
        arr[y][x]=0
    t+=1

print(t)
