from itertools import*
n=int(input())
a=[[*map(int,input().split())] for i in range(n)]+[(1,0)]*(n-1)
r=1e9
for i in combinations(a,n):
    m,s=1,0
    for M,S in i:
        m*=M
        s+=S
    r=min(abs(m-s),r)
print(r)