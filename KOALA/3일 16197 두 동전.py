from sys import stdin
input=stdin.readline

dx,dy=[0,0,1,-1],[1,-1,0,0]

n,m=map(int,input().split())
board=[list(input().rstrip()) for i in range(n)]
vi1=[[0 for i in range(m)]for i in range(n)]
vi2=[[0 for i in range(m)]for i in range(n)]

coins=[]
ans=11

for i in range(n):
    for j in range(m):
        if board[i][j]=='o':
            coins.append((j,i))

def dfs(coin1,coin2,tmpt):
    global ans
    if tmpt>10:
        return
    coin1_moved=False
    coin2_moved=False
    for i in range(4):
        fallen=0
        nx1=coin1[0]+dx[i]
        ny1=coin1[1]+dy[i]
        nx2=coin2[0]+dx[i]
        ny2=coin2[1]+dy[i]
        if nx1<0 or ny1<0 or nx1>=m or ny1>=n:
            fallen+=1
        if nx2<0 or ny2<0 or nx2>=m or ny2>=n:
            fallen+=1
        if fallen==1:
            ans=min(ans,tmpt+1)
            continue
        elif fallen==2:
            continue
        elif ny1==ny2 and nx1==nx2:
            continue
        if board[ny1][nx1]=='#':
            nx1=coin1[0]
            ny1=coin1[1]
        if board[ny2][nx2]=='#':
            nx2=coin2[0]
            ny2=coin2[1]
        if board[ny1][nx1]=='.' and vi1[ny1][nx1]==0:
            board[ny1][nx1],board[coin1[1]][coin1[0]]=board[coin1[1]][coin1[0]],board[ny1][nx1]
            vi1[ny1][nx1]=1
            coin1_moved=True
        if board[ny2][nx2]=='.' and vi2[ny2][nx2]==0:
            board[ny2][nx2],board[coin2[1]][coin2[0]]=board[coin2[1]][coin2[0]],board[ny2][nx2]
            vi2[ny2][nx2]=1
            coin2_moved=True
        dfs((nx1,ny1),(nx2,ny2),tmpt+1)
        if coin1_moved:
            board[ny1][nx1],board[coin1[1]][coin1[0]]=board[coin1[1]][coin1[0]],board[ny1][nx1]
            vi1[ny1][nx1]=0
        if coin2_moved:
            board[ny2][nx2],board[coin2[1]][coin2[0]]=board[coin2[1]][coin2[0]],board[ny2][nx2]
            vi2[ny2][nx2]=0
            
            
dfs(coins[0],coins[1],0)
        
        
print(ans if ans!=11 else -1)
