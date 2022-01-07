from sys import stdin
input=stdin.readline
n=int(input())
s=1
for i in range(n):
    s+=int(input())
print(s-n)
