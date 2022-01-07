from sys import stdin
input=stdin.readline

a=input().rstrip()
rev={"E":"I","I":"E","S":"N","N":"S","T":"F","F":"T","J":"P","P":"J"}

for i in a:
    print(rev[i],end='')
