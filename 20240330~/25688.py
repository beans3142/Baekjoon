from sys import stdin
from itertools import permutations
input=stdin.readline
from collections import deque

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs(queue):
    while queue:
        mov,x,y,idx=queue.popleft()
        if order[idx]==arr[y][x]:
            idx+=1
            if idx==6:
                return mov
        tar=order[idx]
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if -1<nx<5 and -1<ny<5:
                if arr[ny][nx]!=-1 and vi[tar][ny][nx]==-1:
                    vi[tar][ny][nx]=mov+1
                    queue.append((mov+1,nx,ny,idx))
    return 1e10


    

arr=[list(map(int,input().split())) for i in range(5)]
s,e=map(int,input().split())
orders=list(permutations(range(1,7)))
ans=1e10
for order in orders:
    vi=[[[-1]*5 for i in range(5)] for i in range(7)]
    queue=deque([(0,e,s,0)])
    ans=min(ans,bfs(queue))
    
print(ans if ans!=1e10 else -1)
