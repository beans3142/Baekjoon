from sys import stdin
from collections import deque,defaultdict
input=stdin.readline

dx=[1,-1,0,0]
dy=[0,0,-1,1]

n,m=map(int,input().split())

arr=[list(input().rstrip()) for i in range(n)]

v=defaultdict(int)

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

def pa(x1,y1,x2,y2):
    print()
    for i in range(n):
        for j in range(m):
            if i==y1 and j==x1:
                print('R',end='')
            elif i==y2 and j==x2:
                print('B',end='')
            else:
                print(arr[i][j],end='')
        print()
    print()

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
    queue=deque([[x1,y1,x2,y2,rpt]])
    end=False
    while queue:
        rx,ry,bx,by,rpt=queue.popleft()
        if v[rx,ry,bx,by]==1:
            continue
        v[rx,ry,bx,by]=1
        for i in range(4):
            order=is_first(rx,ry,bx,by,i)
            end=0
            if order=='R':
                
                rnx=rx
                rny=ry
                rbx=bx
                rby=by
                
                #pa(rnx,rny,rbx,rby)
                
                while arr[rny+dy[i]][rnx+dx[i]]!='#':
                    rnx+=dx[i]
                    rny+=dy[i]
                    if rny==ly and rnx==lx:
                        #print('ex')
                        end=1
                if end!=1:
                    arr[rny][rnx]='#'

                #pa(rnx,rny,rbx,rby)
                
                while arr[rby+dy[i]][rbx+dx[i]]!='#':
                    rbx+=dx[i]
                    rby+=dy[i]
                    if rby==ly and rbx==lx:
                        end=-1

                #pa(rnx,rny,rbx,rby)

                if arr[rny][rnx]=='#':
                    arr[rny][rnx]='.'

                if end==1:
                    return rpt+1
                if end==-1:
                    continue
                if rnx==rx and rny == ry and rby == by and rbx==bx:
                    continue
    
                queue.append([rnx,rny,rbx,rby,rpt+1]) 
                
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
                        #print('ex')
                        end=1

                arr[rby][rbx]='.'

                if end==1:
                    return rpt+1
                if rnx==rx and rny == ry and rby == by and rbx==bx:
                    continue

                queue.append([rnx,rny,rbx,rby,rpt+1]) 

    return -1

ans=bfs(rx,ry,bx,by,0)

print(ans)
