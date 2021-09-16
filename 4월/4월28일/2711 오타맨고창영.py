#https://www.acmicpc.net/problem/2711

t=int(input())
for i in range(0,t):
    n,m=input().split()
    n=int(n)-1
    for i in range(0,len(m)):
        if i!=n:
            print(m[i],end='')
    print()
