from sys import stdin
input=stdin.readline

n=int(input())
for i in range(1,n+1):
    if 31%(i+1)==1:
        print(i)
