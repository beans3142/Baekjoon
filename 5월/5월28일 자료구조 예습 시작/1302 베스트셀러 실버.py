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

#난이도 : 실버 중하위권
#유형 : 자료구조
#https://www.acmicpc.net/problem/1302
#참고 : X 
#만족도 : 4
#풀이 : 스킵
#       

import sys ; input=sys.stdin.readline

n=int(input())

sold={}
bestseller=0

for i in range(n):
    book=input().rstrip()
    if book not in sold:
        sold[book]=1
    else:
        sold[book]+=1
    bestseller=max(sold[book],bestseller)

for k in sorted(sold):
    if sold[k]==bestseller:
        print(k)
        break

'''
import sys ; input=sys.stdin.readline

arr=[input().rstrip() for i in range(int(input()))]

bestseller=0
for i in set(sorted(arr)):
    bestseller=max(bestseller,arr.count(i))

for i in sorted(set(arr)):
    if arr.count(i)==bestseller:
        break

print(i)
'''
    
