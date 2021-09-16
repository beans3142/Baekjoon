#https://www.acmicpc.net/problem/5054

t=int(input())

for i in range(0,t):
    n=int(input())
    nl=list(map(int,input().split()))
    print(2*(max(nl)-min(nl)))
