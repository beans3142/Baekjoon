from sys import stdin
from collections import deque
input=stdin.readline

n=int(input())
dx=[0,-1,1,0]
dy=[-1,0,0,1]
sea=[[0]for i in range(n)]
d=['▲','◀','▶','▼']

for i in range(n):
    sea[i]=list(map(int,input().split()))
    try:
        shark_x=sea[i].index(9)
        shark_y=i
        sea[shark_y][shark_x]=0
    except:
        pass

def shark(x,y,size,eat,move,v):
    queue=deque([[x,y,size,eat,move,v]])
    mn=10000000
    #V=[[0 for i in range(n)]for j in range(n)]
    while queue:
        #print(queue)
        X,Y,S,E,M,V=queue.popleft()
        V[Y][X]=1
        if mn<M:
            continue
        for i in range(4):
            nx=X+dx[i]
            ny=Y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if V[ny][nx]==0:
                    if 0<sea[ny][nx]<S:
                        sea[ny][nx]=0
                        #print(d[i],M+1,end=' ')
                        mn=M
                        if E==S-1:
                            queue.append([nx,ny,S+1,0,M+1,[[0 for i in range(n)]for j in range(n)]])
                        else:
                            queue.append([nx,ny,S,E+1,M+1,[[0 for i in range(n)]for j in range(n)]])
                    elif sea[ny][nx]==0 or sea[ny][nx]==S:
                        queue.append([nx,ny,S,E,M+1,V])
    return move

print(shark(shark_x,shark_y,2,0,0,[[0 for i in range(n)]for j in range(n)]))

                    
