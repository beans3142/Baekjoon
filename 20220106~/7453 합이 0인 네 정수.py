from sys import stdin
from collections import defaultdict
input=stdin.readline

n=int(input())
arr=[]
cnt=0
for i in range(n):
    arr.append(list(map(int,input().split())))

two={}
for i in range(n):
    for j in range(n):
        try:
            two[arr[i][0]+arr[j][1]]+=1
        except:
            two[arr[i][0]+arr[j][1]]=1

for i in range(n):
    for j in range(n):
        try:
            cnt+=two[-(arr[i][2]+arr[j][3])]
        except:
            pass

print(cnt)
