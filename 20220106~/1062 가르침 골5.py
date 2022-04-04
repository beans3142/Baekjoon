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
#n,m=map(int,input().split())
#arr=list(map(int,input().split()))
#arr=[int(input()) for i in range()]
#arr=[list(map(int,input().split()))for i in range()]
#alphabet=[chr(i) for i in range(97,123)]
#arr=[]
#------------------------

import sys
input=sys.stdin.readline
n,k=map(int,input().split())
arr=[input() for i in range(n)]
# antic <- 최소한 포함되어야 하는 것
result=0

alphabet=[chr(i) for i in range(97,123)]

if k<5:
    print(0)
else:
    k-=5
    use_list=list('antic')
    spell_list=[]
    for i in range(n):
        arr[i]=arr[i][4:-5]
        arr[i]={w for w in arr[i] if w not in use_list}
        if len(arr[i])<=k:
            for w in arr[i]:
                if w not in spell_list:
                    spell_list.append(w)
    
    for i in arr:
        for w in i:
            if w not in use_list:
                result-=1
                break
        result+=1
                
    
    
        
