        # 기본 템플릿 #
'''------------------------
import sys ; input=sys.stdin.readline
import math
import os
import time
from collections import *
input=sys.stdin.readline
dx=[1,-1,0,0] ; dy=[0,0,1,-1] # x,y 변화값 저장
visited=[[False for i in range()]for j in range()] # 2차원 탐사용
matrix=[[0 for i in range()]for j in range()] #x*y 매트릭스
n,m=map(int,input().split()) # 값 두개 입력받기
 입력받아 만들어지는 배열
arr=list(map(int,input().split())) # 한줄에 여럿
arr=[int(input()) for i in range()] #여러줄에 걸쳐 한줄
arr=[list(map(int,input().split()))for i in range()] # 여러줄에 걸쳐 여러줄
------------------------'''

#https://www.acmicpc.net/problem/2606
#티어 : 실버3
#분류 : 그래프

import sys ; input=sys.stdin.readline

n=int(input())
connect=int(input())
visited=[False for i in range(n)]
virus=0

matrix=[[0 for i in range(n)]for j in range(n)]

for i in range(connect):
    a,b=map(int,input().split())
    matrix[a-1][b-1]=matrix[b-1][a-1]=1

def dfs(x):
    global virus
    visited[x]=True
    for i in range(n):
        if matrix[x][i]==1 and visited[i]==False:
            matrix[x][i]=matrix[i][x]=0
            virus+=1
            dfs(i)

dfs(0)

print(virus)
    
