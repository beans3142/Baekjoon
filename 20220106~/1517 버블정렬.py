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
#난이도 : 골드 1 21/05/30 기준 혼자 푼 문제중 가장 높음.
#유형 : 자료구조, 정렬, 분할 정복
#문제 주소 : https://www.acmicpc.net/status?user_id=beans3142&problem_id=1517&from_mine=1
#참고 : 정답 체크용으로 사용 https://suri78.tistory.com/143
#만족도 : 8
#풀이 : 병합 정렬로 풀음, l내에서 l1은 무조건 왼쪽 l2는 오른쪽임을 이용, 기타등등.

import sys ; input=sys.stdin.readline

n=int(input())
arr=list(map(int,input().split()))

swap=0

def merge(l):
    global swap
    if len(l)==1:
        return
    mid=len(l)//2
    
    l1=l[:mid]
    l2=l[mid:]
    
    merge(l1)
    merge(l2)

    i1=0
    i2=0
    idx=0
    ds=0
    
    while i1<len(l1) and i2<len(l2):
        if l1[i1]<=l2[i2]:
            l[idx]=l1[i1]
            idx+=1
            i1+=1
            swap+=ds
        else:
            ds+=1
            l[idx]=l2[i2]
            idx+=1
            i2+=1

    while i1<len(l1):

        l[idx]=l1[i1]
        idx+=1
        i1+=1
        swap+=ds
        
    while i2<len(l2):

        l[idx]=l2[i2]
        idx+=1
        i2+=1
        

merge(arr)
print(swap)

'''
import sys ; input=sys.stdin.readline

n=int(input())
arr=list(map(int,input().split()))
swap=0
sarr=sorted(arr)
     
while arr:
    l=arr.index(sarr[n-1])
    swap+=n-1-l
    arr.pop(l)
    n-=1

print(swap)
'''
'''
n=int(input())
arr=list(map(int,input().split()))
swap=0

for i in range(n):
    for j in range(i+1,n):
        if arr[i]>arr[j]:
            swap+=1

print(swap)
'''
'''
n=int(input())
arr=list(map(int,input().split()))

swap=0


def burble(l):
    global swap
    if len(l)==1:
        return swap
    for i in range(1,len(l)):
        if l[i-1]>l[i]:
            swap+=1
            l[i],l[i-1]=l[i-1],l[i]

    return burble(l[:-1])

print(burble(arr))
'''
