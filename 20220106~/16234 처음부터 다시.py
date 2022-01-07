from sys import stdin
from collections import deque
input=stdin.readline
dx=[1,-1,0,0]
dy=[0,0,1,-1]

n,l,r=map(int,input().split())
m=[]

for i in range(n):
    m.append(list(map(int,input().split())))


def bfs(X,Y):
    loc=[]
    queue=deque([[X,Y]])
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            
