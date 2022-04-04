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

#https://www.acmicpc.net/problem/1068
#rank : gold5
#type : dfs, tree, graph

import sys
input=sys.stdin.readline
n=int(input())
arr=list(map(int,input().split()))
del_n=int(input())
leaf=0

tree={}

for i in set(arr):
    tree[i]=[]

visited=[False]*(n+1)

for j,i in enumerate(arr):
    if j!=del_n:
        tree[i].append(j)

if del_n in tree:
    tree.pop(del_n)


def dfs(x):
    global leaf
    visited[x]=True
    if x in tree:
        for i in tree[x]:
            if i not in tree:
                leaf+=1
            elif not tree[i]:
                leaf+=1
            elif visited[i]==False and i != del_n:
                dfs(i)

dfs(-1)

print(leaf)

