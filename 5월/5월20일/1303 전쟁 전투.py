import sys
from collections import *

input=sys.stdin.readline

a,b=map(int,input().split())

field=[[0]* (a+2)] + [[0]+list(input())[:-1]+[0] for i in range(b)] + [[0]*(a+2)]
visited=[[False for i in range(a+2)] for i in range(b+2)]

cnt=1
w=0
e=0

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def bfs(x,y):
    global cnt,queue
    if visited[y][x]==False:
        cnt+=1
    visited[y][x]=True
    queue=[[x,y]]
    queue=deque(queue)
    while queue:
        x,y=queue.popleft()
        visited[y][x]=True
        for i in range(4):
            if visited[y+dy[i]][x+dx[i]]==False and field[y][x]==field[y+dy[i]][x+dx[i]]:
                queue.append([y+dy[i],x+dx[i]])
        for i in queue:
            bfs(i[1],i[0])
    return cnt
    

for k in range(1,b+1):
    for l in range(1,a+1):
        cnt=0
        if not visited[k][l]:
            bfs(l,k)
            if field[k][l]=='W':
                w+=cnt**2
            else:
                e+=cnt**2

print(w,e)
                
            
        
        
    
