from sys import stdin
input=stdin.readline
n,m=map(int,input().split())
if m<3:
    print("NEWBIE!")
elif m<=n:
    print("OLDBIE!")
else:
    print("TLE!")
