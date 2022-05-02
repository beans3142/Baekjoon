from sys import stdin
from collections import defaultdict
input=stdin.readline

n,p=map(int,input().split())
w,l,goal=map(int,input().split())
dd=defaultdict(int)
score=0

for i in range(p):
    name,res=input().rstrip().split()
    dd[name]=w if res=='W' else -l

for i in range(n):
    playwith=input().rstrip()
    score=max(0,score+(dd[playwith] if playwith in dd else -l))
    print(score)
    if score>=goal:
        print("I AM NOT IRONMAN!!")
        exit()
        
print("I AM IRONMAN!!")

