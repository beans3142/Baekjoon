#https://www.acmicpc.net/problem/2439

n=int(input())

for i in range(n,0,-1):
    print(str('*'*i).rjust(n,' '))
