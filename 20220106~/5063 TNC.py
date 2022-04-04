n=int(input())

for i in range(n):
    r,e,c=map(int,input().split())
    if e==r+c:
        print('does not matter')
    elif e>r+c:
        print('advertise')
    else:
        print('do not advertise')

#https://www.acmicpc.net/problem/5063
