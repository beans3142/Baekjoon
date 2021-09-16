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
#난이도 : 실버 5
#유형 : 자료구조,
#문제 주소 : https://www.acmicpc.net/problem/1158
#참고 : X
#만족도 : 3 ( 출제자가 원한 풀이는 아닐 것 )
#풀이 : 내장함수와 적절한 형태 사용

import sys ; input=sys.stdin.readline

r,d=map(int,input().split())

circle=list(range(1,r+1))
arr=[]
idx=0
while len(arr) != r:
    idx=(idx+d-1)%len(circle)
    arr.append(str(circle.pop(idx)))

print('<%s>'%', '.join(arr))
    
    
        

    
