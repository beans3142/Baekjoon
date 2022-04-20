from sys import stdin
input=stdin.readline

prime=[1]*(1000001)
prime[0]=prime[1]=0
mx=int(1000001**0.5)
for i in range(2,mx+1):
    if prime[i]==0:
        continue
    for j in range(i+i,1000001,i):
        prime[j]=0

while True:
    n=int(input())
    if n==0:
        break
    for i in range(2,n):
        if prime[i]==prime[n-i]==1:
            print(f'{n} = {i} + {n-i}')
            break
