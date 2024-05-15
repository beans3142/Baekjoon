from sys import stdin
input=stdin.readline

e,s,m=map(int,input().split())
t=max(e,s,m)
if e==t:
    add=15
elif s==t:
    add=28
else:
    add=19
now=t
while True:
    te=15 if now%15==0 else now%15
    ts=28 if now%28==0 else now%28
    tm=19 if now%19==0 else now%19
    if te==e and ts==s and tm==m:
        break
    now+=add
        
print(now)
