from sys import stdin
input=stdin.readline
n=int(input())
do={i+1:[] for i in range(n)}
total=0
time_spend=[0]*n

for i in range(n):
    job=list(map(int,input().split()))
    print(job)
    time_spend[i]=job[0]
    for _ in range(job[1]):
        do[i+1].append(job[2+_])

for i in range(n):
    
