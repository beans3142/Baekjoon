from sys import stdin
input=stdin.readline

n,w,h,l=map(int,input().split())
print(min(n,(w//l)*(h//l)))
