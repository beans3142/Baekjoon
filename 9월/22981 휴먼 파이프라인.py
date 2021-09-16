from sys import stdin
input=stdin.readline
n,k=map(int,input().split())
people=sorted(map(int,input().split()))
mn=10**18
for i in range(1,n):
    team=(i*people[0]+(n-i)*people[i])
    if k%team==0:
        time=k//team
    else:
        time=k//team+1
    mn=min(mn,time)

print(mn)

