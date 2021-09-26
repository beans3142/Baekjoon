from sys import stdin
from collections import defaultdict
input=stdin.readline
r,c=map(int,input().split())
arr=[list(map(lambda x: ord(x)-65,input().rstrip())) for i in range(r)]
dx=[0,0,-1,1]
dy=[1,-1,0,0]
vi=[0]*26
vi[arr[0][0]]=1
ans=1
def sol(x,y,l):
    global ans
    ans=max(ans,l)
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if -1<nx<c and -1<ny<r:
            if vi[arr[ny][nx]]==0:
                vi[arr[ny][nx]]=1
                sol(nx,ny,l+1)
                vi[arr[ny][nx]]=0

sol(0,0,1)
print(ans)
