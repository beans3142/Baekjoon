from sys import stdin
input=stdin.readline


for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    s=0
    for i in range(n):
        s+=arr[i]^arr[i-1]
    print(s)
