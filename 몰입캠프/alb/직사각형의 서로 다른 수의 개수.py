from collections import defaultdict
from sys import stdin
from copy import deepcopy
input=stdin.readline

n=int(input())
arr=[list(map(int,input().split())) for i in range(n)]
presum=[[defaultdict(int) for i in range(n)] for i in range(n)]
presum[0][0][arr[0][0]]+=1

for i in range(1,n):
    
    presum[0][i]=deepcopy(presum[0][i-1])
    presum[i][0]=deepcopy(presum[i-1][0])
    presum[0][i][arr[0][i]]+=1
    presum[i][0][arr[i][0]]+=1


for i in range(1,n):
    for j in range(1,n):
        presum[i][j]
