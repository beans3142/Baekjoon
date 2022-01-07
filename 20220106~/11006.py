from sys import stdin
input=stdin.readline

t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    cut=2*m-n
    print(cut,m-cut)
