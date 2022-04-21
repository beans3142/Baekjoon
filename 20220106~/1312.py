from sys import stdin
input=stdin.readline

under=[]
a,b,n=map(int,input().split())
r=a%b
while len(under)<n:
    under.append((r*10)//b)
    r=10*r-under[-1]*b

print(under[-1])
