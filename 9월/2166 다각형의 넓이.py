from sys import stdin
from math import fabs
input=stdin.readline

n=int(input())

arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))

arr.append(arr[0])

p=0
m=0

for i in range(n):
    p+=arr[i][0]*arr[i+1][1]
    m+=arr[i][1]*arr[i+1][0]

area=fabs(0.5*(p-m))
print(round(area,2))
