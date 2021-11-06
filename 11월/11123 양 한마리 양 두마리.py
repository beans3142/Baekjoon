from sys import stdin
from collections import deque
input=stdin.readline
dx=[0,0,-1,1]
dy=[1,-1,0,0]

for _ in range(int(input())):
    h,w=map(int,input().split())
    mat=[list(input().rstrip()) for i in range(h)]
    cnt=0
    for i in range(h):
        for j in range(w):
            if mat[i][j]=='#':
                queue=deque([[j,i]])
                cnt+=1
                while queue:
                    x,y=queue.popleft()
                    for k in range(4):
                        nx=x+dx[k]
                        ny=y+dy[k]
                        if -1<nx<w and -1<ny<h and mat[ny][nx]=='#':
                            mat[ny][nx]='.'
                            queue.append([nx,ny])
                            
    print(cnt)
