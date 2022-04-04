from sys import stdin
from math import gcd
input=stdin.readline

n=int(input())
n_arr=list(map(int,input().split()))
m=int(input())
m_arr=list(map(int,input().split()))

a=n_arr[0]
b=m_arr[0]

for i in range(1,n):
    a*=n_arr[i]
    
for i in range(1,m):
    b*=m_arr[i]
    
ans=str(gcd(a,b))

if len(ans)>9:
    for i in range(-9,0,1):
        print(ans[i],end='')
else:
    print(ans)
