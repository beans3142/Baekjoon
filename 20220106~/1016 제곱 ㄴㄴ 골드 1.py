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

mn,mx=map(int,input().split())
arr=[1 for i in range(mx-mn+1)]

n=2

while n**2<=mx:
    x=mn//(n**2)
    while x*(n**2) <= mx:
        if x * (n**2) - mn >=0 and x * (n**2) <= mx:
            arr[x*(n**2)-mn]=0
        x+=1
    n+=1

print(sum(arr))
    
    
