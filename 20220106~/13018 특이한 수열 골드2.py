#https://www.acmicpc.net/problem/13018
n,k=map(int,input().split())
nl=[i for i in range(1,n+1)]
if n-k<1 and k != 0:
    print('Impossible')
else:
    nl=nl[1:n-k]+[nl[0]]+nl[n-k:]
    print(*nl)
