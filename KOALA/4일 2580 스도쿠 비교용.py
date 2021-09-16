import sys
input=sys.stdin.readline

sdoku=[list(map(int,input().split())) for i in range(9)]
sector=[[] for i in range(9)]

for x in range(9):
    for y in range(9):
        sector[3*(y//3)+x//3].append((x,y))

def dfs(x):
    try:
        X,Y=locate[x]
        able=check(X,Y)
        for i in range(9):
            if able[i]==1:
                sdoku[Y][X]=i+1
                dfs(x+1)
                sdoku[Y][X]=0
    except:
        for row in sdoku:
            print(*row)
        quit()
        
def check(x,y):
    to_check=[1]*9
    able=[]
    for X,Y in sector[3*(y//3)+x//3]:
        if sdoku[Y][X] != 0:
            to_check[sdoku[Y][X]-1]=0

    for l in range(9):
        if sdoku[l][x]!=0:
            to_check[sdoku[l][x]-1]=0
        if sdoku[y][l]:
            to_check[sdoku[y][l]-1]=0 
    return to_check

locate=[]
for i in range(9):
    for j in range(9):
        if sdoku[i][j]==0:
            locate.append((j,i))

dfs(0)
