from sys import *
from collections import *
#from math import *
#from itertools import *
#from heapq import *
#from bisect import *
#setrecursionlimit(100000)
dx=[0,0,1,-1]
dy=[1,-1,0,0]
input=stdin.readline

r,c=map(int,input().split())
arr=[list(input().rstrip()) for i in range(r)]
vi=[[0 for i in range(c)] for i in range(r)]
water=deque([])
for i in range(r):
    for j in range(c):
        if arr[i][j]=='S':
            sx,sy=j,i
            arr[i][j]='.'
        elif arr[i][j]=='*':
            water.append((j,i))
        elif arr[i][j]=='D':
            ex,ey=j,i
queue=deque([(sx,sy)])
vi[sy][sx]=1
move=0
escape=False

while queue:

    le=len(water)
    for _ in range(le):
        wx,wy=water.popleft()
        for i in range(4):
            nwx=wx+dx[i]
            nwy=wy+dy[i]
            if -1<nwx<c and -1<nwy<r:
                if arr[nwy][nwx]=='.':
                    arr[nwy][nwx]='*'
                    water.append((nwx,nwy))
    le=len(queue)
    for _ in range(le):
        x,y=queue.popleft()
        if x==ex and y==ey:
            escape=True
            ans=move
            break

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if -1<nx<c and -1<ny<r:
                if vi[ny][nx]==0 and arr[ny][nx]!='*' and arr[ny][nx]!='X':
                    vi[ny][nx]=1
                    queue.append((nx,ny))
    if escape:
        break
    move+=1
'''
    for i in vi:
        print(*i)
    print()
    for i in arr:
        print(*i)
    print()
'''

if escape:
    print(ans)
else:
    print('KAKTUS')
