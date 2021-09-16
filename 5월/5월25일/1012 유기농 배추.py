#default template
#------------------------
#import sys
#import math
#import os
#import time
#from collections import *
#input=sys.stdin.readline
#dx=[1,-1,0,0] ; dy=[0,0,1,-1]
#visited=[[False for i in range()]for j in range()]
#arr=list(map(int,input().split()))
#arr=[int(input()) for i in range()]
#arr=[list(map(int,input().split()))for i in range()]
#arr=[]
#------------------------

import sys
input=sys.stdin.readline

sys.setrecursionlimit(10**6)

dx=[1,-1,0,0] ; dy=[0,0,1,-1]

def dfs(x,y):
    field[y][x]=0
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<m and 0<=ny<n:
            if field[ny][nx]==1:
                field[ny][nx]=0
                dfs(nx,ny)
                
t=int(input())

for i in range(t):
    m,n,k=map(int,input().split())
    result=0
    field=[[0 for i in range(m)]for _ in range(n)]
    for _ in range(k):
        a,b=map(int,input().split())
        field[b][a]=1
    #visited=[[False for i in range(m)]for j in range(n)]
    for Y in range(n):
        for X in range(m):
            if field[Y][X]==1:
                result+=1
                dfs(X,Y)
    print(result)
