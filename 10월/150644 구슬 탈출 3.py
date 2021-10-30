from sys import stdin
from collections import deque
input=stdin.readline

dx=[1,-1,0,0]
dy=[0,0,-1,1]
direction={0:"R",1:"L",2:"U",3:"D"}

n,m=map(int,input().split())

arr=[list(input().rstrip()) for i in range(n)]

for i in range(n):
    for j in range(m):
        if arr[i][j]=='B':
            bx,by=j,i
            arr[i][j]='.'
        if arr[i][j]=='R':
            rx,ry=j,i
            arr[i][j]='.'
        if arr[i][j]=='O':
            lx,ly=j,i

def is_first(x1,y1,x2,y2,h):
    if h==0:
        if x1>x2:
            return 'R'
        return 'B'
    if h==1:
        if x1>x2:
            return 'B'
        return 'R'
    if h==2:
        if y1>y2:
            return 'B'
        return 'R'
    if h==3:
        if y1>y2:
            return 'R'
        return 'B'

def bfs(x1,y1,x2,y2,rpt):
    queue=deque([[x1,y1,x2,y2,rpt,[]]])
    end=False
    while queue:
        rx,ry,bx,by,rpt,move=queue.popleft()
        if rpt==10:
            return []
        for i in range(4):
            order=is_first(rx,ry,bx,by,i)
            end=0
            if order=='R':
                
                rnx=rx
                rny=ry
                rbx=bx
                rby=by
                
                while arr[rny+dy[i]][rnx+dx[i]]!='#':
                    rnx+=dx[i]
                    rny+=dy[i]
                    if rny==ly and rnx==lx:
                        end=1
                if end!=1:
                    arr[rny][rnx]='#'

                while arr[rby+dy[i]][rbx+dx[i]]!='#':
                    rbx+=dx[i]
                    rby+=dy[i]
                    if rby==ly and rbx==lx:
                        end=-1


                if arr[rny][rnx]=='#':
                    arr[rny][rnx]='.'

                if end==1:
                    return move+[direction[i]]
                if end==-1:
                    continue
                if rnx==rx and rny == ry and rby == by and rbx==bx:
                    continue
    
                queue.append([rnx,rny,rbx,rby,rpt+1,move+[direction[i]]]) 
                
            else:
                
                rbx=bx
                rby=by
                
                while arr[rby+dy[i]][rbx+dx[i]]!='#':
                    rbx+=dx[i]
                    rby+=dy[i]
                    if rby==ly and rbx==lx:
                        end=-1

                if end==-1:
                    continue
                
                arr[rby][rbx]='#'
                
                rnx=rx
                rny=ry
                
                while arr[rny+dy[i]][rnx+dx[i]]!='#':
                    rnx+=dx[i]
                    rny+=dy[i]
                    if rny==ly and rnx==lx:
                        end=1

                arr[rby][rbx]='.'

                if end==1:
                    return move+[direction[i]]
                if rnx==rx and rny == ry and rby == by and rbx==bx:
                    continue

                queue.append([rnx,rny,rbx,rby,rpt+1,move+[direction[i]]]) 

    return []

ans=bfs(rx,ry,bx,by,0)

if ans:
    print(len(ans))
    print(''.join(ans))
else:
    print(-1)
