from sys import stdin
input=stdin.readline
isprime=[1]*(130000*2)
isprime[0]=isprime[1]=0
beforeprime=[0]*(130000*2)

for i in range(2,55000):
    if isprime[i]==0:
        continue
    for j in range(i+i,260000,i):
        isprime[j]=0
cnt=0
for i in range(2,260000):
    cnt+=isprime[i]
    beforeprime[i]=cnt
while True:
    n=int(input())
    if n==0:
        break
    print(beforeprime[2*n]-beforeprime[n])
    
