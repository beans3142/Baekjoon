from sys import stdin,setrecursionlimit
from collections import defaultdict
input=stdin.readline
setrecursionlimit(100000)

n,m=map(int,input().split())
level=[*map(int,input().split())]
tree={i:defaultdict(int) for i in range(1,n+1)}
praise=[0]*(n)

for person in range(1,n):
    tree[level[person]][person+1]=0

for i in range(m):
    whogetpraise,amount=map(int,input().split())
    praise[whogetpraise-1]+=amount # 실제 인덱스에 맞추기 위해 -1

def dfs(nowperson,totalpraised):
    praise[nowperson-1]+=totalpraised
    for i in tree[nowperson]:
        dfs(i,praise[nowperson-1])

dfs(1,0)

print(*praise)
