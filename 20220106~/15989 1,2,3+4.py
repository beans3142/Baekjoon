#default template
#------------------------
#import sys
#import math
#import os
#import time
#from collections import *
#input=sys.stdin.readline
#dx=[1,-1,0,0] ; dy=[0,0,1,-1]
#visited=[[False for i in range()]for j in range()]
#arr=list(map(int,input().split()))
#arr=[int(input()) for i in range()]
#arr=[list(map(int,input().split()))for i in range()]
#arr=[]
#------------------------

# type = dp
# rank = gold
# 포기..

import sys
input=sys.stdin.readline

#1 : 1 => 1
#2 : 1+1, 2 => 2
#3 : 1+1+1,1+2, 3 => 3
#4 : 1+1+1+1, 1+1+2, 2+2, 1+3 => 4
#5 : 1+1+1+1+1, 1+1+1+2, 1+2+2, 1+1+3, 2+3 => 5
#6 : 1+1+1+1+1+1, 1+1+1+1+2, 1+1+2+2, 1+1+1+3, 1+2+3, 2+2+2, 3+3 => 7
#7 : 1+1+1+1+1+1+1, 1+1+1+1+1+2, 1+1+1+2+2, 1+1+1+1+3, 1+1+2+3, 1+2+2+2, 1+3+3,
#    2+2+3 => 8
#8   8+2
#
#
#10 : 14

# 2 4 6 8



# 6 [5][4][2]

# 1로 시작하는 것의 갯수 = n-1?
# n-1 + 2로 시작하는것의 개수 + 3으로 시작하는 것의 개수?
# 7의 경우 6+1+1.. 8
# 10경우 14

# 1 2 3 4 5 7 8 10 12 14


t=int(input())
for i in range(t):
    n=int(input())
    dp=[0]*n
    
