from sys import stdin
input=stdin.readline
n=int(input())
f=int(input())

n-=n%100

for i in range(100):
    if (n+i)%f==0:
        break

print('%02d'%i)
