from sys import stdin
input=stdin.readline
t=int(input())
for i in range(t):
    n=int(input())
    hakjum=[]
    score=[]
    for j in range(n):
        a,b=input().rstrip().split()
        a=int(a)
        b=float(b)
        hakjum.append(a)
        score.append(b*a)
    print(sum(hakjum),sum(score)/sum(hakjum))
