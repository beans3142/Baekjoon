from collections import defaultdict
from sys import stdin
input=stdin.readline

cnt+=1
n,c=map(int,input().split())
v=defaultdict(int)
arr=sorted(list(map(int,input().split())))

def ls(x,idx):
    for i in range(idx,n//2):
        v[c[i]]=1
    
