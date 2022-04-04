from sys import stdin
from math import ceil
input=stdin.readline

n=int(input())
arr=list(map(int,input().split()))
x,m=map(int,input().split())
print(ceil(len(arr)/(100/x)),len([i for i in arr if i >= m]))
