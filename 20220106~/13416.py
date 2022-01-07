from sys import stdin
input=stdin.readline
t=int(input())
for i in range(t):
    n=int(input())
    money=0
    for j in range(n):
        a,b,c=map(int,input().split())
        money+=max(a,b,c,0)
    print(money)
        
