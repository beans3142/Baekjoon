import sys
input=sys.stdin.readline

sdoku=[list(map(int,input().split())) for i in range(9)]
sector=[[] for i in range(9)]

for x in range(9):
    for y in range(9):
        sector[3*(y//3)+x//3].append((x,y))

def dfs(x):
    X,Y=locate[x]
    able=check(X,Y)
    for i in range(1,10):
        if able[i]==1:
            sdoku[Y][X]=i
            dfs(x+1)
            sdoku[Y][X]=0
            
def check(x,y):
    to_check=[1]*10
    for X,Y in sector[3*(y//3)+x//3]:
        to_check[sdoku[Y][X]]=0

    for l in range(9):
        to_check[sdoku[l][x]]=0
        to_check[sdoku[y][l]]=0 
    return to_check

locate=[]
for i in range(9):
    for j in range(9):
        if sdoku[i][j]==0:
            locate.append((j,i))
try:
    dfs(0)
except:
    for i in range(9):
        print(*sdoku[i])
