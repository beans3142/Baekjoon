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
#난이도 :
#유형 :
#문제 주소
#참고 : 
#만족도 : 
#풀이 :
'''
import sys ; input=sys.stdin.readline

n,k=map(int,input().split())

arr=list(map(int,input().split()))

made=[arr]
temp={str(arr):0}

if arr!=sorted(arr):
    arr=sorted(arr)
else:
    print(0)
    exit()

for i in made:
    for j in range(n-1):
        if i[j]>i[j+1]:
            s=i[:j]+list(reversed(i[j:j+k]))+i[j+k:]
            if s not in made:
                if s == arr:
                    print(temp[str(i)]+1)
                made.append(s)
                temp[str(s)]=temp[str(i)]+1

print(-1)
'''
from collections import deque

N,K=map(int,input().split())
L=list(input().split())


visitedS=set("".join(L))
q=deque([["".join(L),0]])

ans=-1
while(q):
    word,cnt=q.popleft()
    tempL=list(word)
    #print(tempL,cnt)

    # 오름차순이면 그만
    if tempL==sorted(tempL):
        ans=cnt
        break

    isFirst=False
    # i를 뒤집기
    for i in range(N-K+1):
        print(q)
        newL = list(tempL)
        targetL=newL[i:i+K]
        targetL.reverse()
        for j in range(K):
            newL[i+j]=targetL[j]
        newWord="".join(newL)
        if newWord not in visitedS:
            visitedS.add(newWord)
            q.append([newWord,cnt+1])

print(ans)

