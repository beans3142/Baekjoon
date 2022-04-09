from sys import stdin
input=stdin.readline

n=int(input())

board=[[0 for i in range(n)] for i in range(n)]

cnt=0

def fill(x,y,typ):
    for i in range(n):
        if i!=x:
            board[y][i]+=typ
        if i!=y:
            board[i][x]+=typ
        
    for i in range(1,n-y):
        if x+i<n:
            board[y+i][x+i]+=typ
        if x-i>-1:
            board[y+i][x-i]+=typ

    for i in range(1,y+1):
        if x+i<n:
            board[y-i][x+i]+=typ
        if x-i>-1:
            board[y-i][x-i]+=typ

    board[y][x]+=typ

def bt(nowline):
    global cnt
    if nowline==n:
        cnt+=1
        return
    for i in range(n):
        if board[nowline][i]==0:
            fill(i,nowline,1)
            bt(nowline+1)
            fill(i,nowline,-1)

bt(0)

print(cnt)
