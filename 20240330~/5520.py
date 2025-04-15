from collections import deque
from copy import deepcopy
def getkey(arr):
    base=1
    for i in arr:
        for j in i:
            base=base*10+j
    return base
    
dx=[[0,1,-1,0,0],[-1,0,1],[0,0,0],[0,-1,-1,-1,1,1,1,0,0]]
dy=[[0,0,0,-1,1],[0,0,0],[1,0,-1],[1,1,0,-1,1,0,-1,-1,0]]
rev=[0,3,1,3,2,0,2,3,1,3]
start=[list(map(int,input().split())) for i in range(3)]
q=deque([(start,[])])
vi=set()
while q:
    now,mov=q.popleft()
    if now==[[0,0,0],[0,0,0],[0,0,0]]: break
    for y in range(3):
        for x in range(3):
            copy=[[i for i in j] for j in now]
            loc=rev[y*3+x+1]
            for i in range(len(dx[loc])):
                nx=x+dx[loc][i]
                ny=y+dy[loc][i]
                if -1<nx<3 and -1<ny<3:
                    copy[ny][nx]+=1
                    copy[ny][nx]%=4
            key=getkey(copy)
            if key not in vi:
                vi.add(key)
                q.append((copy,mov+[y*3+x+1]))
print(*mov)
