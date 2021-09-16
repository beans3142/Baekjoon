        # 기본 템플릿 #
'''------------------------
import sys ; input=sys.stdin.readline
import math
import os
import time
from collections import *
dx=[1,-1,0,0] ; dy=[0,0,1,-1] # x,y 변화값 저장
visited=[[False for i in range()]for j in range()] # 2차원 탐사용
matrix=[[0 for i in range()]for j in range()] #x*y 매트릭스
n,m=map(int,input().split()) # 값 두개 입력받기
 입력받아 만들어지는 배열
arr=list(map(int,input().split())) # 한줄에 여럿
arr=[int(input()) for i in range()] #여러줄에 걸쳐 한줄
arr=[list(map(int,input().split()))for i in range()] # 여러줄에 걸쳐 여러줄
------------------------'''

# 골 4 인데 존나어려움 RUN!

import sys ; input=sys.stdin.readline

n=int(input())

dx=[0,0,-1,1] ; dy=[1,-1,0,0]

sea=[list(map(int,input().split()))for i in range(n)]
eat_left=0

for i in range(n):
    eat_left+=sum(sea[i])
    if 9 in sea[i]:
        shark_locate=[i,sea[i].index(9)]

def bfs(x,y):
    global eat_left
    time=0
    sharksize=2
    eat=0
    queue=[[x,y]]
    while queue:
        if eat_left==9:
            break
        x,y=queue.pop(0)
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if sea[ny][nx]>sharksize:
                    continue
                elif 0<sea[ny][nx]<sharksize:
                    sea[ny][nx]=0
                    eat+=1
                    if eat==sharksize:
                        eat=0
                        sharksize+=1
                time+=1
                eat_left-=sea[ny][nx]
                queue.append([nx,ny])
    return time

bfs(shark_locate[0],shark_locate[1])
                    

