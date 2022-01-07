from sys import stdin
input=stdin.readline

while True:
    a,b,c,d=map(int,input().split())
    if a==b==c==d==0:
        break
    print(abs(b-c),abs(a-d))
