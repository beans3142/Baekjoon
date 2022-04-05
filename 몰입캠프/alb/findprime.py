from sys import stdin
input=stdin.readline
n=int(input())

isprime=[1]*1001 # 에라토스테네스
isprime[0]=isprime[1]=0
for i in range(2,33):
    if isprime[i]!=1:
        continue
    for i in range(i+i,1001,i):
        isprime[i]=0
cnt=0
for i in range(n):
    cnt+=isprime[int(input())]
print(cnt)
