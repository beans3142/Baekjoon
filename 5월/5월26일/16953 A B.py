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



import sys

input=sys.stdin.readline

a,b=map(int,input().split())

def bfs(x):
    queue=[[x,0]]
    while queue:
        i,cnt=queue.pop(0)
        m1=10*i+1
        m2=i*2
        if m1 == b or m2 == b:
            return cnt+1
        else:
            if m1<b:
                queue.append([m1,cnt+1])
            if m2<b:
                queue.append([m2,cnt+1])

result=bfs(a)
if result==None:
    print(-1)
else:
    print(result+1)
