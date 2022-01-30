from sys import stdin
input=stdin.readline

n=int(input())
th=64
while n%2==0:
    n//=2 
    th-=1
print(th)
