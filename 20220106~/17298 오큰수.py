#https://www.acmicpc.net/problem/17298
from sys import stdin
from collections import deque
input=stdin.readline

n=int(input())
arr=list(map(int,input().split()))
oken_arr=[0]*n
queue=[]
for i,num in enumerate(arr):
    if queue:
        if queue[-1][0]>=num:
            queue.append([num,i])
        try:
            while queue[-1][0]<num:
                N,idx=queue.pop()
                oken_arr[idx]=num
        except:
            queue.append([num,i])
    queue.append([num,i])

for i in oken_arr:
    print(i if i != 0 else -1,end=' ')
            

