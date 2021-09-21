from sys import stdin
from collections import deque
input=stdin.readline
n=int(input())
a=input().rstrip()
zomloc=deque([])
dx=[0,-1,0,1,1,1,-1,-1,0]
dy=[-1,0,1,0,-1,1,-1,1,0]
move=2
light=[[0 for i in range(n)]for i in range(n)]
s=[list(input().rstrip()) for i in range(n)]
ahri=[0,0]
zom_meet=False

for i in range(n):
    for j in range(n):
        if s[i][j]=='Z':
            zomloc.append([j,i,2])
        if s[i][j]=='S':
            s[i][j]='O'
            light[i][j]=2


def switch_on(x,y):
    for i in range(9):
        nx=x+dx[i]
        ny=y+dy[i]
        if -1<nx<n and -1<ny<n:
            light[ny][nx]=1 if light[ny][nx]!=2 else 3

def zom_move():
    global zom_meet,zomloc,s
    re=len(zomloc)
    for i in range(re):
        zomx,zomy,zomsee=zomloc.popleft()
        nexty=zomy+dy[zomsee]
        if light[zomy][zomx]%2!=1:
            if ahri[0]==zomx and ahri[1]==zomy:
                zom_meet=True
                return
        if -1<nexty<n:
            zomloc.append([zomx,nexty,zomsee])
            if light[nexty][zomx]%2==1:
                continue
            if ahri[0]==zomx and ahri[1]==nexty:
                zom_meet=True
                return
        else:
            zomsee=(zomsee+2)%4
            zomloc.append([zomx,zomy,zomsee])

for i in range(len(a)):
    if a[i]=='R':
        move=(move-1 if move>0 else 3)%4
    elif a[i]=='L':
        move=(move+1)%4
    else:
        nx=ahri[0]+dx[move]
        ny=ahri[1]+dy[move]
        if -1<nx<n and -1<ny<n:
            ahri[0]=nx
            ahri[1]=ny
            if light[ny][nx]>1:
                switch_on(nx,ny)
    s[ahri[1]][ahri[0]]='A'
    zom_move()
    if zom_meet:
        break
if zom_meet:
    print("Aaaaaah!")
else:
    print("Phew...")

