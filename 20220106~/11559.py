from sys import stdin
from collections import deque
input=stdin.readline

dx=[0,0,1,-1]
dy=[1,-1,0,0]
arr=[list(input().rstrip()) for i in range(12)]
v=[[0 for i in range(6)] for i in range(12)]

chain=0
keep_chain=True

def bfs(X,Y):
    global v
    queue=deque([[X,Y]])
    v[Y][X]=chain+1
    cnt=1
    region=[[X,Y]]
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if -1<nx<6 and -1<ny<12:
                if arr[ny][nx]==arr[y][x] and v[ny][nx]<=chain:
                    v[ny][nx]=chain+1
                    cnt+=1
                    queue.append([nx,ny])
                    region.append([nx,ny])
    return cnt,region
                
    
while keep_chain:
    '''
    for i in arr:
        print(i)
    print()
    '''
    keep_chain=False
    to_break=[]

    # 부서질 공간 찾고 부수기
    for x in range(6):
        for y in range(12):
            if arr[y][x]!='.' and v[y][x]<=chain:
                cnt,zone=bfs(x,y)
                if cnt>3:
                    keep_chain=True
                    for X,Y in zone:
                        arr[Y][X]='.'

    # 중력 작용
    for x in range(6):
        line=[]
        for y in range(12):
            if arr[~y][x]!='.':
                line.append(arr[~y][x])
                arr[~y][x]='.'
        for y in range(len(line)):
            arr[~y][x]=line[y]
    
    if keep_chain:
        chain+=1
            

print(chain)
