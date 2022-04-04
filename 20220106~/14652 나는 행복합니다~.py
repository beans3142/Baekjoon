from sys import stdin
input=stdin.readline
n,m,k=map(int,input().split())
print((k-1)//m,(k-1)//n)
