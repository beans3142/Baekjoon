import sys
from collections import deque
input=sys.stdin.readline

sdoku=[list(map(int,input().rstrip().split())) for i in range(9)]
sector=[[] for i in range(9)]
element={}

for x in range(9):
    for y in range(9):
        sector[3*(y//3)+x//3].append((x,y))

for i in range(9):
    for xy in sector[i]:
        element[xy]=i
'''
def fill(locate,arr):
    queue=deque([])
    queue.append(arr)
    #print(locate)
    while True:
        X,Y=locate.popleft()
        l=len(queue)
        #print(locate,queue)
        for i in range(l):
            S=queue.popleft()
            print(i)
            a=check(X,Y,S)
            if a:
                for i in a:
                    S[Y][X]=i
                    queue.append(S)
        if not locate:
            break
    return queue[0]
'''

def dfs(x):
    if x==len(locate):
        for row in sdoku:
            print(*row)
        exit()
    else:
        X,Y=locate[x]
        able=check(X,Y)
        for i in able:
            sdoku[Y][X]=i
            dfs(x+1)
            sdoku[Y][X]=0
            
    
    

def check(x,y):
    to_check=[1 for i in range(9)]
    able=[]
    for X,Y in sector[element[(x,y)]]:
        if sdoku[Y][X] != 0:
            to_check[sdoku[Y][X]-1]=0

    for Y in range(9):
        if sdoku[Y][x]!=0:
            to_check[sdoku[Y][x]-1]=0

    for X in range(9):
        if sdoku[y][X]:
            to_check[sdoku[y][X]-1]=0

    for i in range(9):
        if to_check[i]==1:
            able.append(i+1)

    return able

locate=[]
for i in range(9):
    for j in range(9):
        if sdoku[i][j]==0:
            locate.append((j,i))

arr=dfs(0)
