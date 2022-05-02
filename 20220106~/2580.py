from sys import stdin
input=stdin.readline

def getloc(x,y):
    return x//3+y//3*3

def bt(idx,cnt):
    if cnt==len(loc):
        for i in matrix:
            print(*i)
        exit()
    x,y=loc[idx]
    for k in range(1,10):
        if check(x,y,k):
            update(x,y,k)
            bt(idx+1,cnt+1)
            update(x,y,0)

def check(x,y,val):
    if area[getloc(x,y)][val]==garo[x][val]==sero[y][val]==0:
        return True
    return False

def update(j,i,val):
    if val!=0:
        matrix[i][j]=val
    area[getloc(j,i)][matrix[i][j]]=val
    sero[i][matrix[i][j]]=val
    garo[j][matrix[i][j]]=val
    if val==0:
        matrix[i][j]=val

def fill(x,y):
    able=[0]*(10)
    for i in area[getloc(x,y)]:
        able[i]=1
    for i in garo[x]:
        able[i]=1
    for i in sero[y]:
        able[i]=1
    return able
        

area=[[0]*10 for i in range(9)]
garo=[[0]*10 for i in range(9)]
sero=[[0]*10 for i in range(9)]
loc=[]

matrix=[[*map(int,input().split())] for i in range(9)]
fillleft=0

for i in range(9):
    for j in range(9):
        area[getloc(j,i)][matrix[i][j]]=matrix[i][j]
        sero[i][matrix[i][j]]=matrix[i][j]
        garo[j][matrix[i][j]]=matrix[i][j]
        if matrix[i][j]==0:
            loc.append((j,i))

bt(0,0)


'''
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
'''
