from sys import stdin
from collections import deque
input=stdin.readline

n,m=map(int,input().split())
matrix=[input().rstrip() for i in range(n)]

def bfs(n,m):
    queue=deque([(0,0,0)]) # x, y 벽 부숨 여부
    move=1
    vi=[[0 for i in range(m)]for j in range(n)]
    vi[0][0]=2
    while queue:
        le=len(queue)
        for i in range(le):
            x,y,useAxe=queue.popleft()
            if x==m-1 and y==n-1:
                return move
            for nx,ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                if -1<nx<m and -1<ny<n:
                    if vi[ny][nx]!=2 and useAxe==0:
                        if matrix[ny][nx]=='0':
                            queue.append((nx,ny,0))
                        else:
                            queue.append((nx,ny,1))
                        vi[ny][nx]=2
                    else:
                        if matrix[ny][nx]=='0' and vi[ny][nx]==0:
                            queue.append((nx,ny,1))
                            vi[ny][nx]=1
        move+=1
    return -1

print(bfs(n,m))
