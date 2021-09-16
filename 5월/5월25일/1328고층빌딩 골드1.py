#default template
#------------------------
import sys
#import math
#import os
#import time
#from collections import *
input=sys.stdin.readline
#dx=[1,-1,0,0] ; dy=[0,0,1,-1]
#visited=[[False for i in range()]for j in range()]
#arr=list(map(int,input().split()))
#arr=[int(input()) for i in range()]
#arr=[list(map(int,input().split()))for i in range()]
#arr=[]
#------------------------

'''
n,l,r=map(int,input().split())

# n은 가장 높은 건물의 높이와도 같긴 함
# n은 어디서 보던 무조건 보임 => l-1 r-1을 해줘도 되지 않을까?
# n을 기준으로 왼쪽에 건물이 최대가 될 경우 = n-r-1 최소가 될 경우 l-1
# l-1+r-1개 만큼의 블럭을

for i in range(l-1,n-r+1):
    pass


'''

import sys

N, L, R = map(int, sys.stdin.readline().split())
dp = [[[0 for _ in range(R + 1)]for __ in range(L + 1)]
      for ___ in range(N + 1)]
dp[1][1][1] = 1
for i in range(2, N + 1):
    for j in range(1, L + 1):
        for k in range(1, R + 1):
            dp[i][j][k] = (dp[i-1][j][k]*(i-2) % 1000000007
                           + dp[i-1][j][k-1] % 1000000007
                           + dp[i-1][j-1][k] % 1000000007)
print(dp[N][L][R] % 1000000007)

