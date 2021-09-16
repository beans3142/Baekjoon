from collections import deque
from sys import stdin
input=stdin.readline

n,m=map(int,input().split())

arr=[input().rstrip() for i in range(n)]
vi=[[0 for i in range(m)]for j in range(n)]

def bfs(x,y,cnt):
    

