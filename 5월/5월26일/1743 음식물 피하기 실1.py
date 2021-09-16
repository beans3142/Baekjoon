# 기본 템플릿
#------------------------
#import sys
#import math
#import os
#import time
#from collections import *
#input=sys.stdin.readline
#dx=[1,-1,0,0] ; dy=[0,0,1,-1] # x,y 변화값 저장
#visited=[[False for i in range()]for j in range()] # 탐사용
#matrix=[[0 for i in range()]for j in range()] #x*y 매트릭스
#n,m=map(int,input().split()) # 값 두개 입력받기
# 입력받아 만들어지는 배열
#arr=list(map(int,input().split())) # 한줄에 여럿
#arr=[int(input()) for i in range()] #여러줄에 걸쳐 한줄
#arr=[list(map(int,input().split()))for i in range()] # 여러줄에 걸쳐 여러줄
#------------------------

import sys
input=sys.stdin.readline

n,m,k=map(int,input().split())
dx=[1,-1,0,0] ; dy=[0,0,1,-1]
matrix=[[0 for i in range(m)]for j in range(n)]
visited=[[False for i in range(m)]for j in range(n)]

for i in range(k):
    r,c=map(int,input().split())
    matrix[r-1][c-1]=1

trash=0

def bfs(x,y):
    cnt=1
    visited[x][y]=True
    queue=[[x,y]]
    while queue:
        nx,ny=queue.pop(0)
        for i in range(4):
            x=nx+dx[i]
            y=ny+dy[i]
            if 0<=x<n and 0<=y<m:
                if visited[x][y]==False and matrix[x][y]==1:
                    cnt+=1
                    visited[x][y]=True
                    queue.append([x,y])
    return cnt

for i in range(n):
    for j in range(m):
        if visited[i][j]==False and matrix[i][j]==1:
            trash=max(trash,bfs(i,j))

print(trash)
            
    
