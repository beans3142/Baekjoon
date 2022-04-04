#https://www.acmicpc.net/problem/1292

a,b=map(int,input().split())
nl=[]

for i in range(1,b+1):
    nl+=[i]*i

print(sum(nl[a-1:b]))
