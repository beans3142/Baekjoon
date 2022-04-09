from sys import *
from collections import *
setrecursionlimit(100000)
input=stdin.readline

dx=[0,0,1,-1]
dy=[1,-1,0,0]

vi=[0]*92
r,c=map(int,input().split())
arr=[[ord(i) for i in input().rstrip()] for i in range(r)]
cnt=0
ans=1

def bt(x,y):
    global ans,cnt
    cnt+=1
    ans=max(ans,cnt)
    if ans==26:
        print(ans)
        exit()
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if -1<nx<c and -1<ny<r:
            if vi[arr[ny][nx]]==0:
                vi[arr[ny][nx]]=1
                bt(nx,ny)
    cnt-=1
    vi[arr[y][x]]-=1

vi[arr[0][0]]=1               
bt(0,0)

print(ans)
