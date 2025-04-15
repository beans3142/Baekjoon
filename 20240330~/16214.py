from sys import stdin
input=stdin.readline

for i in range(int(input())):
    n,m=map(int,input().split())
    now=n
    bef=n%m
    while True:
        now=pow(now,n,m)
        if now==bef: break
    print(now)
