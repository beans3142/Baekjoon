from sys import stdin
from bisect import *
input=stdin.readline

fibo=[0,1,2]
fibo[0]=-1
for i in range(500):
    fibo.append(fibo[-1]+fibo[-2])

while True:
    a,b=map(int,input().split())
    if a==b==0:
        break
    print(bisect_right(fibo,b)-bisect_left(fibo,a))
