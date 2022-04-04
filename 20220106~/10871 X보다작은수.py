#https://www.acmicpc.net/problem/10871

n,x=map(int,input().split())

nl=list(map(int,input().split()))

for i in nl:
    if i<x:
        print(i,end=' ')
