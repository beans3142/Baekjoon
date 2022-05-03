from itertools import combinations
from collections import deque

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def check(arr):
    global ans
    if connected(arr):
        cnt=0
        for x,y in arr:
            cnt+=matrix[y][x]=='A'
        if cnt>=4:
            ans+=1

def connected(arr):
    for x,y in arr:
        vi[y][x]=1
    res=bfs(x,y)
    for x,y in arr:
        vi[y][x]=0
    return res

def bfs(x,y):
    queue=deque([(x,y)])
    cnt=1
    vi[y][x]=2
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if -1<nx<5 and -1<ny<5:
                if vi[ny][nx]==1:
                    vi[ny][nx]=2
                    cnt+=1
                    queue.append([nx,ny])
    if cnt==7:
        return True
    return False



ans=0
arr=[[(i,j) for i in range(5)] for j in range(5)]
xy=[]
vi=[[0]*5 for i in range(5)]
for i in arr:
    xy+=i

case=list(combinations(xy,7))

matrix=[input() for i in range(5)]

for i in case:
    check(i)

print(ans)
