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

import sys ; input=sys.stdin.readline
from collections import *

s=int(input())
mn=1000

def bfs(x):
    global mn
    visited=[0 for i in range(2000)]
    queue=deque([[x,0,0]])
    while queue:
        n,clip,cnt=queue.popleft()
        if n < s:
            if clip != n:
                queue.append([n,n,cnt+1])
            if n+clip<=int(s*1.5) and clip != 0:
                queue.append([n+clip,clip,cnt+1])
            if mn>cnt and n>1 and visited[n-1]==0:
                visited[n-1]=1
                queue.append([n-1,clip,cnt+1])
            
        else:
            mn=min(mn,n-s+cnt)

bfs(1)

print(mn)

        
