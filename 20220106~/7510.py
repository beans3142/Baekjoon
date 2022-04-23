from sys import stdin
input=stdin.readline

n=int(input())
for i in range(n):
    three=sorted(map(int,input().split()))
    print("Scenario #%d:"%(i+1))
    if three[0]**2+three[1]**2==three[2]**2:
        print("yes\n")
    else:
        print("no\n")
