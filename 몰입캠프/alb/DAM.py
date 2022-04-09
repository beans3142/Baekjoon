from sys import stdin
from collections import deque
input=stdin.readline

n=int(input())
matrix=[list(map(int,input().split())) for i in range(n)]
sx,sy=map(int,input().split())
k=int(input())

vi=[[0 for i in range(n)] for j in range(n)]
queue=deque([(sx-1,sy-1)])
time=0
vi[sy-1][sx-1]=1
while queue:
    le=len(queue)
    for i in range(le):
        x,y=queue.popleft()
        for nx,ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
            if -1<nx<n and -1<ny<n:
                if vi[ny][nx]==0 and matrix[ny][nx]==0:
                    vi[ny][nx]=1
                    queue.append((nx,ny))
    time+=1
    if time>=k:
        break
if len(queue)==0:
    print(-1)
else:
    print(len(queue))
