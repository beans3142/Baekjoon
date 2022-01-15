from sys import stdin
input=stdin.readline
n,m=map(int,input().split())
for i in range(n):
    print(input().rstrip()[::-1])
