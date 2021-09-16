#https://www.acmicpc.net/problem/3460

t=int(input())

for i in range(1,t+1):
    n=bin(int(input()))
    for i in range(1,len(n)):
        if n[-i]=='1':
            print(i-1)
