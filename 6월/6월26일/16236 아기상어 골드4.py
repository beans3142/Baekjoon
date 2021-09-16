import sys
#from collections import deque
input=sys.stdin.readline

n=int(input())
sea=[list(map(int,input().split())) for i in range(n)]
dx,dy=[0,0,1,-1],[1,-1,0,0]


def where_is_shark():
    for i in range(n):
        for j in range(n):
            if sea[i][j]==9:
                return i,j

def shark_move(locate,move,size,eat):
    global sea
    queue=[[move,-size,-eat,locate]]
    reset=False
    eated=False
    second=0
    sea[locate[0]][locate[1]]=0
    visited=[[0 for i in range(n)]for _ in range(n)]
    while queue:
        queue.sort()
        t,S,E,xy=queue.pop(0)
        if S==E:
            S-=1
            E=0
        y,x=xy
        if eated:
            sea[y][x]=0
            eated=False
        if reset:
            queue=[]
            reset=False
            visited=[[0 for i in range(n)]for _ in range(n)]
        visited[y][x]=1
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if 1<=sea[ny][nx]<-S:
                    queue.append([t-1,S,E-1,(ny,nx)])
                    eated=True
                    second=t
                    reset=True
                elif visited[ny][nx]==0 and (sea[ny][nx]==-S or sea[ny][nx]==0):
                    queue.append([t-1,S,E,(ny,nx)])
    return second
                
print(shark_move(where_is_shark(),0,2,0))
