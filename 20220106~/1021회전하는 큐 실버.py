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
#난이도 : 실버 중하위
#유형 : 자료구조 / 해시?
#문제 주소 : https://www.acmicpc.net/problem/1021
#참고 : X
#만족도 : 
#풀이 :

import sys ; input=sys.stdin.readline

l,n=map(int,input().split())
extract=list(map(int,input().split()))

queue=list(range(1,l+1))
temp=0 # n번 빼므로

while extract:
    order=extract.pop(0)
    if queue.index(order) <= len(queue)-queue.index(order):
        while order != queue[0]:
            queue.append(queue.pop(0))
            temp+=1
        queue.pop(0)
    else:
        while order != queue[0]:
            queue.insert(0,queue.pop(-1))
            temp+=1
        queue.pop(0)

print(temp)
