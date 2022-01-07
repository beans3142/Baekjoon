from sys import stdin
input=stdin.readline
a,b,c=map(int,input().split())
print(int(max(a*b/c,a/b*c)))
