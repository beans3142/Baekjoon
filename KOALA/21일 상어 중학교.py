# bfs를 통해 얻어내야 할 값 (크기,무지개 블록 수,
# 행이 가장 작은 = 가장 왼쪽 그리고 열의 번호가 가 작은, (x,y)순으로 sort 하면 될 것
# 

from sys import stdin
from collections import deque
input=stdin.readline

n,m=map(int,input().split())
dx=[0,0,1,-1]
dy=[1,-1,0,0]

board=[list(map(int,input().split())) for i in range(n)]

def bfs(X,Y,color):
    global board,visited
    queue=deque([[X,Y]])
    size=1
    locate=[[Y,X]]
    cnt_rainbow=0
    locate_rainbow=[]
    #print('실행됨')
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if board[ny][nx]==color and visited[ny][nx]==0:
                    visited[ny][nx]=1
                    locate.append([ny,nx])
                    size+=1
                    queue.append([nx,ny])
                elif board[ny][nx]==0 and visited[ny][nx]==0:
                    #print(ny,nx)
                    visited[ny][nx]=1
                    locate_rainbow.append([ny,nx])
                    cnt_rainbow+=1
                    size+=1
                    queue.append([nx,ny])

    for y,x in locate_rainbow:
        visited[y][x]=0
    #print(size)
    #print(cnt_rainbow,'무지개')
    ''',cnt_rainbow,sorted(located))'''
    if size>1:
        return (size,cnt_rainbow,sorted(locate),locate_rainbow)
    return False
                    
'''
def gravity(): # 중력 구현
    for i in range(n):
        for j in range(1,n):
            if board[~j][i]!='-1' and board[~j][i]!=None and board[~j+1][i]==None:
                try:
                    while j>=0 and board[~j+1][i] == None:
                        board[~j][i],board[~j+1][i]=board[~j+1][i],board[~j][i]
                        j-=1
                except:
                    pass
'''
def gravity():
    for i in range(n-1,-1,-1):
        for j in range(n):
            if board[i][j]>=0:
                start=i
                while True:
                    if 0<=start+1<n:
                        if board[start+1][j]==-2:
                            board[start+1][j]=board[start][j]
                            board[start][j]=-2
                            start+=1
                        else:
                            break
                    else:
                        break

def showboard():
    for i in range(n):
        for j in range(n):
            print(board[i][j]if board[i][j]!=-2 else 'X',end='\t'if j!=n-1 else '\n')

def rotate(): # 회전 구현
    global board
    rotated_board=[[0 for i in range(n)]for j in range(n)]
    for i in range(n):
        for j in range(n):
            rotated_board[n-j-1][i]=board[i][j]
    board=rotated_board
'''
showboard()
gravity()
print()
showboard()
board=rotate()
print()
showboard()
gravity()
print()
showboard()
'''
t=1
totalscore=0

while True:
    scoreboard=[]
    visited=[[0 for i in range(n)]for j in range(n)]
    for i in range(n):
        for j in range(n):
            if 0<board[i][j] and visited[i][j]==0:
                visited[i][j]=1
                a=bfs(j,i,board[i][j])
                if a:
                    scoreboard.append(a)

    if not scoreboard:
        print(totalscore)
        break
    #print(scoreboard)
    mx_size,mx_rainbow,block_used,rainbow_block_used=sorted(scoreboard,reverse=True)[0]
    totalscore+=mx_size**2
    for y,x in block_used+rainbow_block_used:
        board[y][x]=-2
    
    if True:
        #print(t,end='\n\n')
        #showboard()
        gravity()
        #print('g')
        #showboard()
        rotate()
        #print('r')
        #showboard()
        gravity()
        #print('g')
        #showboard()
        #print()
        #print()
        #t+=1
    
    '''
    gravity()
    rotate()
    gravity()
'''
'''
test case
5 3
2 2 -1 3 -1
None None 2 0 -1
None None None 1 2
-1 None 1 3 2
None None 2 2 1
'''
